"""KALoRA on Qwen2.5-0.5B — float32 forced"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

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
    def __init__(self, D=64, hidden=16):
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

print("="*55)
print("KALoRA — Qwen2.5-0.5B (float32)")

# Force float32
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-0.5B", torch_dtype=torch.float32).eval()
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")

config = model.config
head_dim = config.hidden_size // config.num_attention_heads
n_layers = config.num_hidden_layers
n_kv_heads = getattr(config, 'num_key_value_heads', config.num_attention_heads)
print(f"Model: {sum(p.numel() for p in model.parameters())/1e6:.1f}M")
print(f"Heads: {config.num_attention_heads}Q/{n_kv_heads}KV | Head dim: {head_dim} | Layers: {n_layers}")

prompt = ("Transformer architecture revolutionized NLP. Self-attention "
          "enables parallel processing of sequences. Modern LLMs use billions "
          "of parameters trained on large-scale data.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

with torch.no_grad():
    out = model(ids, use_cache=True)
    past = out.past_key_values
    
    # Get first layer KV
    if hasattr(past, 'key_cache'):
        full_k, full_v = past.key_cache[0].float(), past.value_cache[0].float()
    else:
        items = list(past)
        full_k, full_v = items[0][0].float(), items[0][1].float()
    print(f"KV: {full_k.shape} | dtype: {full_k.dtype}")

print(f"\n{'='*55}")
print("Results")
print(f"{'Rank':>5} | {'CR':>6} | {'MSE önce':>9} | {'MSE sonra':>9} | {'Gain':>5} | {'Params'}")
print(f"{'-'*55}")

results = []
for rank in [2, 4, 6, 8, 12, 16, 20]:
    hidden = 16 if rank <= 6 else 32
    
    with torch.no_grad():
        k_comp, cr, _ = compress_svd(full_k, rank)
        mse_base = F.mse_loss(k_comp, full_k).item()
    
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
        imp = max(0, (1-mse_final/mse_base))*100
    
    p = sum(p.numel() for p in rh.parameters())
    results.append((rank, cr, mse_base, mse_final, imp, p))
    sym = "✅" if imp > 5 else ("⬆️" if imp > 1 else "➖")
    print(f"  r={rank:2d} | {cr:.1f}x | {mse_base:.4f}  -> {mse_final:.4f} | {imp:4.1f}% | {p:5d} {sym}")

print(f"\n{'='*55}")
for r, cr, ms, mf, imp, p in results:
    if imp > 3:
        print(f"  ✅ r={r}: {cr:.1f}x, MSE={mf:.4f} ({imp:.1f}% gain), {p} params")
print(f"{'='*55}")
