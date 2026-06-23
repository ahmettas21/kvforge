"""KALoRA on Qwen2.5-0.5B — real test"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

def get_kv(past, idx=0):
    if hasattr(past, 'key_cache'): return past.key_cache[idx], past.value_cache[idx]
    items = list(past)
    if isinstance(items[0], (tuple, list)): return items[idx][0], items[idx][1]
    return items[idx], items[idx+1] if idx+1 < len(items) else items[idx]

def compress_svd(k, rank):
    B,H,S,D = k.shape; r = min(rank,S,D)
    kf = k.reshape(-1,S,D)
    U,s,Vh = torch.linalg.svd(kf, full_matrices=False)
    Uk,sk,Vhk = U[:,:,:r], s[:,:r], Vh[:,:r,:]
    k_r = (Uk*sk.unsqueeze(-2))@Vhk
    k_r = k_r.reshape(B,H,S,D)
    cb = (Uk.numel()+sk.numel()+Vhk.numel())*2
    return k_r, k.numel()*2/cb if cb>0 else 1.0, r

class RestoreHead(nn.Module):
    def __init__(self, D=128, hidden=16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(D, hidden, bias=True),
            nn.ReLU(),
            nn.Linear(hidden, D, bias=True),
        )
        self.net[-1].weight.data.zero_()
        self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)

print("=" * 55)
print("KALoRA — Qwen2.5-0.5B Test")
print("=" * 55)

# Load Qwen
print("\nLoading Qwen2.5-0.5B...")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B").eval()
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
print(f"Params: {sum(p.numel() for p in model.parameters())/1e6:.1f}M")

# Model yapısını incele
config = model.config
print(f"Config: {config.hidden_size=}, {config.num_attention_heads=}, {config.num_hidden_layers=}")

# head_dim hesapla
head_dim = config.hidden_size // config.num_attention_heads
print(f"head_dim: {head_dim}")

prompt = ("Transformer architecture revolutionized NLP by introducing "
          "self-attention. Models process sequences in parallel, capturing "
          "long-range dependencies efficiently.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

with torch.no_grad():
    out = model(ids, use_cache=True)
    past = out.past_key_values
    
    # İlk layer'ı al
    if hasattr(past, 'key_cache'):
        full_k, full_v = past.key_cache[0], past.value_cache[0]
    else:
        full_k, full_v = get_kv(past, 0)
    
    print(f"KV shape: {full_k.shape}")
    print(f"Heads: {full_k.shape[1]}, Head dim: {full_k.shape[3]}")

# Test ranks
print(f"\n{'='*55}")
print("Compression + Restoration Results")
print(f"{'='*55}")
print(f"  {'Rank':>5} | {'CR':>6} | {'MSE önce':>9} | {'MSE sonra':>9} | {'Gain':>5} | {'Params'}")
print(f"  {'-'*55}")

results = []
for rank in [2, 4, 6, 8, 12, 16]:
    with torch.no_grad():
        k_comp, cr, r_actual = compress_svd(full_k.float(), rank)
        mse_base = F.mse_loss(k_comp, full_k.float()).item()
    
    # Restore head — hidden larger for bigger head_dim
    hidden = 24 if rank <= 6 else 32
    rh = RestoreHead(D=head_dim, hidden=hidden)
    opt = torch.optim.Adam(rh.parameters(), lr=0.05)
    
    for _ in range(80):
        opt.zero_grad()
        pred = rh(k_comp.reshape(-1, head_dim))
        restored = k_comp.reshape(-1, head_dim) + pred
        loss = F.mse_loss(restored, full_k.reshape(-1, head_dim))
        loss.backward()
        opt.step()
    
    with torch.no_grad():
        pred = rh(k_comp.reshape(-1, head_dim))
        restored = k_comp.reshape(-1, head_dim) + pred
        mse_final = F.mse_loss(restored, full_k.reshape(-1, head_dim)).item()
        imp = max(0, (1-mse_final/mse_base))*100
    
    p = sum(p.numel() for p in rh.parameters())
    results.append((rank, cr, mse_base, mse_final, imp, p))
    
    sym = "✅" if imp > 5 else ("⬆️" if imp > 1 else "➖")
    print(f"  r={rank:3d} | {cr:.1f}x | {mse_base:.4f}  -> {mse_final:.4f} | {imp:4.1f}% | {p:5d} {sym}")

# Summary
print(f"\n{'='*55}")
print("Best tradeoffs:")
for r, cr, ms, mf, imp, p in results:
    if imp > 3:
        print(f"  ✅ r={r}: {cr:.1f}x, MSE={mf:.4f} ({imp:.1f}% improvement), {p} params")
print(f"{'='*55}")
print("Done!")
