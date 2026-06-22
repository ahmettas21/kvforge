# KALoRA — Kaggle PPL Benchmark (multi-rank)
import os, math, warnings, json, time
warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache

MODEL = "Qwen/Qwen2.5-1.5B"
N_SAMPLES = 30
MAX_LEN = 256
RANKS = [4, 6]

print(f"Model: {MODEL}")
print(f"Ranks: {RANKS} | Samples: {N_SAMPLES}")
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Device: {device}")

class RestoreHead(nn.Module):
    def __init__(self, D, h):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(D,h), nn.ReLU(), nn.Linear(h,D))
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x): return self.net(x)

def svd_compress(k, rank):
    B,H,S,D=k.shape; r=min(rank,S,D); kf=k.float().reshape(-1,S,D)
    U,s,Vh=torch.linalg.svd(kf, full_matrices=False)
    Uk,sk,Vhk=U[:,:,:r],s[:,:r],Vh[:,:r,:]
    kr=(Uk*sk.unsqueeze(-2))@Vhk; kr=kr.reshape(B,H,S,D)
    cb=(Uk.numel()+sk.numel()+Vhk.numel())*2
    ob=k.numel()*2
    return kr, ob/cb if cb>0 else 1.0

# ── Load model once ──
print("\nLoading...")
t0=time.time()
model=AutoModelForCausalLM.from_pretrained(MODEL).eval()
tok=AutoTokenizer.from_pretrained(MODEL); tok.pad_token=tok.eos_token
cfg=model.config; head_dim=cfg.hidden_size//cfg.num_attention_heads; n_layers=cfg.num_hidden_layers
print(f"  {sum(p.numel() for p in model.parameters())/1e6:.1f}M | {head_dim=} | {n_layers} layers | {time.time()-t0:.1f}s")

# ── Dataset ──
print("\nLoading WikiText-2...")
from datasets import load_dataset
ds=load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
texts=[t['text'] for t in ds if len(t['text'].strip())>50][:N_SAMPLES]
print(f"  {len(texts)} samples")

# ── Calibration text ──
calib = ("The transformer architecture revolutionized natural language processing. "
         "Self-attention allows models to process sequences in parallel. "
         "Modern LLMs build on this with billions of parameters.")

# ── Forward with compressed KV ──
def kalora_forward(input_ids, rank, heads_k, heads_v):
    with torch.no_grad():
        out=model(input_ids=input_ids, use_cache=True)
    dc=DynamicCache()
    for i in range(n_layers):
        k=out.past_key_values.layers[i].keys
        v=out.past_key_values.layers[i].values
        k_c,_=svd_compress(k,rank); v_c,_=svd_compress(v,rank)
        kr=k_c.reshape(-1,head_dim)+heads_k[i](k_c.reshape(-1,head_dim))
        vr=v_c.reshape(-1,head_dim)+heads_v[i](v_c.reshape(-1,head_dim))
        dc.update(kr.reshape(k.shape).to(v.dtype), vr.reshape(v.shape).to(v.dtype), i)
    out2=model(input_ids=input_ids, past_key_values=dc, labels=input_ids)
    return out2

# ── Per-rank test ──
results={}
for rank in RANKS:
    print(f"\n{'='*50}")
    print(f"RANK = {rank}")
    print(f"{'='*50}")
    
    # Train heads
    ids=tok(calib, return_tensors='pt', truncation=True, max_length=256)
    with torch.no_grad():
        out=model(**ids, use_cache=True)
    
    heads_k, heads_v=[],[]
    for i in range(n_layers):
        k=out.past_key_values.layers[i].keys
        v=out.past_key_values.layers[i].values
        k_c,cr=svd_compress(k,rank); v_c,_=svd_compress(v,rank)
        # Log CR for first layer
        if i==0: first_cr=cr
        
        rhk=RestoreHead(head_dim, 24).to(k.device)
        rhv=RestoreHead(head_dim, 24).to(v.device)
        optk=torch.optim.Adam(rhk.parameters(), lr=0.05); optv=torch.optim.Adam(rhv.parameters(), lr=0.05)
        kf=k_c.reshape(-1,head_dim).detach(); k_full=k.reshape(-1,head_dim)
        vf=v_c.reshape(-1,head_dim).detach(); v_full=v.reshape(-1,head_dim)
        for _ in range(40):
            optk.zero_grad(); F.mse_loss(kf+rhk(kf.float()),k_full.float()).backward(); optk.step()
            optv.zero_grad(); F.mse_loss(vf+rhv(vf.float()),v_full.float()).backward(); optv.step()
        heads_k.append(rhk); heads_v.append(rhv)
    
    # CR estimate (first layer)
    print(f"  CR: {first_cr:.1f}x (layer 0)")
    
    # PPL benchmark
    ppls=[]
    for idx, text in enumerate(texts):
        ids=tok(text, return_tensors='pt', truncation=True, max_length=MAX_LEN)
        
        with torch.no_grad():
            out_base=model(input_ids=ids['input_ids'], labels=ids['input_ids'])
            ppl_base=math.exp(min(out_base.loss.item(), 15))
        
        out_kal=kalora_forward(ids['input_ids'], rank, heads_k, heads_v)
        ppl_kal=math.exp(min(out_kal.loss.item(), 15))
        
        ratio=ppl_kal/ppl_base
        ppls.append((ppl_base, ppl_kal, ratio))
        
        if (idx+1)%10==0:
            avg_ratio=sum(r for _,_,r in ppls)/len(ppls)
            print(f"  [{idx+1}/{N_SAMPLES}] avg PPL ratio: {avg_ratio:.4f}")
    
    # Aggregate
    avg_base=sum(b for b,_,_ in ppls)/len(ppls)
    avg_kal=sum(k for _,k,_ in ppls)/len(ppls)
    avg_ratio=sum(r for _,_,r in ppls)/len(ppls)
    max_delta=max(r-1 for _,_,r in ppls)*100
    results[rank]=(first_cr, avg_base, avg_kal, avg_ratio, max_delta)
    
    verdict="✅ <5%" if avg_ratio<1.05 else ("⚠️ <10%" if avg_ratio<1.10 else "❌ >10%")
    print(f"  CR={first_cr:.1f}x | Base PPL={avg_base:.2f} | KALoRA PPL={avg_kal:.2f} | Ratio={avg_ratio:.4f}x | {verdict}")

# ── FINAL TABLE ──
print(f"\n{'='*60}")
print("KALoRA PPL BENCHMARK — FINAL RESULTS")
print(f"{'='*60}")
print(f"{'Rank':>5} | {'CR':>6} | {'Base PPL':>8} | {'KALoRA PPL':>10} | {'Ratio':>6} | {'Max Δ':>6} | {'Verdict'}")
print(f"{'-'*60}")
for rank in RANKS:
    cr, base, kal, ratio, md = results[rank]
    v="✅" if ratio<1.05 else ("⚠️" if ratio<1.10 else "❌")
    print(f"  r={rank:2d} | {cr:5.1f}x | {base:7.2f} | {kal:9.2f} | {ratio:5.3f}x | {md:5.1f}% | {v}")
print(f"{'='*60}")
print("Done!")
