#!/usr/bin/env python3
"""
Kaggle — GPT-2 MiniKV KV Cache Compression PoC
================================================
GPU'da çalışır. Sadece Run All yapman yeterli.
"""

import json, math, time
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM, DynamicCache

# ── 1. Test texts ───────────────────────────────────────────
TEXTS = [
    "The transformer architecture revolutionized natural language processing by introducing "
    "self-attention mechanisms that capture long-range dependencies in text. These models "
    "process sequences in parallel making training much more efficient than recurrent "
    "neural networks. Later advances like GPT BERT and T5 showed that scaling up these "
    "architectures leads to remarkable improvements across many language tasks. The key "
    "innovation was the self-attention mechanism which computes weighted representations "
    "of all positions in the input sequence allowing the model to understand context.",
    "Large language models face a critical bottleneck during text generation: the key-value "
    "cache grows linearly with sequence length. For billion-parameter models serving "
    "thousands of concurrent users this memory cost becomes substantial. Techniques like "
    "quantization pruning and sparse attention have been developed to address this challenge. "
    "The most promising approaches include KV cache quantization which reduces memory "
    "footprint with minimal quality loss and attention pruning which removes redundant heads.",
    "Knowledge distillation is a technique where a smaller student model learns to mimic "
    "the behavior of a larger teacher model. This allows deploying lightweight models that "
    "retain much of the performance of their larger counterparts. Recent work has shown "
    "that combining distillation with quantization can produce extremely efficient models "
    "suitable for edge devices and real-time applications.",
]

# ── 2. Quantizer ────────────────────────────────────────────
class Quantizer:
    def __init__(self, n_layers, bc):
        self.n = n_layers
        self.bc = bc if len(bc) == n_layers else bc + [4] * (n_layers - len(bc))
        self.state = [None] * n_layers

    def quantize(self, t, li):
        b = self.bc[li]
        if b >= 16:
            self.state[li] = {"bits": 16}
            return t, 1.0
        mn = t.min(-1, True).values
        mx = t.max(-1, True).values
        s = (mx - mn).clamp(1e-8) / (2**b - 1)
        zp = mn
        q = ((t - zp) / s).round().clamp(0, 2**b - 1).to(torch.uint8)
        self.state[li] = {"s": s, "zp": zp, "bits": b}
        return q, q.numel() / (t.numel() * 2)

    def dequant(self, q, li):
        st = self.state[li]
        return q if st["bits"] >= 16 else q.float() * st["s"] + st["zp"]

    def apply(self, cache: DynamicCache):
        qc = DynamicCache()
        for li in range(self.n):
            k = cache.key_cache[li]; v = cache.value_cache[li]
            qk, _ = self.quantize(k, li)
            qv, _ = self.quantize(v, li)
            dk = self.dequant(qk, li).to(k.dtype)
            dv = self.dequant(qv, li).to(v.dtype)
            qc.update(dk, dv, k.size(2))
        return qc

    def ratio(self, cache: DynamicCache):
        orig = sum(cache.key_cache[li].numel() * cache.key_cache[li].element_size() +
                   cache.value_cache[li].numel() * cache.value_cache[li].element_size()
                   for li in range(self.n))
        q_total = 0
        for li in range(self.n):
            b = self.bc[li]
            if b >= 16:
                k, v = cache.key_cache[li], cache.value_cache[li]
                q_total += k.numel()*k.element_size() + v.numel()*v.element_size()
            else:
                q_total += cache.key_cache[li].numel() + cache.value_cache[li].numel()
        return orig / q_total, orig / (1024**2), q_total / (1024**2)

# ── 3. Main ──────────────────────────────────────────────────
@torch.no_grad()
def main():
    print("=" * 65)
    print("  GPT-2 MiniKV KV Cache Compression PoC (GPU)")
    print("=" * 65)

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\n  Device: {dev}")
    if dev == "cuda":
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  Memory: {torch.cuda.get_device_properties(0).total_mem / 1e9:.1f} GB")

    print("\n  Loading GPT-2...", end=" ", flush=True)
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained("gpt2")
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained("gpt2").to(dev).eval()
    cfg = model.config
    nl = cfg.n_layer
    print(f"({time.time()-t0:.1f}s)  {nl}L {cfg.n_embd}D  {model.num_parameters():,}p")

    # Tokenize
    encoded = []
    for t in TEXTS:
        ids = tok(t, return_tensors="pt", truncation=True, max_length=256).input_ids
        if ids.size(1) > 64:
            encoded.append(ids)
    print(f"  Samples: {len(encoded)} ({[ids.size(1) for ids in encoded]})")

    # Reference PPL
    print("\n  Reference PPL...", end=" ", flush=True)
    refs = []
    for ids in encoded:
        logits = model(ids.to(dev)).logits
        sl = logits[..., :-1, :].reshape(-1, logits.size(-1))
        lb = ids[..., 1:].to(dev).reshape(-1)
        refs.append(math.exp(F.cross_entropy(sl, lb, reduction="mean").item()))
    avg_ref = sum(refs) / len(refs)
    print(f"{avg_ref:.4f}")

    # Test configs
    tests = [
        ("Uniform 8-bit",       [8] * nl),
        ("Uniform 4-bit",       [4] * nl),
        ("Uniform 2-bit",       [2] * nl),
        ("Layer 8×6 + 4×6",     [8] * (nl//2) + [4] * (nl - nl//2)),
        ("Layer 8×4+4×4+2×4",   [8]*4 + [4]*4 + [2]*4),
        ("Layer 8×8 + 4×4",     [8]*8 + [4]*(nl-8)),
    ]

    print(f"\n  {'Method':<28} {'PPL':<10} {'ΔPPL':<10} {'Ratio':<10} {'MSE':<12} {'MB':<8}")
    print(f"  {'-'*28} {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*8}")

    results = {"ref_ppl": avg_ref, "tests": []}

    for name, bc in tests:
        qz = Quantizer(nl, bc)
        unique = sorted(set(bc))
        print(f"\n  [{name}]  bits={unique}", flush=True)

        s_res = []
        for ids in encoded:
            ids = ids.to(dev)
            pf = min(64, ids.size(1)//2)
            pref, rest = ids[:, :pf], ids[:, pf:]

            # Prefill
            out = model(pref, use_cache=True, past_key_values=None)
            cache = out.past_key_values

            # MSE on prefill cache
            qcache = qz.apply(cache)
            out_ref = model(rest[:, :1], use_cache=True, past_key_values=cache)
            out_q   = model(rest[:, :1], use_cache=True, past_key_values=qcache)
            mse = F.mse_loss(out_q.logits, out_ref.logits).item()

            # Continue with quantization
            pk = qcache
            for i in range(rest.size(1)):
                out = model(rest[:, i:i+1], use_cache=True, past_key_values=pk)
                pk = qz.apply(out.past_key_values)

            # PPL on full seq with quantized cache
            full = torch.cat([pref, rest], dim=-1)
            logits = model(full).logits
            sl = logits[..., :-1, :].reshape(-1, logits.size(-1))
            lb = full[..., 1:].reshape(-1)
            ppl_val = math.exp(F.cross_entropy(sl, lb, reduction="mean").item())

            ratio, orig_mb, comp_mb = qz.ratio(cache)
            s_res.append({"ppl": ppl_val, "mse": mse, "ratio": ratio, "orig_mb": orig_mb, "comp_mb": comp_mb})

        avg_ppl = sum(s["ppl"] for s in s_res) / len(s_res)
        avg_mse = sum(s["mse"] for s in s_res) / len(s_res)
        avg_ratio = sum(s["ratio"] for s in s_res) / len(s_res)
        avg_mb = sum(s["comp_mb"] for s in s_res) / len(s_res)
        print(f"  {'':<28} {avg_ppl:<10.4f} {avg_ppl-avg_ref:<+10.4f} {avg_ratio:<10.2f}x {avg_mse:<12.6e} {avg_mb:<8.4f}")
        results["tests"].append({"name": name, "ppl": avg_ppl, "delta": avg_ppl-avg_ref, "ratio": avg_ratio, "mse": avg_mse, "comp_mb": avg_mb})

    # Summary
    print("\n" + "=" * 80)
    print("  RESULTS SUMMARY")
    print("=" * 80 + "\n")
    print(f"  Reference PPL: {avg_ref:.4f}  |  Model: GPT-2 ({nl}L {cfg.n_embd}D)\n")
    h = f"  {'Method':<28} {'PPL':<10} {'Δ':<8} {'Ratio':<10} {'MSE':<15} {'MB':<8}"
    print(h)
    print(f"  {'-'*28} {'-'*10} {'-'*8} {'-'*10} {'-'*15} {'-'*8}")
    for t in results["tests"]:
        print(f"  {t['name']:<28} {t['ppl']:<10.4f} {t['delta']:<+8.4f} {t['ratio']:<10.2f}x {t['mse']:<15.6e} {t['comp_mb']:<8.4f}")

    with open("gpt2_results_kaggle.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  → gpt2_results_kaggle.json")

    # Extra: GPU memory usage
    if dev == "cuda":
        print(f"\n  GPU Memory: {torch.cuda.max_memory_allocated() / 1e9:.2f} GB peak")

    print(f"\n{'='*80}")
    print("  ✅ Done!")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
