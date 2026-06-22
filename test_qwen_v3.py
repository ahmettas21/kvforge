"""KALoRA on Qwen2.5-0.5B — normalized KV + proper restoration"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

def compress_svd_norm(k, rank):
    """SVD with normalization — handles different KV scales"""
    B,H,S,D = k.shape; r = min(rank,S,D)
    kf = k.reshape(-1,S,D)
    
    # Normalize per head
    mean = kf.mean(dim=(1,2), keepdim=True)
    std = kf.std(dim=(1,2), keepdim=True).clamp(min=1e-8)
    kfn = (kf - mean) / std
    
    U,s,Vh = torch.linalg.svd(kfn, full_matrices=False)
    Uk,sk,Vhk = U[:,:,:r], s[:,:r], Vh[:,:r,:]
    
    k_rn = (Uk*sk.unsqueeze(-2))@Vhk
    k_r = k_rn * std + mean  # denormalize
    k_r = k_r.reshape(B,H,S,D)
    
    cb = (Uk.numel()+sk.numel()+Vhk.numel())*2
    return k_r, k.numel()*2/cb if cb>0 else 1.0, r

class RestoreHead(nn.Module):
    def __init__(self, D=64, hidden=16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(D, hidden, bias=True), nn.ReLU(),
            nn.Linear(hidden, D, bias=True),
        )
        self.net[-1].weight.data.zero_()
        self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)

print("="*55)
print("KALoRA — Qwen2.5-0.5B (normalized SVD)")
device = 'cpu'

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-0.5B", torch_dtype=torch.float32).eval()
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")

config = model.config
head_dim = config.hidden_size // config.num_attention_heads
n_kv = getattr(config, 'num_key_value_heads', config.num_attention_heads)
print(f"Model: 494M | {config.num_attention_heads}Q/{n_kv}KV | head_dim={head_dim}")

prompt = ("Transformer architecture revolutionized NLP. Self-attention enables "
          "parallel processing. Modern LLMs use billions of parameters. "
          "This breakthrough has transformed artificial intelligence.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

with torch.no_grad():
    out = model(ids, use_cache=True)
    if hasattr(out.past_key_values, 'key_cache'):
        full_k = out.past_key_values.key_cache[0].float()
    else:
        full_k = list(out.past_key_values)[0][0].float()
    print(f"KV: {full_k.shape} range=[{full_k.min():.2f}, {full_k.max():.2f}]")

print(f"\n{'='*55}")
print("Results (normalized SVD + restoration)")
print(f"{'Rank':>5} | {'CR':>6} | NRMSE önce | NRMSE sonra | {'Gain':>5} | {'Params'}")
print(f"{'-'*55}")

results = []
for rank in [2, 4, 6, 8, 12, 16]:
    hidden = 32 if rank > 6 else 16
    
    k_comp, cr, _ = compress_svd_norm(full_k, rank)
    
    # Normalized RMSE (relative to KV range)
    k_range = full_k.max() - full_k.min()
    mse_base = F.mse_loss(k_comp, full_k).item()
    nrmse_base = (mse_base ** 0.5) / k_range if k_range > 0 else mse_base ** 0.5
    
    rh = RestoreHead(D=head_dim, hidden=hidden)
    opt = torch.optim.Adam(rh.parameters(), lr=0.05)
    
    for step in range(100):
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
        nrmse_final = (mse_final ** 0.5) / k_range if k_range > 0 else mse_final ** 0.5
        imp = max(0, (1-mse_final/mse_base))*100
    
    p = sum(p.numel() for p in rh.parameters())
    results.append((rank, cr, nrmse_base, nrmse_final, imp, p, mse_base, mse_final))
    sym = "✅" if imp > 5 else ("⬆️" if imp > 1 else "➖")
    print(f"  r={rank:2d} | {cr:.1f}x | {nrmse_base:.4f}  -> {nrmse_final:.4f} | {imp:4.1f}% | {p:5d} {sym}")

print(f"\n{'='*55}")
print("Summary (MSE values):")
for r, cr, _, _, imp, p, ms, mf in results:
    if imp > 2:
        print(f"  ✅ r={r}: {cr:.1f}x, MSE {ms:.4f}->{mf:.4f} ({imp:.1f}% gain)")
    else:
        print(f"     r={r}: {cr:.1f}x, MSE {ms:.4f}->{mf:.4f} ({imp:.1f}% gain)")
print(f"{'='*55}")
