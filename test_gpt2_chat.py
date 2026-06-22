"""KALoRA — GPT-2 canlı chat testi"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache
import time

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

print("="*55)
print("KALoRA — GPT-2 Canlı Chat Testi")
print("="*55)

model=AutoModelForCausalLM.from_pretrained("gpt2").eval()
tok=AutoTokenizer.from_pretrained("gpt2")
tok.pad_token=tok.eos_token
cfg=model.config
head_dim=cfg.hidden_size//cfg.num_attention_heads
n_layers=cfg.num_hidden_layers
print(f"  124M | heads={cfg.num_attention_heads} | head_dim={head_dim} | layers={n_layers}")

prompt="The future of artificial intelligence is"
ids=tok(prompt,return_tensors='pt')

# ── 1. NORMAL ──
print("\n[1/4] Normal inference...")
torch.manual_seed(42)
t0=time.time()
with torch.no_grad():
    out_n=model.generate(**ids, max_new_tokens=30, do_sample=True, temperature=0.8,
                          pad_token_id=tok.eos_token_id, use_cache=True)
normal=tok.decode(out_n[0], skip_special_tokens=True)
print(f"  \"{normal}\" | {time.time()-t0:.1f}s")

# ── 2. SADECE COMPRESS (restore yok) ──
print("\n[2/4] Sadece compress (restore yok)...")
with torch.no_grad():
    out=model(input_ids=ids['input_ids'], use_cache=True)
    compressed_past = DynamicCache()
    for i in range(n_layers):
        k,v=get_kv(out.past_key_values, i)
        k_c, cr = svd_compress(k, rank=4)
        compressed_past.update(k_c.half(), v.half(), i)
    print(f"  CR: {cr:.1f}x")

torch.manual_seed(42)
t0=time.time()
with torch.no_grad():
    out_c=model.generate(input_ids=ids['input_ids'], max_new_tokens=30, do_sample=True,
                          temperature=0.8, pad_token_id=tok.eos_token_id,
                          use_cache=True, past_key_values=compressed_past)
compress_only=tok.decode(out_c[0], skip_special_tokens=True)
print(f"  \"{compress_only}\" | {time.time()-t0:.1f}s")

# ── 3. KALoRA (compress + restore head eğit) ──
print("\n[3/4] KALoRA (compress + restore head training)...")
with torch.no_grad():
    out=model(input_ids=ids['input_ids'], use_cache=True)
    k0,v0=get_kv(out.past_key_values, 0)

with torch.no_grad():
    k_c, cr = svd_compress(k0, rank=4)
    mse_b = F.mse_loss(k_c, k0).item()

# Train restore head
rh=RestoreHead(D=head_dim, h=24)
opt=torch.optim.Adam(rh.parameters(), lr=0.05)
kf=k_c.reshape(-1,head_dim).detach(); k_full=k0.reshape(-1,head_dim)
for _ in range(100):
    opt.zero_grad(); loss=F.mse_loss(kf+rh(kf), k_full); loss.backward(); opt.step()

with torch.no_grad():
    mse_a=F.mse_loss(kf+rh(kf), k_full).item()
imp=max(0,(1-mse_a/mse_b))*100
print(f"  MSE: {mse_b:.4f}->{mse_a:.4f} ({imp:.1f}% gain) | CR: {cr:.1f}x | Params: {sum(p.numel() for p in rh.parameters())}")

# KALoRA generate
kalora_cache=DynamicCache()
with torch.no_grad():
    for i in range(n_layers):
        k,v=get_kv(out.past_key_values, i)
        k_c,_=svd_compress(k, rank=4)
        kr=k_c.reshape(-1,head_dim)+rh(k_c.reshape(-1,head_dim))
        kr=kr.reshape(k.shape)
        kalora_cache.update(kr.half(), v.half(), i)

torch.manual_seed(42)
t0=time.time()
with torch.no_grad():
    out_k=model.generate(input_ids=ids['input_ids'], max_new_tokens=30, do_sample=True,
                          temperature=0.8, pad_token_id=tok.eos_token_id,
                          use_cache=True, past_key_values=kalora_cache)
kalora=tok.decode(out_k[0], skip_special_tokens=True)
print(f"  \"{kalora}\" | {time.time()-t0:.1f}s")

# ── 4. DAHA UZUN RESTORE EĞİTİMİ ──
print("\n[4/4] KALoRA+ (200 step training)...")
rh2=RestoreHead(D=head_dim, h=32)
opt2=torch.optim.Adam(rh2.parameters(), lr=0.05)
for _ in range(200):
    opt2.zero_grad(); loss=F.mse_loss(kf+rh2(kf), k_full); loss.backward(); opt2.step()

with torch.no_grad():
    mse_a2=F.mse_loss(kf+rh2(kf), k_full).item()
imp2=max(0,(1-mse_a2/mse_b))*100
print(f"  MSE: {mse_b:.4f}->{mse_a2:.4f} ({imp2:.1f}% gain)")

kalora2_cache=DynamicCache()
with torch.no_grad():
    for i in range(n_layers):
        k,v=get_kv(out.past_key_values, i)
        k_c,_=svd_compress(k, rank=4)
        kr=k_c.reshape(-1,head_dim)+rh2(k_c.reshape(-1,head_dim))
        kalora2_cache.update(kr.half().reshape(k.shape), v.half(), i)

torch.manual_seed(42)
t0=time.time()
with torch.no_grad():
    out_k2=model.generate(input_ids=ids['input_ids'], max_new_tokens=30, do_sample=True,
                           temperature=0.8, pad_token_id=tok.eos_token_id,
                           use_cache=True, past_key_values=kalora2_cache)
kalora2=tok.decode(out_k2[0], skip_special_tokens=True)
print(f"  \"{kalora2}\" | {time.time()-t0:.1f}s")

# ── SONUÇ ──
print(f"\n{'='*55}")
print("KARŞILAŞTIRMA")
print(f"{'='*55}")
print(f"  ① Normal:     \"{normal}\"")
print(f"  ② Compress:   \"{compress_only}\"")
print(f"  ③ KALoRA:     \"{kalora}\" ({imp:.1f}% gain)")
print(f"  ④ KALoRA+:    \"{kalora2}\" ({imp2:.1f}% gain)")
print(f"  CR: {cr:.1f}x")
print(f"{'='*55}")
