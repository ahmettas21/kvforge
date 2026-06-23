import os; os.environ["CUDA_VISIBLE_DEVICES"]=""
# KALoRA v2 — GELU + Cross-Head Sharing Benchmark
# Compares: Linear vs ReLU vs GELU restoration heads
# Then: Cross-Head sharing (GQA optimized)
import os, math, warnings, json, time
warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer, DynamicCache

MODEL = "Qwen/Qwen2.5-1.5B"
N_SAMPLES = 20
MAX_LEN = 128

print(f"Model: {MODEL} | Samples: {N_SAMPLES}")
device = 'cpu'
print(f"Device: {device}")

# ── 3 Restoration Head Variants ──
class LinearHead(nn.Module):
    """Pure linear: ΔK̂ = W_B W_A · K_r (rank ≤ h)"""
    def __init__(self, D, h):
        super().__init__()
        self.W_A = nn.Linear(D, h, bias=False)
        self.W_B = nn.Linear(h, D, bias=True)
        self.W_B.weight.data.zero_(); self.W_B.bias.data.zero_()
    def forward(self, x):
        return self.W_B(self.W_A(x))

class ReLUHead(nn.Module):
    """Current baseline: ReLU activation"""
    def __init__(self, D, h):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(D, h), nn.ReLU(), nn.Linear(h, D))
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)

class GELUHead(nn.Module):
    """Proposed: GELU activation (smoother gradient, better approx)"""
    def __init__(self, D, h):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(D, h), nn.GELU(), nn.Linear(h, D))
        self.net[-1].weight.data.zero_(); self.net[-1].bias.data.zero_()
    def forward(self, x):
        return self.net(x)

HEAD_CLASSES = {
    "Linear": LinearHead,
    "ReLU": ReLUHead,
    "GELU": GELUHead
}

def svd_compress(k, rank):
    B,H,S,D=k.shape; r=min(rank,S,D); kf=k.float().reshape(-1,S,D)
    U,s,Vh=torch.linalg.svd(kf, full_matrices=False)
    Uk,sk,Vhk=U[:,:,:r],s[:,:r],Vh[:,:r,:]
    kr=(Uk*sk.unsqueeze(-2))@Vhk; kr=kr.reshape(B,H,S,D)
    cb=(Uk.numel()+sk.numel()+Vhk.numel())*2
    ob=k.numel()*2
    return kr, ob/cb if cb>0 else 1.0

# ── Load model ──
print("\nLoading model...")
t0=time.time()
model=AutoModelForCausalLM.from_pretrained(MODEL).eval()
tok=AutoTokenizer.from_pretrained(MODEL); tok.pad_token=tok.eos_token
cfg=model.config
D=cfg.hidden_size//cfg.num_attention_heads
n_layers=cfg.num_hidden_layers
n_kv_heads=getattr(cfg, 'num_key_value_heads', cfg.num_attention_heads)
print(f"  {sum(p.numel() for p in model.parameters())/1e6:.1f}M | {D=} | {n_layers=} | {n_kv_heads=} | {time.time()-t0:.1f}s")

# ── Dataset ──
print("Loading WikiText-2...")
from datasets import load_dataset
ds=load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
texts=[t['text'] for t in ds if len(t['text'].strip())>50][:N_SAMPLES]
print(f"  {len(texts)} samples")

# ── Calibration ──
calib = ("The transformer architecture revolutionized natural language processing. "
         "Self-attention allows models to process sequences in parallel. "
         "Modern LLMs build on this with billions of parameters.")
ids_calib = tok(calib, return_tensors='pt', truncation=True, max_length=256).to(device)

# ── Train heads for a rank ──
def train_heads(rank, head_cls, h=16):
    with torch.no_grad():
        out = model(**ids_calib, use_cache=True)
    heads_k, heads_v = [], []
    first_cr = 0
    for i in range(n_layers):
        k = out.past_key_values.layers[i].keys
        v = out.past_key_values.layers[i].values
        k_c, cr = svd_compress(k, rank); v_c, _ = svd_compress(v, rank)
        if i == 0: first_cr = cr
        rhk = head_cls(D, h).to(device)
        rhv = head_cls(D, h).to(device)
        optk = torch.optim.Adam(rhk.parameters(), lr=0.05)
        optv = torch.optim.Adam(rhv.parameters(), lr=0.05)
        kf = k_c.reshape(-1, D).detach(); k_full = k.reshape(-1, D)
        vf = v_c.reshape(-1, D).detach(); v_full = v.reshape(-1, D)
        for _ in range(25):
            optk.zero_grad()
            F.mse_loss(kf + rhk(kf.float()), k_full.float()).backward()
            optk.step()
            optv.zero_grad()
            F.mse_loss(vf + rhv(vf.float()), v_full.float()).backward()
            optv.step()
        heads_k.append(rhk); heads_v.append(rhv)
    return heads_k, heads_v, first_cr

# ── Train cross-head shared heads ──
def train_cross_heads(rank, head_cls, h=16):
    """GQA-optimized: share restore heads across KV heads (only 2)"""
    with torch.no_grad():
        out = model(**ids_calib, use_cache=True)
    # Shared restore heads: one per KV head group
    shared_heads_k = nn.ModuleList([head_cls(D, h) for _ in range(n_kv_heads)]).to(device)
    shared_heads_v = nn.ModuleList([head_cls(D, h) for _ in range(n_kv_heads)]).to(device)
    first_cr = 0
    for i in range(n_layers):
        k = out.past_key_values.layers[i].keys
        v = out.past_key_values.layers[i].values
        k_c, cr = svd_compress(k, rank); v_c, _ = svd_compress(v, rank)
        if i == 0: first_cr = cr
        # Which KV head? In GQA, each layer's KV has n_kv_heads
        # But the cache stores all heads. We process all heads at once.
        # For cross-head: all KV heads share the same 2 base heads
        B_, H_, S_, D_ = k.shape
        # kv_head_idx = head_idx % n_kv_heads  # not needed; we use shared heads directly
        # Training: just train the shared heads on all KV data
        kf = k_c.reshape(-1, D).detach()
        k_full = k.reshape(-1, D)
        vf = v_c.reshape(-1, D).detach()
        v_full = v.reshape(-1, D)
        for hk, hv in zip(shared_heads_k, shared_heads_v):
            optk = torch.optim.Adam(hk.parameters(), lr=0.05)
            optv = torch.optim.Adam(hv.parameters(), lr=0.05)
            for _ in range(25):
                optk.zero_grad()
                F.mse_loss(kf + hk(kf.float()), k_full.float()).backward()
                optk.step()
                optv.zero_grad()
                F.mse_loss(vf + hv(vf.float()), v_full.float()).backward()
                optv.step()
    return shared_heads_k, shared_heads_v, first_cr

# ── Forward with compressed KV ──
def kalora_forward(input_ids, rank, heads_k, heads_v):
    with torch.no_grad():
        out = model(input_ids=input_ids, use_cache=True)
    dc = DynamicCache()
    for i in range(n_layers):
        k = out.past_key_values.layers[i].keys
        v = out.past_key_values.layers[i].values
        k_c, _ = svd_compress(k, rank); v_c, _ = svd_compress(v, rank)
        kr = k_c.reshape(-1, D) + heads_k[i](k_c.reshape(-1, D).float())
        vr = v_c.reshape(-1, D) + heads_v[i](v_c.reshape(-1, D).float())
        dc.update(kr.reshape(k.shape).to(v.dtype), vr.reshape(v.shape).to(v.dtype), i)
    out2 = model(input_ids=input_ids, past_key_values=dc, labels=input_ids)
    return out2

def kalora_cross_forward(input_ids, rank, heads_k, heads_v):
    """Cross-head version: heads_k/v are ModuleList of n_kv_heads"""
    with torch.no_grad():
        out = model(input_ids=input_ids, use_cache=True)
    dc = DynamicCache()
    for i in range(n_layers):
        k = out.past_key_values.layers[i].keys
        v = out.past_key_values.layers[i].values
        B_, H_, S_, D_ = k.shape
        k_c, _ = svd_compress(k, rank); v_c, _ = svd_compress(v, rank)
        # For each head, apply corresponding shared head
        # n_kv_heads is small (2 for Qwen), heads map cyclically
        kr_parts = []
        for h_idx in range(H_):
            hk = heads_k[h_idx % n_kv_heads]
            k_head = k_c[:, h_idx:h_idx+1, :, :]
            kr_h = k_head.reshape(-1, D) + hk(k_head.reshape(-1, D).float())
            kr_parts.append(kr_h.reshape(B_, 1, S_, D_))
        kr = torch.cat(kr_parts, dim=1)
        vr_parts = []
        for h_idx in range(H_):
            hv = heads_v[h_idx % n_kv_heads]
            v_head = v_c[:, h_idx:h_idx+1, :, :]
            vr_h = v_head.reshape(-1, D) + hv(v_head.reshape(-1, D).float())
            vr_parts.append(vr_h.reshape(B_, 1, S_, D_))
        vr = torch.cat(vr_parts, dim=1)
        dc.update(kr.to(v.dtype), vr.to(v.dtype), i)
    out2 = model(input_ids=input_ids, past_key_values=dc, labels=input_ids)
    return out2

# ── Compute PPL ──
def compute_ppl(forward_fn, *args):
    ppls = []
    for text in texts:
        ids = tok(text, return_tensors='pt', truncation=True, max_length=MAX_LEN).to(device)
        with torch.no_grad():
            out_base = model(input_ids=ids['input_ids'], labels=ids['input_ids'])
            ppl_base = math.exp(min(out_base.loss.item(), 15))
        out_kal = forward_fn(ids['input_ids'], *args)
        ppl_kal = math.exp(min(out_kal.loss.item(), 15))
        ppls.append((ppl_base, ppl_kal, ppl_kal / ppl_base))
    avg_base = sum(b for b, _, _ in ppls) / len(ppls)
    avg_kal = sum(k for _, k, _ in ppls) / len(ppls)
    avg_ratio = sum(r for _, _, r in ppls) / len(ppls)
    return avg_base, avg_kal, avg_ratio

# ═══════════════════════════════════════════
# BENCHMARK
# ═══════════════════════════════════════════
RANK = 4
H = 24

print(f"\n{'='*60}")
print(f"KALoRA v2 BENCHMARK — Rank={RANK}, h={H}")
print(f"{'='*60}")

# 1. Baseline PPL
print("\n[1/5] Computing baseline PPL...")
base_ppls = []
for text in texts:
    ids = tok(text, return_tensors='pt', truncation=True, max_length=MAX_LEN).to(device)
    with torch.no_grad():
        out = model(input_ids=ids['input_ids'], labels=ids['input_ids'])
        base_ppls.append(math.exp(min(out.loss.item(), 15)))
BASELINE_PPL = sum(base_ppls) / len(base_ppls)
print(f"  Baseline PPL: {BASELINE_PPL:.2f}")

results = {"model": MODEL, "rank": RANK, "h": H, "baseline_ppl": round(BASELINE_PPL, 2)}

# 2. Test each head type
for name, head_cls in HEAD_CLASSES.items():
    print(f"\n[{name}] Training heads...")
    t0 = time.time()
    heads_k, heads_v, cr = train_heads(RANK, head_cls, h=H)
    train_t = time.time() - t0
    print(f"  CR: {cr:.1f}x | Train: {train_t:.1f}s")
    
    # Per-layer gain (calibration set)
    print(f"  Per-layer gain (train set):")
    gains = []
    with torch.no_grad():
        out = model(**ids_calib, use_cache=True)
    for i in range(n_layers):
        k = out.past_key_values.layers[i].keys
        v = out.past_key_values.layers[i].values
        k_c, _ = svd_compress(k, RANK)
        v_c, _ = svd_compress(v, RANK)
        kr = k_c + heads_k[i](k_c.reshape(-1, D).float()).reshape(k.shape)
        vr = v_c + heads_v[i](v_c.reshape(-1, D).float()).reshape(v.shape)
        mse_before = F.mse_loss(k_c, k).item()
        mse_after = F.mse_loss(kr, k).item()
        gain = max(0, (1 - mse_after / max(mse_before, 1e-10))) * 100
        gains.append(gain)
    avg_gain = sum(gains) / len(gains)
    print(f"  avg restoration gain: {avg_gain:.1f}%")
    
    t0 = time.time()
    avg_base, avg_kal, avg_ratio = compute_ppl(kalora_forward, RANK, heads_k, heads_v)
    ppl_t = time.time() - t0
    print(f"  Base: {avg_base:.2f} | KALoRA: {avg_kal:.2f} | Ratio: {avg_ratio:.4f}x | Time: {ppl_t:.1f}s")
    
    results[name] = {
        "cr": round(cr, 1),
        "gain_avg": round(avg_gain, 1),
        "ppl_base": round(avg_base, 2),
        "ppl_kalora": round(avg_kal, 2),
        "ratio": round(avg_ratio, 4)
    }

# 3. Cross-Head Sharing (GELU)
print(f"\n[CrossHead] Training GELU shared heads ({n_kv_heads} KV heads)...")
t0 = time.time()
shared_k, shared_v, cr = train_cross_heads(RANK, GELUHead, h=H)
train_t = time.time() - t0
print(f"  CR: {cr:.1f}x | Train: {train_t:.1f}s | Params: {sum(p.numel() for p in shared_k.parameters()) + sum(p.numel() for p in shared_v.parameters())}")

t0 = time.time()
avg_base, avg_kal, avg_ratio = compute_ppl(kalora_cross_forward, RANK, shared_k, shared_v)
ppl_t = time.time() - t0
print(f"  Base: {avg_base:.2f} | KALoRA: {avg_kal:.2f} | Ratio: {avg_ratio:.4f}x | Time: {ppl_t:.1f}s")

results["CrossHead-GELU"] = {
    "cr": round(cr, 1),
    "n_kv_heads": n_kv_heads,
    "params": sum(p.numel() for p in shared_k.parameters()) + sum(p.numel() for p in shared_v.parameters()),
    "ppl_base": round(avg_base, 2),
    "ppl_kalora": round(avg_kal, 2),
    "ratio": round(avg_ratio, 4)
}

# ── FINAL TABLE ──
print(f"\n{'='*60}")
print("KALoRA v2 — FINAL RESULTS")
print(f"{'='*60}")
print(f"{'Head Type':>15} | {'CR':>5} | {'Gain':>5} | {'Base PPL':>8} | {'KALoRA':>8} | {'Ratio':>6} | {'Params':>8}")
print(f"{'-'*60}")
for name in list(HEAD_CLASSES.keys()) + ["CrossHead-GELU"]:
    r = results.get(name, {})
    cr = r.get('cr', 0.0)
    g = r.get('gain_avg', 0.0)
    bp = r.get('ppl_base', 0.0)
    kp = r.get('ppl_kalora', 0.0)
    rat = r.get('ratio', 0.0)
    # Count params
    if name == "CrossHead-GELU":
        pcount = r.get('params', 0)
    else:
        pcount = 2 * n_layers * (2 * D * H + H)  # 2 heads × 28 layers × linear params
    v = "✅" if rat < 1.05 else ("⚠️" if rat < 1.10 else "❌")
    print(f"  {name:>13} | {cr:4.1f}x | {g:4.1f}% | {bp:7.2f} | {kp:7.2f} | {rat:5.3f}x | {pcount:>6,} | {v}")

print(f"\nBaseline PPL: {BASELINE_PPL:.2f}")
print(f"{'='*60}")
print("Done!")

# Save results
with open('kalora_v2_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Results saved to kalora_v2_results.json")
