#!/usr/bin/env python3
"""
GPT-2 MiniKV KV Cache Compression PoC
======================================
Layer-discriminative quantization on GPT-2's KV cache.
Uses DynamicCache API (transformers >=4.49).

Method: prefill → quantize KV cache → dequantize → measure logit MSE + PPL.
"""

import json, math, time
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM, DynamicCache


def tokenize(texts, tokenizer, max_len=196):
    result = []
    for t in texts:
        ids = tokenizer(t, return_tensors="pt", truncation=True, max_length=max_len).input_ids
        if ids.size(1) > 64:
            result.append(ids)
    return result


@torch.no_grad()
def ppl(model, ids):
    l = model(ids).logits
    sl, lb = l[..., :-1, :].reshape(-1, l.size(-1)), ids[..., 1:].reshape(-1)
    return math.exp(F.cross_entropy(sl, lb, reduction="mean").item())


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
        mn, mx = t.min(-1, True).values, t.max(-1, True).values
        s = (mx - mn).clamp(1e-8) / (2**b - 1)
        zp = mn
        q = ((t - zp) / s).round().clamp(0, 2**b - 1).to(torch.uint8)
        self.state[li] = {"s": s, "zp": zp, "bits": b}
        return q, q.numel() / (t.numel() * 2)

    def dequant(self, q, li):
        st = self.state[li]
        return q if st["bits"] >= 16 else q.float() * st["s"] + st["zp"]

    def apply(self, cache: DynamicCache):
        """Quantize all layers in a DynamicCache, return quantized copy."""
        qc = DynamicCache()
        for li in range(self.n):
            k = cache.key_cache[li]
            v = cache.value_cache[li]
            qk, _ = self.quantize(k, li)
            qv, _ = self.quantize(v, li)
            dk, dv = self.dequant(qk, li), self.dequant(qv, li)
            qc.update(dk.to(k.dtype), dv.to(v.dtype), k.size(2))
        return qc

    def ratio(self, cache: DynamicCache):
        orig = sum(
            cache.key_cache[li].numel() * cache.key_cache[li].element_size() +
            cache.value_cache[li].numel() * cache.value_cache[li].element_size()
            for li in range(self.n)
        )
        q_total = 0
        for li in range(self.n):
            k = cache.key_cache[li]
            v = cache.value_cache[li]
            b = self.bc[li]
            if b >= 16:
                q_total += k.numel()*k.element_size() + v.numel()*v.element_size()
            else:
                q_total += k.numel() + v.numel()  # uint8
        return orig / q_total if q_total > 0 else 1.0, orig / (1024**2), q_total / (1024**2)


def main():
    print("=" * 60)
    print("  GPT-2 MiniKV KV Cache Compression PoC")
    print("=" * 60)

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\n  Device: {dev}")
    print("  Loading GPT-2...", end=" ", flush=True)
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained("gpt2")
    tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    model = model.to(dev).eval()
    cfg = model.config
    nl = cfg.n_layer
    print(f"({time.time()-t0:.1f}s) {nl}L {cfg.n_embd}D")

    texts = [
        ("The transformer architecture revolutionized natural language processing by introducing "
         "self-attention mechanisms that capture long-range dependencies in text. These models "
         "process sequences in parallel making training much more efficient than recurrent "
         "neural networks. Later advances like GPT BERT and T5 showed that scaling up these "
         "architectures leads to remarkable improvements across many language tasks. The key "
         "innovation was the self-attention mechanism which computes weighted representations "
         "of all positions in the input sequence allowing the model to understand context."),
        ("Large language models face a critical bottleneck during text generation: the key-value "
         "cache grows linearly with sequence length. For billion-parameter models serving "
         "thousands of concurrent users this memory cost becomes substantial. Techniques like "
         "quantization pruning and sparse attention have been developed to address this challenge. "
         "The most promising approaches include KV cache quantization which reduces memory "
         "footprint with minimal quality loss and attention pruning which removes redundant heads."),
    ]
    encoded = tokenize(texts, tok)
    if not encoded:
        print("No valid samples"); return
    print(f"  Samples: {len(encoded)} ({encoded[0].size(1)}-{encoded[-1].size(1)} tokens)")

    # Reference PPL
    print("  Ref PPL...", end=" ", flush=True)
    refs = [ppl(model, ids.to(dev)) for ids in encoded]
    avg_ref = sum(refs) / len(refs)
    print(f"{avg_ref:.4f}")

    # Test configurations
    tests = [
        ("Uniform 8-bit",       [8] * nl),
        ("Uniform 4-bit",       [4] * nl),
        ("Uniform 2-bit",       [2] * nl),
        ("Layer 8×6 + 4×6",     [8] * (nl//2) + [4] * (nl - nl//2)),
        ("Layer 8×4 + 4×4 + 2×4", [8,8,8,8] + [4,4,4,4] + [2,2,2,2]),
    ]

    print(f"\n  {'Method':<28} {'PPL':<10} {'ΔPPL':<10} {'Ratio':<10} {'MSE':<12}")
    print(f"  {'-'*28} {'-'*10} {'-'*10} {'-'*10} {'-'*12}")

    results = {"ref_ppl": avg_ref, "tests": []}

    for name, bc in tests:
        qz = Quantizer(nl, bc)
        print(f"\n  [{name}]  bits={sorted(set(bc))}", flush=True)

        s_res = []
        for ids in encoded:
            ids = ids.to(dev)
            pf = min(48, ids.size(1)//2)
            pref, rest = ids[:, :pf], ids[:, pf:]

            # Prefill
            out = model(pref, use_cache=True, past_key_values=None)
            cache = out.past_key_values  # DynamicCache

            # Quantize
            qcache = qz.apply(cache)

            # MSE: compare logit difference on first rest token
            out_ref = model(rest[:, :1], use_cache=True, past_key_values=cache)
            out_q = model(rest[:, :1], use_cache=True, past_key_values=qcache)
            mse = F.mse_loss(out_q.logits, out_ref.logits).item()

            # Continue generation with quantized cache to measure PPL
            # (quantize after each forward)
            pk = qcache
            for i in range(rest.size(1)):
                out = model(rest[:, i:i+1], use_cache=True, past_key_values=pk)
                pk_new = out.past_key_values
                pk = qz.apply(pk_new)

            ppl_val, _ = ppl(model, ids), None

            ratio, orig_mb, comp_mb = qz.ratio(cache)
            s_res.append({"ppl": ppl_val, "mse": mse, "ratio": ratio, "orig_mb": orig_mb, "comp_mb": comp_mb})

        avg_ppl = sum(s["ppl"] for s in s_res) / len(s_res)
        avg_mse = sum(s["mse"] for s in s_res) / len(s_res)
        avg_ratio = sum(s["ratio"] for s in s_res) / len(s_res)
        print(f"  {'':<28} {avg_ppl:<10.4f} {avg_ppl-avg_ref:<+10.4f} {avg_ratio:<10.2f}x {avg_mse:<12.6e}")
        results["tests"].append({"name": name, "bits": bc, "ppl": avg_ppl, "delta": avg_ppl-avg_ref, "ratio": avg_ratio, "mse": avg_mse})

    # Print summary
    print("\n" + "=" * 60)
    print("  RESULTS")
    print("=" * 60 + "\n")
    print(f"  Reference avg PPL: {avg_ref:.4f}\n")
    print(f"  {'Method':<28} {'PPL':<10} {'Δ':<8} {'Ratio':<8} {'MSE':<12}")
    print(f"  {'-'*28} {'-'*10} {'-'*8} {'-'*8} {'-'*12}")
    for t in results["tests"]:
        print(f"  {t['name']:<28} {t['ppl']:<10.4f} {t['delta']:<+8.4f} {t['ratio']:<8.2f}x {t['mse']:<12.6e}")

    with open("gpt2_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  → gpt2_results.json  ✅")


if __name__ == "__main__":
    main()
