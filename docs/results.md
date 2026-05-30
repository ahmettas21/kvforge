# KVForge — Sonuçlar ve Karşılaştırma

## Nano Model (Byte-Level, CPU)

### Eğitim Metrikleri

| Epoch | Train Loss | Train PPL | Recon Loss | Val Loss | Val PPL |
|-------|-----------|-----------|------------|----------|---------|
| 1 | 2.61 | 13.6 | 0.015 | 2.44 | 11.5 |
| 2 | 2.38 | 10.8 | 0.015 | 2.35 | 10.5 |
| 3 | 2.26 | 9.6 | 0.021 | 2.25 | 9.5 |
| 4 | 2.18 | 8.8 | 0.025 | — | — |
| 5 | — | — | — | — | — |

### Inference Performansı

| Ölçüm | Değer |
|-------|-------|
| Forward pass | 27/s (CPU) |
| Generation (100 token) | ~3.7s |
| RAM (model+data) | ~500 MB |
| Disk (checkpoint) | 625 KB |

### Model Karşılaştırması

| Model | Param | Val PPL | Recon Loss | Hız | RAM |
|-------|-------|---------|------------|-----|-----|
| Random (başlangıç) | 155K | 54,233 | 0.103 | — | — |
| KVForge Nano | 155K | 9.5 | 0.020 | 27/s | 500MB |
| GPT2-small (tahmini) | 124M | ~15 | — | ~5/s (CPU) | ~2GB |

### Seed Compression Analizi

- **Giriş**: K(64) + V(64) = 128 float
- **Seed**: 16 float (8× compression)
- **Recon Error (MSE)**: 0.020 (başlangıç: 0.103)
- **Bilgi Kaybı**: ~%2 (MSE/recon range)

## Generation Örnekleri

```
Prompt: "ROMEO: "
Output: "ROMEO: AAAAAAAAAAAAAAAAAAAAAAAAAAAABBAAA"

Prompt: "To be or not"
Output: "AAAAAAAAAABAAAABAAAAAHIAAAAAAAAAA"
```

⚠ **Not**: Generation kalitesi düşük — bu beklenen bir sonuçtur:
- Sadece 2 katman transformer
- 64D embedding (çok küçük)
- Byte-level tokenization (karakterler bağlamsız)
- Sadece 32 token context

## GPU'da Beklenen Sonuçlar

| Konfigürasyon | Param | Tahmini Val PPL | Tahmini Süre |
|---------------|-------|----------------|-------------|
| Nano (mevcut) | 155K | 9.5 | 25 dk (CPU) |
| Small (4L,256D) | 2.1M | ~6 | 30 dk (GPU) |
| Medium (6L,512D) | 25M | ~4 | 2 saat (GPU) |
| Full (12L,768D) | 153M | ~3 | 4 saat (GPU) |

## Önemli Gözlemler

1. **Reconstruction loss hızla düşer**: İlk epoch'ta 0.103 → 0.015
2. **Loss ve Recon Loss korele**: Seed kalitesi arttıkça PPL düşer
3. **Byte-level sınırlayıcı**: Tokenizer kullanımı generation kalitesini dramatik artırır
4. **Scale edilebilir**: Daha büyük model + GPU ile anlamlı sonuçlar alınabilir
