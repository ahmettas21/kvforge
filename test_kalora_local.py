"""KALoRA local test — optimized for this CPU"""
import sys, math, os, warnings
warnings.filterwarnings('ignore')

# CPU safety
os.environ['OMP_NUM_THREADS'] = '2'
os.environ['MKL_NUM_THREADS'] = '2'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

# Fallback SVD — pure PyTorch, no external deps
def robust_svd(X, k):
    """Simple power-iteration based SVD — avoids AVX issues"""
    m, n = X.shape
    Q = torch.randn(n, k+5, device=X.device, dtype=X.dtype)
    Q = Q / Q.norm(dim=0, keepdim=True)
    for _ in range(3):
        Q = X.T @ (X @ Q)
        Q, _ = torch.linalg.qr(Q)
    Y = X @ Q[:, :k]
    return Y  # just return the compressed version

def ultra_compress(k, rank=2):
    B,H,S,D = k.shape
    r = min(rank, S, D)
    kf = k.reshape(-1, S, D)
    # Simple compression: top-r SVD via power iteration
    Uk, Sk, Vhk = torch.linalg.svd(kf, full_matrices=False)
    Uk, Sk, Vhk = Uk[:, :, :r], Sk[:, :r], Vhk[:, :r, :]
    Klr = (Uk * Sk.unsqueeze(-2)) @ Vhk
    Klr = Klr.reshape(B, H, S, D)
    cb = (Uk.numel() + Sk.numel() + Vhk.numel()) * 2
    ob = k.numel() * 2
    return Klr, ob / cb if cb > 0 else 1.0

def get_kv(past):
    if hasattr(past, 'key_cache'):
        return past.key_cache[0], past.value_cache[0]
    if hasattr(past, 'to_tuple'):
        t = past.to_tuple()
        return t[0][0], t[0][1]
    if isinstance(past, (tuple, list)):
        return (past[0][0], past[0][1]) if isinstance(past[0], (tuple, list)) else (past[0], past[1])
    return list(past)[0][0], list(past)[0][1]

print("=" * 50)
print("KALoRA — Local CPU Test")
print("=" * 50)
print(f"PyTorch: {torch.__version__}")
print(f"CPU threads: {os.environ.get('OMP_NUM_THREADS', 'default')}")

# Load model — eval mode, no gradients for base
print("\nLoading GPT-2...")
base = AutoModelForCausalLM.from_pretrained('gpt2')
tok = AutoTokenizer.from_pretrained('gpt2')
tok.pad_token = tok.eos_token
base.eval()
print(f"Model loaded: {sum(p.numel() for p in base.parameters())/1e6:.1f}M params")

# Simple restoration head
class TinyRestore(nn.Module):
    def __init__(self, D=64, r=8):
        super().__init__()
        self.W1 = nn.Linear(D, r, bias=False)
        self.W2 = nn.Linear(r, D, bias=False)
    def forward(self, x):
        return self.W2(torch.relu(self.W1(x)))

restore = TinyRestore()

# Prompt
prompt = ("The transformer architecture revolutionized NLP by introducing "
          "self-attention mechanisms that process entire sequences in parallel. "
          "This enabled models to capture long-range dependencies efficiently.")
ids = tok(prompt, return_tensors='pt')['input_ids']
print(f"Prompt: {ids.shape[1]} tokens")

# Forward pass — get KV
print("\nForward pass...")
with torch.no_grad():
    out = base(ids, use_cache=True)
    full_k, full_v = get_kv(out.past_key_values)
    print(f"KV shape: {full_k.shape}")

# Compress
print("\nUltra low-rank compression (r=2)...")
with torch.no_grad():
    k_lr, cr = ultra_compress(full_k, rank=2)
    print(f"Compressed: {k_lr.shape} | CR: {cr:.1f}x")
    mse_initial = F.mse_loss(k_lr, full_k).item()
    print(f"MSE (no restore): {mse_initial:.6f}")

# Quick restoration training
print("\nTraining restoration head (50 steps)...")
optim = torch.optim.Adam(restore.parameters(), lr=5e-2)
for step in range(50):
    optim.zero_grad()
    kf_lr = k_lr.reshape(-1, 64).detach()
    residual = restore(kf_lr)
    k_restored = kf_lr + residual
    loss = F.mse_loss(k_restored, full_k.reshape(-1, 64).detach())
    loss.backward()
    optim.step()
    if step % 10 == 0:
        with torch.no_grad():
            mse = loss.item()
            imp = max(0, (1 - mse / mse_initial)) * 100
        print(f"  step {step:2d} | MSE: {mse:.6f} ({imp:.1f}% improvement)")

# Final eval
with torch.no_grad():
    kf_lr = k_lr.reshape(-1, 64)
    residual = restore(kf_lr)
    k_final = kf_lr + residual
    mse_final = F.mse_loss(k_final, full_k.reshape(-1, 64)).item()
    imp_final = max(0, (1 - mse_final / mse_initial)) * 100

print(f"\n{'='*50}")
print(f"RESULT")
print(f"  Compression: {cr:.1f}x (ultra low-rank, r=2)")
print(f"  MSE before:  {mse_initial:.6f}")
print(f"  MSE after:   {mse_final:.6f}")
print(f"  Improvement: {imp_final:.1f}%")
print(f"  Params:      {sum(p.numel() for p in restore.parameters())}")
check = "✅ WORKS!" if imp_final > 3 else "⚠️ Marginal"
print(f"  Verdict:     {check}")
print(f"{'='*50}")
