#!/usr/bin/env python3
"""
GPT-2 MiniKV KV Cache Compression PoC
======================================
Layer-discriminative quantization on GPT-2's KV cache.
Uses DynamicCache API (transformers >=5.9).
"""

import json, math, time
import torch, torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM, DynamicCache


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
        qc = DynamicCache()
        for li in range(self.n):
            k = cache.layers[li].keys
            v = cache.layers[li].values
            qk, _ = self.quantize(k, li)
            qv, _ = self.quantize(v, li)
            dk, dv = self.dequant(qk, li), self.dequant(qv, li)
            qc.update(dk.to(k.dtype), dv.to(v.dtype), k.size(2))
        return qc

    def ratio(self, cache: DynamicCache):
        orig = sum(
            cache.layers[li].keys.numel() * cache.layers[li].keys.element_size() +
            cache.layers[li].values.numel() * cache.layers[li].values.element_size()
            for li in range(self.n)
        )
        q_total = 0
        for li in range(self.n):
            k = cache.layers[li].keys
            v = cache.layers[li].values
            b = self.bc[li]
            if b >= 16:
                q_total += k.numel()*k.element_size() + v.numel()*v.element_size()
            else:
                q_total += k.numel() + v.numel()
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
    print(f"({time.time()-t0:.1f}s) {nl}L {cfg.n_embd}D  {model.num_parameters():,}p")

    texts = [
        "The transformer architecture revolutionized natural language processing by introducing "
        "self-attention mechanisms that capture long-range dependencies in text. These models "
        "process sequences in parallel making training much more efficient than recurrent "
        "neural networks. Later advances like GPT BERT and T5 showed that scaling up these "
        "architectures leads to remarkable improvements across many language tasks.",
        "Large language models face a critical bottleneck during text generation: the key-value "
        "cache grows linearly with sequence length. For billion-parameter models serving "
        "thousands of concurrent users this memory cost becomes substantial. Techniques like "
        "quantization pruning and sparse attention have been developed to address this challenge.",
    ]

    encoded = []
    for t in texts:
        ids = tok(t, return_tensors="pt", truncation=True, max_length=196).input_ids
        if ids.size(1) > 64:
            encoded.append(ids)
    if not encoded:
        print("No valid samples"); return
    print(f"  Samples: {len(encoded)} ({[ids.size(1) for ids in encoded]})")

    # Reference PPL
    print("  Ref PPL...", end=" ", flush=True)
    refs = [ppl(model, ids.to(dev)) for ids in encoded]
    avg_ref = sum(refs) / len(refs)
    print(f"{avg_ref:.4f}")

    tests = [
        ("Uniform 8-bit",       [8] * nl),
        ("Uniform 4-bit",       [4] * nl),
        ("Uniform 2-bit",       [2] * nl),
        ("Layer 8×6 + 4×6",     [8] * (nl//2) + [4] * (nl - nl//2)),
        ("Layer 8×4+4×4+2×4",   [8]*4 + [4]*4 + [2]*4),
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

            out = model(pref, use_cache=True, past_key_values=None)
            cache = out.past_key_values

            # MSE on first continuation token
            qcache = qz.apply(cache)
            out_ref = model(rest[:, :1], use_cache=True, past_key_values=cache)
            out_q   = model(rest[:, :1], use_cache=True, past_key_values=qcache)
            mse = F.mse_loss(out_q.logits, out_ref.logits).item()

            # Continue with requantization — collect logits for all steps
            pk = qcache
            all_logits = []
            all_labels = []
            for i in range(rest.size(1)):
                out = model(rest[:, i:i+1], use_cache=True, past_key_values=pk)
                all_logits.append(out.logits[:, 0, :])  # last (only) token
                if i < rest.size(1) - 1:
                    all_labels.append(rest[:, i+1])
                pk = qz.apply(out.past_key_values)

            # PPL with quantized cache: loss = cross_entropy over generated tokens
            if len(all_labels) > 0:
                logits_stacked = torch.stack(all_logits[:-1], dim=1)  # [1, T-1, V]
                labels_stacked = torch.stack(all_labels, dim=1)      # [1, T-1]
                loss = F.cross_entropy(
                    logits_stacked.reshape(-1, logits_stacked.size(-1)),
                    labels_stacked.reshape(-1),
                    reduction="mean"
                )
                ppl_val = math.exp(loss.item())
            else:
                ppl_val = avg_ref

            ratio, orig_mb, comp_mb = qz.ratio(cache)
            s_res.append({"ppl": ppl_val, "mse": mse, "ratio": ratio, "comp_mb": comp_mb})

        avg_ppl = sum(s["ppl"] for s in s_res) / len(s_res)
        avg_mse = sum(s["mse"] for s in s_res) / len(s_res)
        avg_ratio = sum(s["ratio"] for s in s_res) / len(s_res)
        avg_mb = sum(s["comp_mb"] for s in s_res) / len(s_res)
        print(f"  {'':<28} {avg_ppl:<10.4f} {avg_ppl-avg_ref:<+10.4f} {avg_ratio:<10.2f}x {avg_mse:<12.6e}  {avg_mb:.4f}MB")
        results["tests"].append({"name": name, "ppl": avg_ppl, "delta": avg_ppl-avg_ref, "ratio": avg_ratio, "mse": avg_mse, "comp_mb": avg_mb})

    # Summary
    print("\n" + "=" * 65)
    print("  RESULTS")
    print("=" * 65 + "\n")
    print(f"  Reference avg PPL: {avg_ref:.4f}\n")
    print(f"  {'Method':<28} {'PPL':<10} {'Δ':<8} {'Ratio':<10} {'MSE':<15}")
    print(f"  {'-'*28} {'-'*10} {'-'*8} {'-'*10} {'-'*15}")
    for t in results["tests"]:
        print(f"  {t['name']:<28} {t['ppl']:<10.4f} {t['delta']:<+8.4f} {t['ratio']:<10.2f}x {t['mse']:<15.6e}")

    with open("gpt2_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  → gpt2_results.json ✅")


if __name__ == "__main__":
    main()
