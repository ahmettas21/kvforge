"""KALoRA v3 — proper init + better restoration"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_kv(past):
    if hasattr(past, 'key_cache'): return past.key_cache[0], past.value_cache[0]
    try:
        if isinstance(past, (tuple, list)) and len(past) > 0:
            item = past[0]
            if isinstance(item, (tuple, list)): return item[0], item[1]
            return item, past[1] if len(past) > 1 else item
        if hasattr(past, 'to_tuple'):
            t = past.to_tuple(); return t[0][0], t[0][1]
    except: pass
    items = list(past)
    if isinstance(items[0], (tuple, list)): return items[0][0], items[0][1]
    return items[0], items[1]

def compress_svd(k, rank):
    """Direct SVD compression with given rank"""
    B,H,S,D = k.shape; r = min(rank,S,D)
    kf = k.reshape(-1,S,D)
    U,s,Vh = torch.linalg.svd(kf, full_matrices=False)
    k_r = (U[:,:,:r] * s[:,:r].unsqueeze(-2)) @ Vh[:,:r,:]
    k_r = k_r.reshape(B,H,S,D)
    cb = (U[:,:,:r].numel()+s[:,:r].numel()+Vh[:,:r,:].numel())*2
    return k_r, k.numel()*2/cb if cb>0 else 1.0, r

class RestoreHead(nn.Module):
    """Residual prediction: compressed_KV -> correction"""
    def __init__(self, D=64, hidden=16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(D, hidden, bias=True),
            nn.ReLU(),
            nn.Linear(hidden, D, bias=True),
        )
        # Initialize to near-zero output (start with no correction)
        self.net[-1].weight.data.zero_()
        self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)

print("="*55)
print("KALoRA v3 — Local Test")
print("="*55)

model = AutoModelForCausalLM.from_pretrained('gpt2').eval()
tok = AutoTokenizer.from_pretrained('gpt2')
tok.pad_token = tok.eos_token

prompt = ("The transformer architecture revolutionized NLP by introducing "
          "self-attention mechanisms that process entire sequences in parallel.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

with torch.no_grad():
    out = model(ids, use_cache=True)
    full_k, full_v = get_kv(out.past_key_values)
    print(f"KV: {full_k.shape}")

# Test ranks
best_mse = float('inf')
best_cr = 0
results = []

for rank in [1, 2, 3, 4, 6, 8]:
    with torch.no_grad():
        k_comp, cr, r_actual = compress_svd(full_k, rank)
        mse_base = F.mse_loss(k_comp, full_k).item()
    
    # Train restore head
    rh = RestoreHead(D=64, hidden=16 if rank <= 4 else 32)
    opt = torch.optim.Adam(rh.parameters(), lr=0.05)
    mse_start = mse_base
    
    for step in range(80):
        opt.zero_grad()
        # Predict residual
        pred = rh(k_comp.reshape(-1, 64))
        restored = k_comp.reshape(-1, 64) + pred
        loss = F.mse_loss(restored, full_k.reshape(-1, 64))
        loss.backward()
        opt.step()
    
    with torch.no_grad():
        pred = rh(k_comp.reshape(-1, 64))
        restored = k_comp.reshape(-1, 64) + pred
        mse_final = F.mse_loss(restored, full_k.reshape(-1, 64)).item()
        imp = max(0, (1-mse_final/mse_start))*100
    
    params = sum(p.numel() for p in rh.parameters())
    results.append((rank, cr, mse_start, mse_final, imp, params))
    
    sym = "✅" if imp > 5 else ("⬆️" if imp > 1 else "➖")
    print(f"  r={rank} | CR={cr:.1f}x | MSE: {mse_start:.4f}->{mse_final:.4f} ({imp:.1f}%) "
          f"| {params} params {sym}")
    
    if mse_final < best_mse:
        best_mse = mse_final
        best_cr = cr

# Summary
print(f"\n{'='*55}")
print("Best tradeoffs:")
for r, cr, ms, mf, imp, p in results:
    if imp > 3:
        print(f"  ✅ r={r}: {cr:.1f}x, MSE={mf:.4f} ({imp:.1f}% improvement), {p} params")
print(f"\n{'='*55}")
print("Done!")
