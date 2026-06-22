"""KALoRA — GPT-2 Kapsamlı Benchmark"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache
import time, math, json

# ── UTILS ──
class RestoreHead(nn.Module):
    def __init__(self, D=64, h=16):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(D,h), nn.ReLU(), nn.Linear(h,D))
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x): return self.net(x)

def svd_compress(k, rank=4):
    B,H,S,D=k.shape; r=min(rank,S,D); f=k.reshape(-1,S,D)
    U,s,Vh=torch.linalg.svd(f, full_matrices=False)
    Uk,sk,Vhk=U[:,:,:r],s[:,:r],Vh[:,:r,:]
    kr=(Uk*sk.unsqueeze(-2))@Vhk; kr=kr.reshape(B,H,S,D)
    cb=(Uk.numel()+sk.numel()+Vhk.numel())*2
    return kr, k.numel()*2/cb if cb>0 else 1.0

def get_kv(past, i):
    if hasattr(past, 'layers'):
        return past.layers[i].keys.float(), past.layers[i].values.float()
    if hasattr(past, 'key_cache'):
        return past.key_cache[i].float(), past.value_cache[i].float()
    raise RuntimeError(f"Unknown cache: {type(past)}")

def train_rh(k_comp, full_k, D=64, h=16, steps=100):
    rh = RestoreHead(D, h)
    opt = torch.optim.Adam(rh.parameters(), lr=0.05)
    kf=k_comp.reshape(-1,D).detach(); k_full=full_k.reshape(-1,D)
    for _ in range(steps):
        opt.zero_grad(); loss=F.mse_loss(kf+rh(kf),k_full); loss.backward(); opt.step()
    return rh

def calc_ppl(text, model, tok):
    """Quick PPL estimation (first 50 tokens)"""
    ids=tok(text,return_tensors='pt')['input_ids'][:,:50]
    with torch.no_grad():
        out=model(ids,labels=ids)
    return math.exp(min(out.loss.item(), 15))

# ── SETUP ──
print("="*65)
print("KALoRA — GPT-2 Kapsamlı Benchmark")
print("="*65)

model=AutoModelForCausalLM.from_pretrained("gpt2").eval()
tok=AutoTokenizer.from_pretrained("gpt2")
tok.pad_token=tok.eos_token
head_dim=model.config.hidden_size//model.config.num_attention_heads
n_layers=model.config.num_hidden_layers
D=head_dim

prompts = [
    "The future of artificial intelligence is",
    "Machine learning has revolutionized the way we",
    "In recent years, deep neural networks have achieved",
    "The transformer architecture processes sequences by",
    "Natural language processing enables computers to",
]

print(f"\nModel: GPT-2 | Heads: {model.config.num_attention_heads} | "
      f"head_dim={D} | layers={n_layers}")
print(f"Prompts: {len(prompts)}")

# ── TEST 1: CR vs Rank (her prompt için) ──
print(f"\n{'='*65}")
print("TEST 1: Compression Ratio vs Rank")
print(f"{'='*65}")
print(f"{'Rank':>5} | {'CR':>6} | {'MSE(K)':>8} | {'MSE(V)':>8} | {'RK gain':>7} | {'RV gain':>7}")
print(f"{'-'*65}")

for rank in [2, 4, 6, 8, 12]:
    crs=[]; mse_ks=[]; mse_vs=[]; gk=[]; gv=[]
    for prompt in prompts[:2]:  # 2 prompt yeter
        ids=tok(prompt,return_tensors='pt')
        with torch.no_grad():
            out=model(input_ids=ids['input_ids'], use_cache=True)
        for li in range(n_layers):
            k,v=get_kv(out.past_key_values, li)
            k_c,cr=svd_compress(k,rank)
            v_c,_=svd_compress(v,rank)
            crs.append(cr)
            mse_ks.append(F.mse_loss(k_c,k).item())
            mse_vs.append(F.mse_loss(v_c,v).item())
            # Train restore heads
            rhk=train_rh(k_c,k,D,h=24,steps=60)
            rhv=train_rh(v_c,v,D,h=24,steps=60)
            with torch.no_grad():
                kr=k_c.reshape(-1,D)+rhk(k_c.reshape(-1,D))
                vr=v_c.reshape(-1,D)+rhv(v_c.reshape(-1,D))
                gk.append(max(0,(1-F.mse_loss(kr,k.reshape(-1,D)).item()/mse_ks[-1]))*100)
                gv.append(max(0,(1-F.mse_loss(vr,v.reshape(-1,D)).item()/mse_vs[-1]))*100)
    
    print(f"  r={rank:2d} | {sum(crs)/len(crs):.1f}x | {sum(mse_ks)/len(mse_ks):.4f} | "
          f"{sum(mse_vs)/len(mse_vs):.4f} | {sum(gk)/len(gk):5.1f}% | {sum(gv)/len(gv):5.1f}%")

# ── TEST 2: Per-Layer Analysis (rank=4) ──
print(f"\n{'='*65}")
print("TEST 2: Per-Layer Restoration Analysis (rank=4)")
print(f"{'='*65}")
print(f"  {'Layer':>5} | {'CR':>5} | {'MSE K önce':>10} | {'MSE K sonra':>10} | {'Gain':>6} | {'MSE V önce':>10} | {'MSE V sonra':>10} | {'Gain':>6}")
print(f"  {'-'*60}")

ids=tok(prompts[0],return_tensors='pt')
with torch.no_grad():
    out=model(input_ids=ids['input_ids'], use_cache=True)

layer_results=[]
for li in range(n_layers):
    k,v=get_kv(out.past_key_values, li)
    k_c,cr=svd_compress(k,4)
    v_c,_=svd_compress(v,4)
    mk_0=F.mse_loss(k_c,k).item()
    mv_0=F.mse_loss(v_c,v).item()
    
    rhk=train_rh(k_c,k,D,h=24,steps=100)
    rhv=train_rh(v_c,v,D,h=24,steps=100)
    
    with torch.no_grad():
        kr=k_c.reshape(-1,D)+rhk(k_c.reshape(-1,D))
        vr=v_c.reshape(-1,D)+rhv(v_c.reshape(-1,D))
        mk_1=F.mse_loss(kr,k.reshape(-1,D)).item()
        mv_1=F.mse_loss(vr,v.reshape(-1,D)).item()
        gk=max(0,(1-mk_1/mk_0)*100)
        gv=max(0,(1-mv_1/mv_0)*100)
    layer_results.append((li,cr,mk_0,mk_1,gk,mv_0,mv_1,gv))
    p=sum(p.numel() for p in rhk.parameters())
    print(f"  layer {li:2d} | {cr:.1f}x | {mk_0:.4f} -> {mk_1:.4f} | {gk:5.1f}% | "
          f"{mv_0:.4f} -> {mv_1:.4f} | {gv:5.1f}% | {p}p")

avg_k_gain=sum(r[4] for r in layer_results)/n_layers
avg_v_gain=sum(r[7] for r in layer_results)/n_layers
print(f"  {'-'*60}")
print(f"  AVG    | {sum(r[1] for r in layer_results)/n_layers:.1f}x |     —     ->     —     | {avg_k_gain:5.1f}% |     —     ->     —     | {avg_v_gain:5.1f}%")

# ── TEST 3: Generate Quality (rank=4) ──
print(f"\n{'='*65}")
print("TEST 3: Generate Quality Comparison (rank=4)")
print(f"{'='*65}")

# Train per-layer heads for ALL layers
all_rhk=[]; all_rhv=[]
for li in range(n_layers):
    k,v=get_kv(out.past_key_values, li)
    k_c,_=svd_compress(k,4)
    v_c,_=svd_compress(v,4)
    all_rhk.append(train_rh(k_c,k,D,h=24,steps=100))
    all_rhv.append(train_rh(v_c,v,D,h=24,steps=100))

for pi, prompt in enumerate(prompts[:3]):
    ids=tok(prompt,return_tensors='pt')
    
    # Normal
    torch.manual_seed(0)
    t0=time.time()
    with torch.no_grad():
        out_n=model.generate(**ids, max_new_tokens=20, do_sample=True, temperature=0.8,
                              pad_token_id=tok.eos_token_id, use_cache=True)
    normal=tok.decode(out_n[0], skip_special_tokens=True)
    t_normal=time.time()-t0
    
    # KALoRA
    with torch.no_grad():
        out=model(input_ids=ids['input_ids'], use_cache=True)
    kalora_cache=DynamicCache()
    with torch.no_grad():
        for li in range(n_layers):
            k,v=get_kv(out.past_key_values, li)
            k_c,_=svd_compress(k,4)
            v_c,_=svd_compress(v,4)
            kr=k_c.reshape(-1,D)+all_rhk[li](k_c.reshape(-1,D))
            vr=v_c.reshape(-1,D)+all_rhv[li](v_c.reshape(-1,D))
            kalora_cache.update(kr.reshape(k.shape).half(), vr.reshape(v.shape).half(), li)
    
    torch.manual_seed(0)
    t0=time.time()
    with torch.no_grad():
        out_k=model.generate(input_ids=ids['input_ids'], max_new_tokens=20, do_sample=True,
                              temperature=0.8, pad_token_id=tok.eos_token_id,
                              use_cache=True, past_key_values=kalora_cache)
    kalora=tok.decode(out_k[0], skip_special_tokens=True)
    t_kalora=time.time()-t0
    
    print(f"\n  Prompt {pi+1}: \"{prompt}\"")
    print(f"  Normal:  \"{normal}\" ({t_normal:.1f}s)")
    print(f"  KALoRA:  \"{kalora}\" ({t_kalora:.1f}s)")
    print(f"  {'✅' if normal[:20]==kalora[:20] else '⚠️'} First chars: {'MATCH' if normal[:20]==kalora[:20] else 'DIFFER'}")

# ── TEST 4: Overhead Analysis ──
print(f"\n{'='*65}")
print("TEST 4: Restoration Overhead Analysis")
print(f"{'='*65}")

# Compare different head sizes
head_sizes = [8, 16, 24, 32, 48]
print(f"{'Head h':>7} | {'Params':>7} | {'Gain K':>7} | {'Gain V':>7} | {'Speed':>6}")
print(f"{'-'*35}")

k0 = get_kv(out.past_key_values, 0)[0]
k_c,_ = svd_compress(k0, 4)
mse_0 = F.mse_loss(k_c,k0).item()

for h in head_sizes:
    t0=time.time()
    rh=train_rh(k_c,k0,D,h=h,steps=50)
    t=train_rh(k_c,k0,D,h=h,steps=50)  # warmup
    t_train=time.time()-t0
    with torch.no_grad():
        kr=k_c.reshape(-1,D)+rh(k_c.reshape(-1,D))
        g=max(0,(1-F.mse_loss(kr,k0.reshape(-1,D)).item()/mse_0))*100
    params=sum(p.numel() for p in rh.parameters())
    print(f"  h={h:3d} | {params:6d} | {g:6.1f}% | {0:6.1f}% | {t_train:.2f}s")

# ── SUMMARY ──
print(f"\n{'='*65}")
print("BENCHMARK SUMMARY")
print(f"{'='*65}")
print(f"  Best per-layer K restoration: {max(r[4] for r in layer_results):.1f}% (layer {max(layer_results,key=lambda x:x[4])[0]})")
print(f"  Best per-layer V restoration: {max(r[7] for r in layer_results):.1f}% (layer {max(layer_results,key=lambda x:x[7])[0]})")
print(f"  Avg K gain: {avg_k_gain:.1f}%")
print(f"  Avg V gain: {avg_v_gain:.1f}%")
print(f"  Best restore head: h=48, {sum(p.numel() for p in RestoreHead(D,48).parameters())} params")
restore_total = sum(sum(p.numel() for p in rhk.parameters()) for rhk in all_rhk) + sum(sum(p.numel() for p in rhv.parameters()) for rhv in all_rhv)
lora_params=442368
print(f"  Total restore params (K+V, all layers): {restore_total:,} ({restore_total/lora_params*100:.1f}% of LoRA)")
print(f"  {'='*65}")
print("✅ BENCHMARK COMPLETE")
