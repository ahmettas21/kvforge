#!/usr/bin/env python3
"""
Base Encode + LoRA Decode PoC
==============================
KvForge'nin temel konsepti:
- Base model encode: KV cache'i full precision'da hesapla
- LoRA Decode: Sadece generation/answer decoding sırasında LoRA adapter'ı aktif et

Araştırma bulgusu (arXiv:2606.05698):
- %75+ sıkıştırmada, base encode + LoRA decode en iyi pattern
- LoRA'nın değeri compression arttıkça artıyor
"""

import json, math, time, os
from dataclasses import dataclass
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

class LoRALinear(nn.Module):
    """Linear with optional LoRA adapter."""
    def __init__(self, in_features, out_features, bias=False, r=8, alpha=16):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features, bias=bias)
        self.r = r
        self.scaling = alpha / r
        self.lora_A = nn.Parameter(torch.randn(in_features, r) * 0.01)
        self.lora_B = nn.Parameter(torch.zeros(r, out_features))
        self.lora_active = False

    def forward(self, x):
        base = self.linear(x)
        if self.lora_active and self.r > 0:
            lora_out = (x @ self.lora_A @ self.lora_B) * self.scaling
            return base + lora_out
        return base

    def activate_lora(self, active=True):
        self.lora_active = active

class Attention(nn.Module):
    def __init__(self, cfg, use_lora=False):
        super().__init__()
        self.head_dim = cfg.hidden_size // cfg.num_attention_heads
        self.num_heads = cfg.num_attention_heads
        d = cfg.hidden_size
        if use_lora:
            self.q_proj = LoRALinear(d, d, bias=False, r=8)
            self.k_proj = LoRALinear(d, d, bias=False, r=8)
            self.v_proj = LoRALinear(d, d, bias=False, r=8)
            self.o_proj = LoRALinear(d, d, bias=False, r=8)
        else:
            self.q_proj = nn.Linear(d, d, bias=False)
            self.k_proj = nn.Linear(d, d, bias=False)
            self.v_proj = nn.Linear(d, d, bias=False)
            self.o_proj = nn.Linear(d, d, bias=False)
        self.rotary = RotaryEmbedding(self.head_dim, cfg.max_position_embeddings)

    def set_lora_active(self, active):
        for p in [self.q_proj, self.k_proj, self.v_proj, self.o_proj]:
            if hasattr(p, 'activate_lora'):
                p.activate_lora(active)

    def forward(self, h, past_kv=None, use_cache=False):
        B, S, D = h.shape; H = self.num_heads; hd = self.head_dim
        q = self.q_proj(h).view(B,S,H,hd).transpose(1,2)
        k = self.k_proj(h).view(B,S,H,hd).transpose(1,2)
        v = self.v_proj(h).view(B,S,H,hd).transpose(1,2)
        offset = 0 if past_kv is None else past_kv[0].size(2)
        sin, cos = self.rotary(q, offset)
        q, k = apply_rotary(q, sin, cos), apply_rotary(k, sin, cos)
        if past_kv is not None:
            k = torch.cat([past_kv[0], k], dim=2)
            v = torch.cat([past_kv[1], v], dim=2)
        T = k.size(2)
        mask = torch.full((S,T), float("-inf"), device=q.device, dtype=q.dtype)
        mask = torch.triu(mask, diagonal=T-S+1)
        a = torch.matmul(q, k.transpose(-2,-1))/math.sqrt(hd) + mask.unsqueeze(0).unsqueeze(0)
        a = F.softmax(a, dim=-1).to(q.dtype)
        o = torch.matmul(a, v).transpose(1,2).reshape(B,-1,D)
        o = self.o_proj(o)
        return o, (k, v) if use_cache else None

class MLP(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.gate = nn.Linear(cfg.hidden_size, cfg.intermediate_size, bias=False)
        self.up = nn.Linear(cfg.hidden_size, cfg.intermediate_size, bias=False)
        self.down = nn.Linear(cfg.intermediate_size, cfg.hidden_size, bias=False)
    def forward(self, x):
        return self.down(F.silu(self.gate(x)) * self.up(x))

class Block(nn.Module):
    def __init__(self, cfg, i, use_lora=False):
        super().__init__()
        self.attn = Attention(cfg, use_lora)
        self.mlp = MLP(cfg)
        self.ln1 = nn.LayerNorm(cfg.hidden_size)
        self.ln2 = nn.LayerNorm(cfg.hidden_size)
    def set_lora_active(self, active):
        self.attn.set_lora_active(active)
    def forward(self, h, past_kv=None, use_cache=False):
        a, pkv = self.attn(self.ln1(h), past_kv, use_cache)
        h = h + a
        h = h + self.mlp(self.ln2(h))
        return h, pkv

class TinyTransformer(nn.Module):
    def __init__(self, cfg, use_lora=False):
        super().__init__()
        self.embed = nn.Embedding(cfg.vocab_size, cfg.hidden_size)
        self.blocks = nn.ModuleList([Block(cfg, i, use_lora) for i in range(cfg.num_hidden_layers)])
        self.ln = nn.LayerNorm(cfg.hidden_size)
        self.head = nn.Linear(cfg.hidden_size, cfg.vocab_size, bias=False)
        self.head.weight = self.embed.weight
    def set_lora_active(self, active):
        for blk in self.blocks:
            blk.set_lora_active(active)
    def forward(self, ids, past_key_values=None, use_cache=False):
        h = self.embed(ids)
        new_past = [] if use_cache else None
        for i, blk in enumerate(self.blocks):
            pkv = past_key_values[i] if past_key_values is not None else None
            h, p = blk(h, pkv, use_cache)
            if use_cache: new_past.append(p)
        h = self.ln(h)
        logits = self.head(h)
        return logits, new_past if use_cache else None

# ── KV Cache Quantizer ────────────────────────────────────────

class KVCacheQuantizer:
    def __init__(self, num_layers):
        self.num_layers = num_layers
        self.bit_config = [16] * num_layers
        self.state = [None] * num_layers
    def set_bit_config(self, bc):
        self.bit_config = bc
    def quantize(self, t, li):
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
        if st["bits"] >= 16: return q
        return q.float() * st["scale"] + st["zp"]
    def compress_past_old(self, past_kv):
        return [self.quantize(k, i) + (self.quantize(v, i) for _ in [0])[:0] or 
                (lambda: None)() or 
                ((lambda qk,stk: qk)(*self.quantize(k,i)), (lambda qv,stv: qv)(*self.quantize(v,i)))
                for i,(k,v) in enumerate(past_kv)]
    def compress_past_v2(self, past_kv):
        compressed = []
        for i, (k, v) in enumerate(past_kv):
            qk, _ = self.quantize(k, i)
            qv, _ = self.quantize(v, i)
            compressed.append((qk, qv))
        return compressed
    def decompress_past(self, compressed):
        return [(self.dequantize(qk, i), self.dequantize(qv, i)) for i, (qk, qv) in enumerate(compressed)]

# ── Test Helpers ──────────────────────────────────────────────

def gendata(b=1, seq=128, vs=50257):
    return torch.randint(0, min(vs, 10000), (b, seq))

@torch.no_grad()
def run_prefill(model, ids):
    _, past = model(ids, use_cache=True)
    return past

@torch.no_grad()
def compute_ppl(model, prompt_ids, past):
    logits, _ = model(prompt_ids, past_key_values=past, use_cache=False)
    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = prompt_ids[:, 1:].contiguous()
    loss = F.cross_entropy(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
    return math.exp(loss.item())

def cache_mb(past_kv):
    return sum(k.numel()*k.element_size() + v.numel()*v.element_size() for k,v in past_kv) / (1024**2)

# ── Main ──────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("  Base Encode + LoRA Decode — KvForge PoC")
    print("=" * 72)

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"  Device: {dev}")
    
    cfg = TinyConfig()
    lora_model = TinyTransformer(cfg, use_lora=True).to(dev).eval()
    # Init LoRA
    for n, p in lora_model.named_parameters():
        if 'lora_A' in n: nn.init.normal_(p, std=0.01)
        elif 'lora_B' in n: nn.init.zeros_(p)
    
    n_total = sum(p.numel() for p in lora_model.parameters())
    n_lora = sum(p.numel() for n, p in lora_model.named_parameters() if 'lora' in n) 
    n_lora_actual = sum(p.numel() for n, p in lora_model.named_parameters() if 'lora' in n)
    n_base = n_total - n_lora_actual
    print(f"  Model: {cfg.num_hidden_layers}L/{cfg.hidden_size}D "
          f"({n_base:,} base + {n_lora_actual:,} LoRA params)")
    
    quantizer = KVCacheQuantizer(cfg.num_hidden_layers)
    prompt = gendata(b=1, seq=64).to(dev)
    
    results = []
    
    def run_test(name, mode, bit_config=None):
        """mode: 'full_lora' or 'base_encode_lora_decode'"""
        if bit_config:
            quantizer.set_bit_config(bit_config)
        
        # === PREFILL ===
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        t0 = time.time()
        lora_model.set_lora_active(mode == 'full_lora')
        past = run_prefill(lora_model, prompt)
        t_prefill = time.time() - t0
        
        # === COMPRESS (if needed) ===
        if bit_config and any(b < 16 for b in bit_config):
            compressed = quantizer.compress_past_v2(past)
            past = quantizer.decompress_past(compressed)
            c_mb = sum(qk.numel()*qk.element_size() + qv.numel()*qv.element_size() 
                       for qk,qv in compressed) / (1024**2)
        else:
            c_mb = cache_mb(past)
        
        # === DECODE ===
        t0 = time.time()
        if mode == 'base_encode_lora_decode':
            lora_model.set_lora_active(True)
        # Generate 1 token (to measure decode with LoRA)
        with torch.no_grad():
            tok = prompt[:, -1:]
            for _ in range(8):  # 8 gen tokens
                l, past = lora_model(tok, past_key_values=past, use_cache=True)
                tok = l[:, -1:].argmax(dim=-1)
        t_decode = time.time() - t0
        
        # Turn off LoRA
        lora_model.set_lora_active(False)
        
        # PPL
        ppl = compute_ppl(lora_model, prompt, past)
        
        total_ms = round((t_prefill + t_decode) * 1000, 2)
        name_s = name[:38]
        bc_s = '-'.join(str(b) for b in (bit_config or [16]*cfg.num_hidden_layers))
        print(f"  {name_s:<38} P:{t_prefill*1000:>7.1f}ms D:{t_decode*1000:>7.1f}ms "
              f"Cache:{c_mb:.3f}MB PPL:{ppl:.4f}")
        
        results.append({
            'name': name, 'mode': mode,
            'bit_config': bit_config or [16]*cfg.num_hidden_layers,
            'prefill_ms': round(t_prefill*1000, 2),
            'decode_ms': round(t_decode*1000, 2),
            'total_ms': total_ms,
            'cache_mb': round(c_mb, 4),
            'perplexity': round(ppl, 4),
        })
    
    n = cfg.num_hidden_layers
    
    print(f"\n  {'Test':<38} {'Prefill':>8} {'Decode':>8} {'Cache':>10} {'PPL':>8}")
    print(f"  {'-'*38} {'-'*8} {'-'*8} {'-'*10} {'-'*8}")
    
    # Test 1: Full LoRA FP16 (baseline)
    run_test("Full LoRA FP16 (baseline)", "full_lora", [16]*n)
    # Test 2: Base Encode + LoRA Decode FP16
    run_test("Base Encode + LoRA Decode FP16", "base_encode_lora_decode", [16]*n)
    # Test 3: Full LoRA 8-bit
    run_test("Full LoRA 8-bit", "full_lora", [8]*n)
    # Test 4: Base Encode + LoRA Decode 8-bit
    run_test("Base Encode + LoRA Decode 8-bit", "base_encode_lora_decode", [8]*n)
    # Test 5: Base Encode + LoRA Decode 4-bit
    run_test("Base Encode + LoRA Decode 4-bit", "base_encode_lora_decode", [4]*n)
    # Test 6: Base Encode + LoRA Decode layer-discrim 8,8,4,4
    run_test("L-Discrim 8,8,4,4 + LoRA Decode", "base_encode_lora_decode", [8,8,4,4])
    
    # === SUMMARY ===
    bl = results[0]
    print(f"\n{'='*72}")
    print(f"  📊 ÖZET")
    print(f"{'='*72}")
    print(f"  Baseline: PPL={bl['perplexity']}, Cache={bl['cache_mb']}MB, {bl['total_ms']}ms")
    print(f"")
    for r in results:
        cache_r = bl['cache_mb'] / r['cache_mb']
        ppl_d = r['perplexity'] - bl['perplexity']
        marker = "✅" if ppl_d < 1.0 else "⚠️" if ppl_d < 5.0 else "❌"
        print(f"  {marker} {r['name']:<36} Cache:{cache_r:.1f}x  PPL:{r['perplexity']:.2f} ({ppl_d:+.2f})")
    
    # Save
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, 'poc_results.json')
    with open(out_path, 'w') as f:
        json.dump({
            'config': {
                'hidden_size': cfg.hidden_size,
                'num_layers': n,
                'num_heads': cfg.num_attention_heads,
                'prefill_len': prompt.size(1),
                'lora_rank': 8,
            },
            'results': results,
        }, f, indent=2)
    print(f"\n  📄 {out_path} saved")
    print(f"\n{'='*72}")
    print(f"  ✅ PoC tamamlandı!")
    print(f"{'='*72}")

if __name__ == "__main__":
    main()
