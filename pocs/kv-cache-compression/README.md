# MiniKV-style KV Cache Compression — PoC

## Ne bu?

KV cache compression için PyTorch tabanlı bir proof-of-concept. MiniKV makalesindeki layer-discriminative quantization yaklaşımını test ediyor.

## Sonuçlar

4-layer tiny transformer (256 hidden, 4 heads) üzerinde 64 token prefill + 64 token generation:

| Method | Bits | Cache (MB) | Ratio | MSE |
|---|---|---|---|---|
| FP16 (baseline) | 16-16-16-16 | 0.5000 | 1.00x | 0 |
| Uniform 8-bit | 8-8-8-8 | 0.1250 | 4.00x | 0.016 |
| Uniform 4-bit | 4-4-4-4 | 0.1250 | 4.00x | 0.018 |
| Aggressive 2-bit | 2-2-2-2 | 0.1250 | 4.00x | 0.120 |
| **Layer-discrim 8-8-4-4** | 8-8-4-4 | 0.1250 | 4.00x | **0.016** |
| Layer-discrim 8-4-4-2 | 8-4-4-2 | 0.1250 | 4.00x | 0.038 |
| Layer-discrim 4-4-2-2 | 4-4-2-2 | 0.1250 | 4.00x | 0.059 |

> **Not:** Ratio 4.00x'te sabit çünkü PoC'de uint8 kullanıyoruz. Gerçek bit-packing ile 8-bit = 2×, 4-bit = 4×, 2-bit = 8× compression yakalanır.

## Çıkarımlar

1. **Layer-discriminative çalışıyor** — 8-8-4-4 konfigürasyonu saf 8-bit ile neredeyse aynı MSE'yi veriyor
2. **2-bit tek başına kötü** — 0.12 MSE, quantization noise çok yüksek
3. **En iyi trade-off** — early layer'lar 8-bit, deep layer'lar 4-bit → hem compression kazanımı hem kalite

## Faz 2 (Plan)

- [ ] Gerçek bit-packing ile compression ratio'yu düzelt
- [ ] Attention head bazında quantization (MiniKV'deki gibi depth-wise similarity)
- [ ] Gerçek modelde test (GPT-2 small / Llama 1B)
- [ ] PPL metric'i ekle (random data yerine WikiText-2)

## Faz 3 (Plan)

- [ ] LoRA adapter ile kombine KV cache sharing
- [ ] CacheBlend tarzı selective recomputation
- [ ] Birden fazla adapter arasında cache reuse
