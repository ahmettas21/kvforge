"""KALoRA — Pythia-70m canlı chat testi (1B için de aynı kod)"""
import os; os.environ['OMP_NUM_THREADS'] = '2'; os.environ['MKL_NUM_THREADS'] = '2'
import warnings; warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
import time, math

class RestoreHead(nn.Module):
    def __init__(self, D=64, hidden=16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(D, hidden, bias=True), nn.ReLU(),
            nn.Linear(hidden, D, bias=True))
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x): return self.net(x)

def compress_kv_simple(k, rank=4):
    B,H,S,D = k.shape; r = min(rank,S,D)
    kf = k.reshape(-1,S,D)
    U,s,Vh = torch.linalg.svd(kf, full_matrices=False)
    Uk,sk,Vhk = U[:,:,:r], s[:,:r], Vh[:,:r,:]
    k_r = (Uk*sk.unsqueeze(-2))@Vhk; k_r = k_r.reshape(B,H,S,D)
    cb = (Uk.numel()+sk.numel()+Vhk.numel())*2
    return k_r, k.numel()*2/cb if cb>0 else 1.0

print("="*55)
print("KALoRA — Canlı Chat Testi")
print("="*55)

# Model
print("\nYükleniyor: Pythia-70m...")
t0 = time.time()
model = AutoModelForCausalLM.from_pretrained("EleutherAI/pythia-70m").eval()
tok = AutoTokenizer.from_pretrained("EleutherAI/pythia-70m")
tok.pad_token = tok.eos_token
print(f"  {sum(p.numel() for p in model.parameters())/1e6:.1f}M params | {time.time()-t0:.1f}s")

config = model.config
head_dim = config.hidden_size // config.num_attention_heads
n_layers = config.num_hidden_layers
print(f"  Heads: {config.num_attention_heads} | head_dim={head_dim} | Layers: {n_layers}")

prompt = "The future of AI is"
print(f"\nPrompt: '{prompt}'")

# ── NORMAL ──
print("\n[1/3] Normal inference...")
t0 = time.time()
ids = tok(prompt, return_tensors='pt')
torch.manual_seed(42)
with torch.no_grad():
    out = model.generate(**ids, max_new_tokens=20, do_sample=True, temperature=0.8,
                         pad_token_id=tok.eos_token_id, use_cache=True)
normal = tok.decode(out[0], skip_special_tokens=True)
print(f"  Çıktı: \"{normal}\" | {time.time()-t0:.1f}s")

# ── COMPRESS + RESTORE ──
print("\n[2/3] KALoRA: compress + restore edip generate...")
# İlk forward (no_grad)
with torch.no_grad():
    out = model(input_ids=ids['input_ids'], use_cache=True)

# Her layer'ı compress et ve restoration head eğit
restored_past = []
for i in range(n_layers):
        if hasattr(out.past_key_values, 'key_cache'):
            k = out.past_key_values.key_cache[i].float()
            v = out.past_key_values.value_cache[i].float()
        elif isinstance(out.past_key_values, (tuple, list)):
            kv_item = list(out.past_key_values)[i]
            if isinstance(kv_item, (tuple, list)):
                k, v = kv_item[0].float(), kv_item[1].float()
            else:
                k = kv_item.float()
                v = list(out.past_key_values)[i+1].float()
        else:
            k, v = out.past_key_values[i][0].float(), out.past_key_values[i][1].float()
        
        # Compress
        k_c, cr = compress_kv_simple(k, rank=4)
        
        # Restore head eğit (ilk layer'da)
        if i == 0:
            rh = RestoreHead(D=head_dim, hidden=16)
            opt = torch.optim.Adam(rh.parameters(), lr=0.05)
            kf = k_c.reshape(-1, head_dim)
            k_full = k.reshape(-1, head_dim)
            for _ in range(50):
                opt.zero_grad()
                loss = F.mse_loss(kf + rh(kf), k_full)
                loss.backward(); opt.step()
            with torch.no_grad():
                mse_b = F.mse_loss(k_c, k).item()
                mse_a = F.mse_loss(kf + rh(kf), k_full).item()
            print(f"   Layer {i}: MSE {mse_b:.4f}->{mse_a:.4f} ({max(0,(1-mse_a/mse_b)*100):.1f}% gain) | CR={cr:.1f}x")
        
        # Restore
        restored = k_c.reshape(-1, head_dim) + rh(k_c.reshape(-1, head_dim))
        restored_past.append((restored.reshape(k.shape).half(), v.half()))  # half for efficiency

# KALoRA generate
t0 = time.time()
torch.manual_seed(42)
with torch.no_grad():
    out_k = model.generate(**ids, max_new_tokens=20, do_sample=True, temperature=0.8,
                           pad_token_id=tok.eos_token_id, use_cache=True,
                           past_key_values=restored_past)
kalora = tok.decode(out_k[0], skip_special_tokens=True)
print(f"  Çıktı: \"{kalora}\" | {time.time()-t0:.1f}s")

# ── KARŞILAŞTIR ──
print(f"\n{'='*55}")
print("KARŞILAŞTIRMA")
print(f"{'='*55}")
print(f"  Normal: \"{normal}\"")
print(f"  KALoRA: \"{kalora}\"")
print(f"  CR: ~{cr:.1f}x")
print(f"{'='*55}")
print("✅ Aynı modelde compression ile inference çalıştı!")
