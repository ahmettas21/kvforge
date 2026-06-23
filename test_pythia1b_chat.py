"""KALoRA — Pythia-1B canlı chat testi"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache
import time

from kalora_inference import KALoRAWrapper, compress_kv, RestoreHead

def get_layer_kv(past, idx):
    if hasattr(past, 'key_cache'):
        return past.key_cache[idx].float(), past.value_cache[idx].float()
    if isinstance(past, (tuple, list)):
        if isinstance(past[0], (tuple, list)):
            return past[idx][0].float(), past[idx][1].float()
        return past[idx].float(), past[idx+1].float()
    items = list(past)
    if isinstance(items[0], (tuple, list)):
        return items[idx][0].float(), items[idx][1].float()
    return items[idx].float(), items[idx+1].float()

# RestoreHead'i tekrar tanımla (import edilmediyse)
class RestoreHead(nn.Module):
    def __init__(self, D=64, hidden=16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(D, hidden, bias=True), nn.ReLU(),
            nn.Linear(hidden, D, bias=True),
        )
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)
    def train_head(self, k_comp, full_k, steps=80, lr=0.05):
        opt = torch.optim.Adam(self.parameters(), lr=lr)
        for _ in range(steps):
            opt.zero_grad()
            loss = F.mse_loss(
                k_comp.reshape(-1, k_comp.shape[-1]) + self(k_comp.reshape(-1, k_comp.shape[-1])),
                full_k.reshape(-1, full_k.shape[-1]))
            loss.backward(); opt.step()

print("=" * 55)
print("KALoRA — Pythia-1B Canlı Chat Testi")
print("=" * 55)

# Modeli yükle
print("\nYükleniyor: Pythia-1B...")
t0 = time.time()
model = AutoModelForCausalLM.from_pretrained(
    "EleutherAI/pythia-1b", dtype=torch.float32).eval()
tok = AutoTokenizer.from_pretrained("EleutherAI/pythia-1b")
tok.pad_token = tok.eos_token
print(f"  {sum(p.numel() for p in model.parameters())/1e6:.1f}M params | {time.time()-t0:.1f}s")

# Model yapısı
config = model.config
head_dim = config.hidden_size // config.num_attention_heads
n_layers = config.num_hidden_layers
print(f"  Heads: {config.num_attention_heads} | head_dim={head_dim} | Layers: {n_layers}")

# Test prompt
prompt = "The future of artificial intelligence lies in"
print(f"\nPrompt: '{prompt}'")

# ── NORMAL INFERENCE ──
print("\n[1/4] Normal inference (KV cache without compression)...")
t0 = time.time()
with torch.no_grad():
    ids = tok(prompt, return_tensors='pt')
    out_normal = model.generate(
        **ids, max_new_tokens=30, do_sample=True, temperature=0.8,
        pad_token_id=tok.eos_token_id, use_cache=True)
normal_text = tok.decode(out_normal[0], skip_special_tokens=True)
print(f"  ✓ {time.time()-t0:.1f}s")
print(f"  Output: \"{normal_text}\"")

# ── KALoRA RESTORE HEAD EĞİT ──
print("\n[2/4] KALoRA restore head training (first layer)...")
with torch.no_grad():
    out = model(ids, use_cache=True)
    full_k, full_v = get_layer_kv(out.past_key_values, 0)

k_lr, cr, _ = compress_kv(full_k, full_v, rank=4)
print(f"  CR: {cr:.1f}x | MSE önce: {F.mse_loss(k_lr[0], full_k).item():.4f}")

rh = RestoreHead(D=head_dim, hidden=24)
rh.train_head(k_lr[0], full_k, steps=80)

with torch.no_grad():
    restored = k_lr[0].reshape(-1, head_dim) + rh(k_lr[0].reshape(-1, head_dim))
    mse_after = F.mse_loss(restored, full_k.reshape(-1, head_dim)).item()
    mse_before = F.mse_loss(k_lr[0], full_k).item()
    imp = max(0, (1-mse_after/mse_before))*100
print(f"  MSE: {mse_before:.4f} -> {mse_after:.4f} ({imp:.1f}% improvement)")

# ── KALoRA INFERENCE (compressed KV ile generate) ──
print("\n[3/4] KALoRA inference (compressed + restored KV)...")
t0 = time.time()
with torch.no_grad():
    # İlk forward
    out = model(ids, use_cache=True)
    
    # Tüm layerları compress + restore et
    compressed_past = []
    for i in range(n_layers):
        k, v = get_layer_kv(out.past_key_values, i)
        k_lr, v_lr, _, _ = compress_kv(k, v, rank=4)
        # Restore (trained head'ler olmadığı için direct)
        compressed_past.append((k_lr, v_lr))
    
    # compressed KV ile generate et
    out_kalora = model.generate(
        **ids, max_new_tokens=30, do_sample=True, temperature=0.8,
        pad_token_id=tok.eos_token_id, use_cache=True,
        past_key_values=compressed_past)
    
kalora_text = tok.decode(out_kalora[0], skip_special_tokens=True)
print(f"  ✓ {time.time()-t0:.1f}s")
print(f"  Output: \"{kalora_text}\"")

# ── KARŞILAŞTIRMA ──
print(f"\n{'='*55}")
print("SONUÇ KARŞILAŞTIRMASI")
print(f"{'='*55}")
print(f"  Normal:  \"{normal_text}\"")
print(f"  KALoRA:  \"{kalora_text}\"")
print(f"  Compression: {cr:.1f}x")
print(f"  Restoration gain: {imp:.1f}%")
print(f"{'='*55}")
print("Completed!")
