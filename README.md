# KVForge — Seed-based KV Cache Compression

**Replace KV Cache with Learned Seed Reconstruction**

KVForge, transformer modellerinde kullanılan klasik KV (Key-Value) cache mekanizmasını **seed vektörlerine** dönüştüren özgün bir mimaridir. K, V matrislerini saklamak yerine, onları küçük seed vektörlerine sıkıştırır ve ihtiyaç duyulduğunda yeniden üretir.

```
Felsefe: "Saklamak yerine yeniden üretmeyi öğren"
```

## 🧠 Temel Fikir

Standart transformer attention'da her token için K ve V matrisleri saklanır:

```
Cache = {K_1, V_1, K_2, V_2, ..., K_n, V_n}  →  2 × n × d_model boyutunda
```

KVForge'da ise:

```
Seed_n = Encoder(K_n, V_n)                      →  seed_dim boyutunda (24× sıkıştırma)
K_n', V_n' = Decoder(Seed_n)                    →  yeniden üretim
Cache = {Seed_1, Seed_2, ..., Seed_n}           →  çok daha küçük
```

## 📐 Mimari Detayları

### Seed Attention Modülü

```
Girdi: x [batch, seq, d_model]
  │
  ├─→ Q = Linear(x)
  ├─→ K = Linear(x)
  └─→ V = Linear(x)
       │
       ▼
  ┌─────────────────────┐
  │   SEED ENCODER      │
  │  ┌───────────────┐  │
  │  │ Concat(K, V)  │  │  [batch, seq, 2*d_model]
  │  │ Linear(d_model)│  │
  │  │ GELU          │  │
  │  │ Linear(seed)  │  │  [batch, seq, seed_dim]
  │  │ LayerNorm     │  │
  │  └───────────────┘  │
  │        ⇓            │
  │   SEED DECODER      │
  │  ┌───────────────┐  │
  │  │ Linear(d_model)│  │
  │  │ GELU          │  │
  │  │ Linear(2*d)   │  │  [batch, seq, 2*d_model]
  │  └───────────────┘  │
  └─────────────────────┘
       │
       ▼
  K', V' = Chunk(2)     →  Yeniden üretilmiş KV
       │
       ▼
  Scaled Dot-Product Attention(Q, K', V')
       │
       ▼
  Çıktı: [batch, seq, d_model]
```

### Kayıp Fonksiyonu

```
Loss = CrossEntropy + λ × ReconstructionLoss

ReconstructionLoss = MSE(K_original, K_reconstructed) 
                   + MSE(V_original, V_reconstructed)
                   
λ = 0.1 (başlangıç, eğitim boyunca azaltılabilir)
```

### Sıkıştırma Oranı

| Model | d_model | seed_dim | Oran |
|-------|---------|----------|------|
| Nano | 64 | 16 | 8× |
| Small | 256 | 32 | 16× |
| Medium | 768 | 64 | 24× |
| Large | 1024 | 128 | 16× |

## 📦 Repo Yapısı

```
kvforge/
├── kvforge/                    # Ana kaynak kodu
│   ├── __init__.py
│   ├── seed_attention.py       # SeedAttention modülü
│   ├── nano_model.py           # Nano model (byte-level)
│   ├── full_model.py           # GPT2-small seed model
│   ├── train_nano.py           # Nano eğitim scripti
│   └── generate.py             # Üretim/çıkarım scripti
├── scripts/                    # Yardımcı scriptler
│   ├── download_tinyshakespeare.sh
│   └── benchmark.sh
├── tests/                      # Testler
│   └── test_seed_attention.py
├── docs/                       # Dokümantasyon
│   ├── architecture.md
│   ├── training.md
│   └── results.md
├── checkpoints/                # Model ağırlıkları (gitignore)
├── requirements.txt
├── setup.py
├── README.md
└── LICENSE
```

## 🚀 Hızlı Başlangıç

```bash
# Kurulum
pip install -r requirements.txt

# Nano model eğitimi (CPU'da ~10-15 dk)
python -m kvforge.train_nano

# Full model eğitimi (GPU önerilir)
python -m kvforge.train_full

# Generation test
python -m kvforge.generate --prompt "ROMEO: "
```

## 📊 Nano Model Sonuçları (CPU'da eğitildi)

### KVForge vs Vanilla — Benchmark Karşılaştırması

Aynı mimari (2L, 4H, 64D, 32 seq, byte-level) üzerinde SeedAttention ile standart attention karşılaştırması:

| Metrik | Vanilla (standart) | KVForge (seed) | Fark |
|--------|-------------------|-----------------|------|
| **Parametre** | 118,016 | 155,488 | +37,472 (%31.7) |
| **Attention parametre** | 32,768 | 70,240 | +37,472 (%114) |
| **Inference hızı** | 323 pas/s | 250 pas/s | ×1.29 yavaş |
| **KV cache boyutu** | 2×64×seq = 128×seq | 16×seq = 16×seq | **8× sıkıştırma** |

> **KVForge'un bedeli:** +%31.7 parametre, ×1.29 inference overhead
> **KVForge'un kazancı:** 8× daha küçük KV cache. Daha büyük modellerde (768D, seed=64) bu oran **24×'e** çıkar.

### Performans Detayları

| Metrik | Değer |
|--------|-------|
| Parametre | 155.5K |
| Eğitim süresi | ~25 dk (CPU) |
| Final Loss | 2.25 |
| Validation PPL | 9.5 |
| Recon Loss | 0.020 |
| Inference hızı | 27 pas/s (CPU) |
| RAM kullanımı | ~500 MB |

## 🔬 Full Model (GPT2-small tabanlı)

| Özellik | Değer |
|---------|-------|
| Katman | 12 |
| Head | 12 |
| d_model | 768 |
| seed_dim | 64 (24× sıkıştırma) |
| Parametre | 153.3M |
| Eğitim için | ~3-4 GB VRAM (GPU) |

## 📚 Referanslar ve İlgili Çalışmalar

- [KV Cache: Transformer Generation Speed](https://huggingface.co/blog/kv-cache)
- [NanoGPT by Karpathy](https://github.com/karpathy/nanoGPT)
- [TinyStories Dataset](https://huggingface.co/datasets/roneneldan/TinyStories)
- [GPT2 Paper](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

## 🤝 Katkı

Bu proje bir araştırma konseptidir. Seed-based KV Cache fikri, "saklamak yerine yeniden üret" felsefesine dayanır. Katkılar, PR'ler, ve fikirler her zaman açıktır.

## 📜 Lisans

MIT
