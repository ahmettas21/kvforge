"""KALoRA v2 — Better restoration head + STAR-KV comparison"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_kv(past):
    if hasattr(past, 'key_cache'):
        return past.key_cache[0], past.value_cache[0]
    try:
        if isinstance(past, (tuple, list)):
            if len(past) > 0:
                item = past[0]
                if isinstance(item, (tuple, list)):
                    return item[0], item[1]
                return item, past[1] if len(past) > 1 else item
        if hasattr(past, 'to_tuple'):
            t = past.to_tuple()
            return t[0][0], t[0][1]
    except:
        pass
    items = list(past)
    if isinstance(items[0], (tuple, list)):
        return items[0][0], items[0][1]
    return items[0], items[1]

def star_kv_compress(k, energy=0.9):
    """Energy-threshold STAR-KV compression"""
    B,H,S,D = k.shape
    kf = k.reshape(-1, S, D)
    U, s, Vh = torch.linalg.svd(kf, full_matrices=False)
    s2 = s ** 2
    total = s2.sum(-1, keepdim=True)
    cum = s2.cumsum(-1)
    r = (cum < energy * total).sum(-1).clamp(min=1).max().item()
    r = min(r, S, D)
    Uk,Sk,Vhk = U[:,:,:r], s[:,:r], Vh[:,:r,:]
    Klr = (Uk * Sk.unsqueeze(-2)) @ Vhk
    Klr = Klr.reshape(B,H,S,D)
    cb = (Uk.numel()+Sk.numel()+Vhk.numel())*2
    ob = k.numel()*2
    return Klr, ob/cb if cb>0 else 1.0, r

def ultra_lr(k, rank=2):
    B,H,S,D = k.shape; r = min(rank,S,D)
    kf = k.reshape(-1,S,D)
    U,s,Vh = torch.linalg.svd(kf, full_matrices=False)
    Uk,Sk,Vhk = U[:,:,:r], s[:,:r], Vh[:,:r,:]
    Klr = (Uk*Sk.unsqueeze(-2))@Vhk
    Klr = Klr.reshape(B,H,S,D)
    cb = (Uk.numel()+Sk.numel()+Vhk.numel())*2
    return Klr, (k.numel())*2/cb if cb>0 else 1.0

class RestoreHead(nn.Module):
    """Larger restoration: D -> 32 -> D (helps with low-rank residual)"""
    def __init__(self, D=64):
        super().__init__()
        self.W1 = nn.Linear(D, 32, bias=False)
        self.W2 = nn.Linear(32, D, bias=False)
        self.bn = nn.BatchNorm1d(32)
    def forward(self, x):
        return self.W2(torch.relu(self.bn(self.W1(x))))

print("="*50)
print("KALoRA v2 — Better Restoration")
print("="*50)

base = AutoModelForCausalLM.from_pretrained('gpt2').eval()
tok = AutoTokenizer.from_pretrained('gpt2')
tok.pad_token = tok.eos_token

prompt = ("The transformer architecture revolutionized NLP. Self-attention "
          "enables parallel processing of entire sequences, capturing long-range "
          "dependencies. Modern LLMs use billions of parameters trained on "
          "internet-scale data. This breakthrough has transformed AI.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

with torch.no_grad():
    out = base(ids, use_cache=True)
    full_k, _ = get_kv(out.past_key_values)
    print(f"KV: {full_k.shape}")

# Compare methods
print("\n--- Compression Comparison ---")
with torch.no_grad():
    skv, cr_skv, r = star_kv_compress(full_k, 0.9)
    ulr, cr_ulr = ultra_lr(full_k, 2)
    print(f"  STAR-KV (e=0.9): rank={r}, CR={cr_skv:.1f}x, MSE={F.mse_loss(skv,full_k).item():.4f}")
    print(f"  Ultra LR (r=2):   CR={cr_ulr:.1f}x, MSE={F.mse_loss(ulr,full_k).item():.4f}")
    print(f"  Compress raw:     CR={full_k.numel()*2/2:.0f}x (no SVD)")

# Train restoration — try different ranks
for label, (k_lr, cr, rank) in [("STAR-KV (e=0.9)", (skv, cr_skv, r)),
                                  ("Ultra LR (r=2)", (ulr, cr_ulr, 2))]:
    if label.startswith("Ultra"):
        restore = RestoreHead()
    else:
        restore = RestoreHead()
    
    optim = torch.optim.Adam(restore.parameters(), lr=1e-1)
    mse0 = F.mse_loss(k_lr, full_k).item()
    
    for step in range(100):
        optim.zero_grad()
        kf_lr = k_lr.reshape(-1, 64).detach()
        out_r = restore(kf_lr)
        restored = kf_lr + out_r
        loss = F.mse_loss(restored, full_k.reshape(-1, 64).detach())
        loss.backward()
        optim.step()
    
    mse_f = F.mse_loss(
        k_lr.reshape(-1,64) + restore(k_lr.reshape(-1,64).detach()),
        full_k.reshape(-1,64)).item()
    imp = max(0, (1-mse_f/mse0))*100
    params = sum(p.numel() for p in restore.parameters())
    print(f"  {label}: MSE {mse0:.4f} -> {mse_f:.4f} ({imp:.1f}%) | params={params} | CR={cr:.1f}x")

# Adaptive: combine STAR-KV quality + Ultra LR compression
print("\n--- Hybrid: STAR-KV ranked SVD + Ultra LR aggressive ---")
with torch.no_grad():
    kf = full_k.reshape(-1, 32, 64)
    U,s,Vh = torch.linalg.svd(kf, full_matrices=False)  # (B*H) x S x D
    # Keep different ranks per mode
    hybrids = {}
    for target_r in [2, 3, 4, 6]:
        r = min(target_r, 32, 64)
        k_r = (U[:,:,:r] * s[:,:r].unsqueeze(-2)) @ Vh[:,:r,:]
        k_r = k_r.reshape(full_k.shape)
        ob = full_k.numel()*2
        cb = (U[:,:,:r].numel()+s[:,:r].numel()+Vh[:,:r,:].numel())*2
        cr = ob/cb if cb>0 else 1.0
        mse = F.mse_loss(k_r, full_k).item()
        hybrids[f"r={r}"] = (k_r, cr, mse)
        print(f"  rank={r:2d}: CR={cr:.1f}x, MSE={mse:.6f}")

print(f"\n{'='*50}")
print("Done! Best tradeoff:")
best_tradeoff = min([(abs(v[2]-0.1), k, v) for k,v in hybrids.items()])
print(f"  {best_tradeoff[1]}: CR={best_tradeoff[2][1]:.1f}x, MSE={best_tradeoff[2][2]:.6f}")

# Save results
torch.save(restore.state_dict(), 'kalora_head.pt')
print("Restoration head saved to kalora_head.pt")
