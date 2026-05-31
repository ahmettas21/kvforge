# KVForge Architecture

## Felsefe: "Saklamak yerine yeniden üretmeyi öğren"

Standart transformer modellerinde, generation sırasında her token için 
Key (K) ve Value (V) matrisleri hesaplanır ve önbelleğe alınır (KV Cache).
Bu cache, context uzunluğuyla doğru orantılı olarak büyür:

```
Cache_size = 2 × n_layers × n_heads × seq_len × head_dim
```

GPT2-small için (seq=1024): ~24 MB
GPT3-175B için (seq=2048): ~3.5 GB

KVForge bu cache'i **seed vektörlerine** dönüştürür.

## Seed Compression Detayları

### Encoder (KV → Seed)

```
Girdi: K [batch, seq, d_model], V [batch, seq, d_model]
  │
  ├─ Concat(K, V) → [batch, seq, 2*d_model]
  │
  ├─ Linear(2*d_model → d_model)
  │
  ├─ GELU activation
  │
  ├─ Linear(d_model → seed_dim)
  │
  └─ LayerNorm(seed_dim)
       │
       ▼
  Çıktı: Seed [batch, seq, seed_dim]
```

### Decoder (Seed → KV)

```
Girdi: Seed [batch, seq, seed_dim]
  │
  ├─ Linear(seed_dim → d_model)
  │
  ├─ GELU activation
  │
  ├─ Linear(d_model → 2*d_model)
  │
  └─ Chunk(2)
       │
       ▼
  Çıktı: K' [batch, seq, d_model], V' [batch, seq, d_model]
```

### Sıkıştırma Oranları

| Konfigürasyon | d_model | seed_dim | 2*d_model/seed_dim | Bellek Tasarrufu |
|---------------|---------|----------|-------------------|-----------------|
| Nano | 64 | 16 | 8× | %87.5 |
| Small | 256 | 32 | 16× | %93.75 |
| Medium (GPT2) | 768 | 64 | 24× | %95.83 |
| Large (LLaMA) | 4096 | 128 | 64× | %98.44 |

## Loss Fonksiyonu

Toplam loss iki bileşenden oluşur:

```
L_total = L_CE + λ × L_recon
```

**L_CE**: Standart cross-entropy (next token prediction)
**L_recon**: Reconstruction MSE loss
**λ**: 0.1 (başlangıç), eğitim ilerledikçe decay

Reconstruction loss'un varlığı, seed'in orijinal KV bilgisini korumasını zorunlu kılar.

## Eğitim Stratejisi

1. **Phase 1: Warm-up** (λ=0.1, yüksek LR)
   - Model token prediction'ı öğrenirken seed compression da başlar
   
2. **Phase 2: Stabilization** (λ decay)
   - Reconstruction loss azaltılır
   - Model seed'den daha iyi KV üretmeyi öğrenir

3. **Phase 3: Inference** (λ=0)
   - Sadece seed cache kullanılır
   - Reconstruction loss hesaplanmaz

## KV Cache Karşılaştırması

| Özellik | Standart KV Cache | KVForge Seed Cache |
|---------|------------------|-------------------|
| Saklanan | K, V matrisleri | Seed vektörleri |
| Boyut | 2 × d_model × seq | seed_dim × seq |
| Erişim | Doğrudan okuma | Decode + okuma |
| Kayıp | Yok | Minimal (recon loss) |
| Ölçeklenebilirlik | O(seq) | O(seq) ama 24× küçük |
