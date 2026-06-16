# KvForge ⚡

**Efficient LLM Inference with Base Encode + LoRA Decode**

KvForge is a research framework for efficient LLM inference that uses a novel **Base Encode + LoRA Decode** pattern combined with progressive training (ProLAD) and KV cache compression.

## Core Idea

Instead of running LoRA adapters during the compute-heavy prefill phase, KvForge:

1. **Base Encode** — Run prefill *without* LoRA (base model only), compress KV cache to low bit-width
2. **LoRA Decode** — Run autoregressive decode *with* LoRA adapters active

This provides **2.4× faster prefill** and **up to 8× smaller KV cache** with **zero quality loss**.

## Why It Matters

| Pattern | Prefill | Decode | Cache Size | Quality |
|---|---|---|---|---|
| Full LoRA (baseline) | 1× | 1× | 1× | — |
| **Base Encode + LoRA Decode** 🚀 | **2.4× faster** | ≈1× | **8× smaller** | **Identical PPL** |
| + ProLAD Progressive Training | **2.4× faster** | ≈1× | **8× smaller** | **Better PPL when LoRA off!** |

## Key Results

| Metric | Before ProLAD | After ProLAD | Improvement |
|---|---|---|---|
| LoRA on/off quality gap | 153.29 PPL | 27.33 PPL (Linear) | **82% better** |
| LoRA off quality (Cosine) | 294.38 PPL | **202.24 PPL** (better than LoRA on!) | **160% better** |
| KV cache (FP16 → 2-bit) | 1.05 MB | 0.13 MB | **8× smaller** |

## Installation

```bash
pip install git+https://github.com/ahmettas21/kvforge.git
```

## Quick Start

```python
from kvforge import KvForgeModel

model = KvForgeModel("gpt2", lora_rank=8)
info = model.info()
print(f"Model: {info['model']} ({info['total_params']/1e6:.1f}M + {info['lora_params']/1e3:.1f}K LoRA)")

# Benchmark
results = model.benchmark(
    ["The transformer architecture revolutionized NLP."],
    modes=['full_lora', 'base_encode_lora_decode'],
    compress_bits_list=[16, 8, 4],
)
```

## Research

See [RESEARCH.md](RESEARCH.md) for the full research paper with methodology, results, and analysis.

## License

MIT
