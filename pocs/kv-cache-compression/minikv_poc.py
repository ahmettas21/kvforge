#!/usr/bin/env python3
"""
MiniKV-style KV Cache Compression PoC
======================================
2-bit layer-discriminative quantization for Transformer KV caches.
Measures compression ratio vs reconstruction accuracy (MSE).

Reference: MiniKV — 2-bit layer-discriminative, training-free KV cache
           compression with >98.5% recovery.
"""

import json
import math
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


# ── Tiny Transformer ──────────────────────────────────────────

@dataclass
class TinyConfig:
    vocab_size: int = 50257
    hidden_size: int = 256
    num_hidden_layers: int = 4
    num_attention_heads: int = 4
    intermediate_size: int = 512
    max_position_embeddings: int = 512


class RotaryEmbedding(nn.Module):
    def __init__(self, dim, max_len=512):
        super().__init__()
        inv_freq = 1.0 / (10000 ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer("inv_freq", inv_freq)
        pos = torch.arange(max_len).float()
        sincos = torch.einsum("i,j->ij", pos, inv_freq)
        self.register_buffer("sin", sincos.sin()[None, None, :, :])
        self.register_buffer("cos", sincos.cos()[None, None, :, :])

    def forward(self, x, offset=0):
        S = x.size(2)
        sin = self.sin[:, :, offset:offset+S, :].repeat_interleave(2, dim=-1)
        cos = self.cos[:, :, offset:offset+S, :].repeat_interleave(2, dim=-1)
        return sin.to(x.dtype), cos.to(x.dtype)


def apply_rotary(x, sin, cos):
    half = x.shape[-1] // 2
    return x * cos + torch.cat([-x[..., half:], x[..., :half]], dim=-1) * sin


class Attention(nn.Module):
    def __init__(self, cfg: TinyConfig):
        super().__init__()
        self.head_dim = cfg.hidden_size // cfg.num_attention_heads
        self.q_proj = nn.Linear(cfg.hidden_size, cfg.hidden_size, bias=False)
        self.k_proj = nn.Linear(cfg.hidden_size, cfg.hidden_size, bias=False)
        self.v_proj = nn.Linear(cfg.hidden_size, cfg.hidden_size, bias=False)
        self.o_proj = nn.Linear(cfg.hidden_size, cfg.hidden_size, bias=False)
        self.rotary = RotaryEmbedding(self.head_dim, cfg.max_position_embeddings)
        self.num_heads = cfg.num_attention_heads

    def forward(self, h, past_kv=None, use_cache=False):
        B, S, D = h.shape
        H = self.num_heads
        hd = self.head_dim

        q = self.q_proj(h).view(B, S, H, hd).transpose(1, 2)
        k = self.k_proj(h).view(B, S, H, hd).transpose(1, 2)
        v = self.v_proj(h).view(B, S, H, hd).transpose(1, 2)

        offset = 0 if past_kv is None else past_kv[0].size(2)
        sin, cos = self.rotary(q, offset)
        q, k = apply_rotary(q, sin, cos), apply_rotary(k, sin, cos)

        if past_kv is not None:
            k = torch.cat([past_kv[0], k], dim=2)
            v = torch.cat([past_kv[1], v], dim=2)

        T = k.size(2)
        # causal mask: each query (dim 2) attends to kv positions ≤ its own
        mask = torch.full((S, T), float("-inf"), device=q.device, dtype=q.dtype)
        mask = torch.triu(mask, diagonal=T - S + 1)

        a = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(hd) + mask.unsqueeze(0).unsqueeze(0)
        a = F.softmax(a, dim=-1).to(q.dtype)
        o = torch.matmul(a, v).transpose(1, 2).reshape(B, -1, D)
        o = self.o_proj(o)
        return o, (k, v) if use_cache else None


class MLP(nn.Module):
    def __init__(self, cfg: TinyConfig):
        super().__init__()
        self.gate = nn.Linear(cfg.hidden_size, cfg.intermediate_size, bias=False)
        self.up = nn.Linear(cfg.hidden_size, cfg.intermediate_size, bias=False)
        self.down = nn.Linear(cfg.intermediate_size, cfg.hidden_size, bias=False)

    def forward(self, x):
        return self.down(F.silu(self.gate(x)) * self.up(x))


class Block(nn.Module):
    def __init__(self, cfg: TinyConfig, i: int):
        super().__init__()
        self.attn = Attention(cfg)
        self.mlp = MLP(cfg)
        self.ln1 = nn.LayerNorm(cfg.hidden_size)
        self.ln2 = nn.LayerNorm(cfg.hidden_size)

    def forward(self, h, past_kv=None, use_cache=False):
        a, pkv = self.attn(self.ln1(h), past_kv, use_cache)
        h = h + a
        h = h + self.mlp(self.ln2(h))
        return h, pkv


class TinyTransformer(nn.Module):
    def __init__(self, cfg: TinyConfig):
        super().__init__()
        self.embed = nn.Embedding(cfg.vocab_size, cfg.hidden_size)
        self.blocks = nn.ModuleList([Block(cfg, i) for i in range(cfg.num_hidden_layers)])
        self.ln = nn.LayerNorm(cfg.hidden_size)
        self.head = nn.Linear(cfg.hidden_size, cfg.vocab_size, bias=False)
        self.head.weight = self.embed.weight  # tie

    def forward(self, ids, past_key_values=None, use_cache=False):
        h = self.embed(ids)
        new_past = [] if use_cache else None
        for i, blk in enumerate(self.blocks):
            pkv = past_key_values[i] if past_key_values is not None else None
            h, p = blk(h, pkv, use_cache)
            if use_cache:
                new_past.append(p)
        h = self.ln(h)
        logits = self.head(h)
        return logits, new_past if use_cache else None


# ── KVCache Quantizer (MiniKV-style) ──────────────────────────

class KVCacheQuantizer:
    def __init__(self, num_layers: int, bit_config: Optional[list] = None):
        self.num_layers = num_layers
        self.bit_config = bit_config or [8] * num_layers
        self.state = [None] * num_layers

    def set_bit_config(self, bit_config: list):
        self.bit_config = bit_config
        self.state = [None] * self.num_layers

    def quantize(self, t: torch.Tensor, li: int):
        bits = self.bit_config[li]
        if bits >= 16:
            self.state[li] = {"bits": 16}
            return t, self.state[li]
        mn = t.min(dim=-1, keepdim=True).values
        mx = t.max(dim=-1, keepdim=True).values
        s = (mx - mn).clamp(min=1e-8) / (2**bits - 1)
        zp = mn
        q = ((t - zp) / s).round().clamp(0, 2**bits - 1).to(torch.uint8)
        self.state[li] = {"scale": s, "zp": zp, "bits": bits}
        return q, self.state[li]

    def dequantize(self, q, li):
        st = self.state[li]
        if st["bits"] >= 16:
            return q
        return q.float() * st["scale"] + st["zp"]

    def compress(self, k, v, li):
        qk, _ = self.quantize(k, li)
        qv, _ = self.quantize(v, li)
        return qk, qv

    def decompress(self, qk, qv, li):
        dk = self.dequantize(qk, li)
        dv = self.dequantize(qv, li)
        return dk, dv

    def ratio(self, li):
        b = self.bit_config[li]
        return 16.0 / b if b < 16 else 1.0


# ── Helpers ────────────────────────────────────────────────────

def gendata(b=1, seq=128, vs=50257):
    return torch.randint(0, min(vs, 10000), (b, seq))


def run_prefill(model, ids):
    with torch.no_grad():
        _, past = model(ids, use_cache=True)
    return past


def run_token(model, tok, past):
    with torch.no_grad():
        l, np = model(tok, past_key_values=past, use_cache=True)
    return l, np


def run_gen(model, ids, past):
    """Run generation tokens and return final (logits, past)."""
    p = past[:]
    for i in range(ids.size(1)):
        _, p = run_token(model, ids[:, i:i+1], p)
    return p


@torch.no_grad()
def compute_mse(model, ids, ref_past, test_past):
    """MSE between logits from reference and test KV caches."""
    lr, _ = model(ids, past_key_values=ref_past, use_cache=True)
    lt, _ = model(ids, past_key_values=test_past, use_cache=True)
    return F.mse_loss(lt, lr).item()


def cache_bytes(past_kv):
    return sum(k.numel() * k.element_size() + v.numel() * v.element_size()
               for k, v in past_kv)


def cache_bytes_compressed(compressed):
    return sum(qk.numel() * qk.element_size() + qv.numel() * qv.element_size()
               for qk, qv in compressed)


# ── Tests ──────────────────────────────────────────────────────

@dataclass
class TestResult:
    name: str
    bit_config: list
    cache_mb: float
    ratio: float
    mse: float
    done: bool = False


def run_test(model, prefill_ids, gen_ids, quantizer, bit_config, name, ref_past=None):
    n = len(bit_config)
    quantizer.set_bit_config(bit_config)

    past = run_prefill(model, prefill_ids)
    compressed = [quantizer.compress(k, v, i) for i, (k, v) in enumerate(past)]
    decompressed = [quantizer.decompress(qk, qv, i) for i, (qk, qv) in enumerate(compressed)]

    cb = cache_bytes_compressed(compressed)
    rb = cache_bytes(past)

    # Compute MSE on post-generation cache (accumulates errors)
    gen_past = run_gen(model, gen_ids, decompressed)
    ref_p = run_gen(model, gen_ids, past)

    mse = compute_mse(model, gen_ids[:, 0:1], ref_p, gen_past)

    return TestResult(
        name=name,
        bit_config=bit_config,
        cache_mb=cb / (1024**2),
        ratio=rb / cb,
        mse=mse,
        done=True,
    )


# ── Main ───────────────────────────────────────────────────────

def main():
    print("=" * 68)
    print("  MiniKV-style KV Cache Compression PoC")
    print("=" * 68)

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"\n  Device: {dev}  |  PyTorch {torch.__version__}")

    cfg = TinyConfig()
    model = TinyTransformer(cfg).to(dev).eval()
    n_param = sum(p.numel() for p in model.parameters())
    print(f"  Model: {cfg.num_hidden_layers}L/{cfg.hidden_size}D/{cfg.num_attention_heads}H"
          f"  ({n_param:,} params)\n")

    quantizer = KVCacheQuantizer(cfg.num_hidden_layers)
    n = cfg.num_hidden_layers

    full = gendata(b=1, seq=128).to(dev)
    pref = full[:, :64]
    gen = full[:, 64:]

    # Build reference FP16 past
    ref_past = run_prefill(model, pref)

    # Tests
    tests = [
        ([16] * n, "FP16 (baseline)"),
        ([8] * n,  "Uniform 8-bit"),
        ([4] * n,  "Uniform 4-bit"),
        ([2] * n,  "Aggressive 2-bit"),
        ([8, 8, 4, 4], "Layer-discrim 8-8-4-4"),
        ([8, 4, 4, 2], "Layer-discrim 8-4-4-2"),
        ([4, 4, 2, 2], "Layer-discrim 4-4-2-2"),
    ]

    results = []
    for bc, nm in tests:
        if len(bc) != n:
            continue  # skip if config doesn't match layer count
        print(f"  [{nm}]  bits={bc}  ", end="", flush=True)
        r = run_test(model, pref, gen, quantizer, bc, nm, ref_past)
        results.append(r)
        print(f"MSE={r.mse:.6e}  ratio={r.ratio:.2f}x  cache={r.cache_mb:.4f} MB")

    # Summary
    print("\n" + "=" * 68)
    print("  RESULTS")
    print("=" * 68)
    h = f"  {'Method':<28} {'Bits':<18} {'Cache (MB)':<12} {'Ratio':<10} {'MSE':<14}"
    print(h)
    print(f"  {'-'*28} {'-'*18} {'-'*12} {'-'*10} {'-'*14}")
    for r in results:
        bits_str = "-".join(str(b) for b in r.bit_config)
        print(f"  {r.name:<28} {bits_str:<18} {r.cache_mb:<12.4f} {r.ratio:<10.2f}x {r.mse:<14.6e}")

    # Save
    data = {
        "config": {
            "hidden_size": cfg.hidden_size,
            "num_layers": n,
            "num_heads": cfg.num_attention_heads,
            "prefill_len": 64,
            "gen_len": gen.size(1),
        },
        "tests": [
            {
                "name": r.name,
                "bit_config": r.bit_config,
                "cache_mb": r.cache_mb,
                "ratio": r.ratio,
                "mse": r.mse,
            }
            for r in results
        ],
    }
    with open("poc_results.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  📄 poc_results.json saved")
    print(f"\n{'='*68}")
    print("  ✅ PoC complete!")
    print(f"{'='*68}")


if __name__ == "__main__":
    main()
