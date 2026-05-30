# Training Guide

## Nano Model (CPU)

En hızlı başlangıç:

```bash
# 1. Dataset indir
wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

# 2. Eğitim
python -m kvforge.train_nano
# ~10-15 dakika, CPU'da çalışır
# Best model → checkpoints/nano_best.pt
```

## Full Model (GPU Önerilir)

```bash
# 1. TinyStories dataset
python -c "from datasets import load_dataset; ds = load_dataset('roneneldan/TinyStories', split='train')"

# 2. Eğitim
python -m kvforge.full_model --train
# ~2-4 saat (GPU), ~20+ saat (CPU)
```

## Hiperparametre Ayarları

### Nano Model (CPU Optimized)

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| d_model | 64 | Hidden size |
| n_heads | 4 | Attention heads |
| n_layers | 2 | Transformer layers |
| seed_dim | 16 | Seed compression |
| seq_len | 32 | Context window |
| batch_size | 64 | Batch size |
| lr | 3e-3 | Learning rate |
| recon_lambda | 0.1 | Recon loss weight |

### Full Model (GPU Optimized)

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| d_model | 768 | Hidden size |
| n_heads | 12 | Attention heads |
| n_layers | 12 | Transformer layers |
| seed_dim | 64 | Seed compression |
| seq_len | 256 | Context window |
| batch_size | 4 (CPU) / 32 (GPU) | Batch size |
| lr | 3e-4 | Learning rate |
| recon_lambda | 0.1 | Recon loss weight |

## Monitoring

Eğitim sırasında takip edilmesi gereken metrikler:

- **Loss**: Düzenli düşüş (başlangıç ~11, hedef ~2-3)
- **Perplexity**: exp(Loss_CE), düşük iyi
- **Recon Loss**: Seed'in KV'yı ne kadar iyi yeniden ürettiği
- **Recon/CE Ratio**: <0.1 ideal (recon loss çok baskın değil)

## Checkpoint Structure

```python
{
    'model_state_dict': ...,  # Model ağırlıkları
    'optimizer_state_dict': ...,  # Optimizer durumu
    'scheduler_state_dict': ...,  # Scheduler durumu
    'epoch': int,  # Son epoch
    'loss': float,  # Validation loss
    'config': {
        'vocab_size': 256,
        'd_model': 64,
        'n_heads': 4,
        'n_layers': 2,
        'seed_dim': 16,
    }
}
```
