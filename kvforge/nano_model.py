"""
KVForge NANO Model
==================
Byte-level Seed Attention Transformer — CPU'da 10 dakikada eğitim.

Bu model, KVForge mimarisinin konsept ispatıdır:
  - K,V matrislerini seed'e sıkıştır (8× compression)
  - Seed'den K,V yeniden üret
  - Reconstruction loss ile kaliteyi koru

Hiperparametreler (DEĞİŞTİRME — CPU'da çalışacak şekilde optimize):
  VOCAB_SIZE = 256    (byte-level, tokenizer gerekmez)
  D_MODEL     = 64    (embedding boyutu)
  N_HEADS     = 4     (attention head sayısı)
  N_LAYERS    = 2     (transformer katmanı)
  SEQ_LEN     = 32    (context uzunluğu)
  SEED_DIM    = 16    (seed vektör boyutu - 8× compression)
  BATCH_SIZE  = 64    (batch boyutu)
  LR          = 3e-3  (learning rate)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import math
import time
import os

# ============================================================
# HİPERPARAMETRELER
# ============================================================
VOCAB_SIZE = 256      # Byte-level kelime haznesi (0-255)
D_MODEL = 64           # Model hidden dimension
N_HEADS = 4            # Multi-head attention head sayısı
N_LAYERS = 2           # Transformer blok sayısı
SEQ_LEN = 32           # Maksimum sequence length
SEED_DIM = 16          # Seed vektör boyutu (compression ratio: 2*64/16 = 8x)
BATCH_SIZE = 64        # Training batch size
D_FF = 4 * D_MODEL     # Feed-forward hidden dimension (256)
DROPOUT = 0.1          # Dropout oranı
LR = 3e-3              # Learning rate
WEIGHT_DECAY = 0.01    # AdamW weight decay
NUM_EPOCHS = 5         # Eğitim epoch sayısı
RECON_LAMBDA = 0.1     # Reconstruction loss ağırlığı (λ)


# ============================================================
# SEED ATTENTION — KVForge'un Kalbi
# ============================================================
class NanoSeedAttention(nn.Module):
    """
    Seed-based Multi-Head Attention.
    
    Standart attention:
        K, V = Linear(x)  → store in cache  →  2 × seq × d_model
    
    KVForge attention:
        K, V = Linear(x)  → compress to seed (d_model → seed_dim)
        store seed only    →  seq × seed_dim (8× smaller)
        reconstruct K,V from seed on demand
    
    Mimarideki Adımlar:
    1. Q, K, V projeksiyonları (standart linear)
    2. K ve V'yi concatenate et → [batch, seq, 2*d_model]
    3. Seed Encoder: 2*d_model → GELU → seed_dim
    4. Seed Decoder: seed_dim → GELU → 2*d_model
    5. Yeniden üretilen K', V' = chunk(2)
    6. Scaled Dot-Product Attention(Q, K', V')
    7. Output projection
    """
    
    def __init__(self):
        super().__init__()
        assert D_MODEL % N_HEADS == 0, "d_model must be divisible by n_heads"
        
        self.head_dim = D_MODEL // N_HEADS  # 64/4 = 16
        
        # === Standart QKV Projeksiyonları ===
        self.q_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.k_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.v_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.out_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        
        # === KVForge: Seed Compression Modülü ===
        # Encoder: K,V → seed
        self.seed_encoder = nn.Sequential(
            nn.Linear(2 * D_MODEL, D_MODEL),  # 128 → 64
            nn.GELU(),
            nn.Linear(D_MODEL, SEED_DIM),     # 64 → 16
        )
        
        # Decoder: seed → K,V
        self.seed_decoder = nn.Sequential(
            nn.Linear(SEED_DIM, D_MODEL),     # 16 → 64
            nn.GELU(),
            nn.Linear(D_MODEL, 2 * D_MODEL),  # 64 → 128
        )
        
        # Seed normalizasyonu (stabilite için)
        self.seed_norm = nn.LayerNorm(SEED_DIM)
        
    def _split_heads(self, x):
        """
        [batch, seq, d_model] → [batch, n_heads, seq, head_dim]
        """
        B, T, _ = x.shape
        return x.view(B, T, N_HEADS, self.head_dim).transpose(1, 2)
    
    def _merge_heads(self, x):
        """
        [batch, n_heads, seq, head_dim] → [batch, seq, d_model]
        """
        B, _, T, _ = x.shape
        return x.transpose(1, 2).contiguous().view(B, T, D_MODEL)
    
    def forward(self, x, return_seed=False):
        """
        Args:
            x: [batch, seq, d_model] — layer input
            return_seed: True ise reconstruction loss döndür
        
        Returns:
            output: [batch, seq, d_model]
            seed (optional): [batch, seq, seed_dim]
            recon_loss (optional): scalar
        """
        B, T, _ = x.shape
        
        # 1. Q, K, V projeksiyonları
        q = self.q_proj(x)
        k_orig = self.k_proj(x)  # Original K (loss hesaplamak için tut)
        v_orig = self.v_proj(x)  # Original V
        
        # 2. KV → Seed Compression
        kv_concat = torch.cat([k_orig, v_orig], dim=-1)  # [B, T, 128]
        seed = self.seed_encoder(kv_concat)               # [B, T, 16]
        seed = self.seed_norm(seed)                       # Normalize
        
        # 3. Seed → KV Reconstruction
        kv_recon = self.seed_decoder(seed)                # [B, T, 128]
        k, v = kv_recon.chunk(2, dim=-1)                  # [B, T, 64], [B, T, 64]
        
        # 4. Multi-Head Attention (yeniden üretilmiş K',V' ile)
        q = self._split_heads(q)   # [B, 4, T, 16]
        k = self._split_heads(k)   # [B, 4, T, 16]
        v = self._split_heads(v)   # [B, 4, T, 16]
        
        scale = 1.0 / math.sqrt(self.head_dim)
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * scale
        attn_weights = F.softmax(attn_weights, dim=-1)
        
        attn_output = torch.matmul(attn_weights, v)
        attn_output = self._merge_heads(attn_output)      # [B, T, 64]
        
        output = self.out_proj(attn_output)               # [B, T, 64]
        
        if return_seed:
            # Reconstruction Loss: original KV ile reconstructed KV arasında MSE
            recon_loss = F.mse_loss(kv_recon, kv_concat.detach())
            return output, seed, recon_loss
        
        return output


# ============================================================
# NANO TRANSFORMER
# ============================================================
class NanoKVForge(nn.Module):
    """
    Byte-level Seed-based Transformer.
    
    Mimarisi:
    1. Token Embedding (byte → d_model)
    2. Positional Embedding
    3. N_LAYERS × Transformer Block:
       a. LayerNorm → SeedAttention → Residual
       b. LayerNorm → MLP (GELU) → Residual
    4. Final LayerNorm
    5. LM Head (d_model → vocab_size)
    
    Weight Tying: token_embed.weight = head.weight
    """
    
    def __init__(self):
        super().__init__()
        
        # Token embedding (byte-level: 0-255)
        self.token_embed = nn.Embedding(VOCAB_SIZE, D_MODEL)
        
        # Positional embedding (0...SEQ_LEN-1)
        self.pos_embed = nn.Embedding(SEQ_LEN, D_MODEL)
        
        # Transformer blokları
        self.blocks = nn.ModuleList()
        for _ in range(N_LAYERS):
            block = nn.ModuleDict({
                'ln1': nn.LayerNorm(D_MODEL),
                'attn': NanoSeedAttention(),
                'ln2': nn.LayerNorm(D_MODEL),
                'mlp': nn.Sequential(
                    nn.Linear(D_MODEL, D_FF),    # 64 → 256
                    nn.GELU(),
                    nn.Dropout(DROPOUT),
                    nn.Linear(D_FF, D_MODEL),    # 256 → 64
                    nn.Dropout(DROPOUT),
                ),
            })
            self.blocks.append(block)
        
        # Final layer norm ve output head
        self.ln_f = nn.LayerNorm(D_MODEL)
        self.head = nn.Linear(D_MODEL, VOCAB_SIZE, bias=False)
        
        # Weight tying: embedding = output head
        self.token_embed.weight = self.head.weight
        
        # Xavier/Uniform initialization
        self._init_weights()
    
    def _init_weights(self):
        """
        GPT-2 style weight initialization:
        - Linear: normal(0, 0.02)
        - Embedding: normal(0, 0.02)
        - LayerNorm: ones(weight), zeros(bias)
        """
        for module in self.modules():
            if isinstance(module, nn.Linear):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)
                if module.bias is not None:
                    nn.init.zeros_(module.bias)
            elif isinstance(module, nn.Embedding):
                nn.init.normal_(module.weight, mean=0.0, std=0.02)
            elif isinstance(module, nn.LayerNorm):
                nn.init.ones_(module.weight)
                nn.init.zeros_(module.bias)
    
    def forward(self, input_ids, labels=None, return_seed=False):
        """
        Args:
            input_ids: [batch, seq] — byte token indices (0-255)
            labels: [batch, seq] — target labels (None = inference)
            return_seed: if True, compute reconstruction loss
        
        Returns:
            loss (optional): CrossEntropy + λ * ReconLoss
            logits: [batch, seq, vocab_size]
            recon_val (optional): scalar reconstruction loss
        """
        B, T = input_ids.shape
        assert T <= SEQ_LEN, f"Sequence length {T} exceeds max {SEQ_LEN}"
        
        # Token + Positional embeddings
        token_emb = self.token_embed(input_ids)                    # [B, T, 64]
        pos_emb = self.pos_embed(torch.arange(T, device=input_ids.device).unsqueeze(0))  # [1, T, 64]
        x = token_emb + pos_emb
        
        # Transformer blokları
        total_recon = 0.0
        for block in self.blocks:
            # Attention sub-layer
            residual = x
            x = block['ln1'](x)
            if return_seed:
                attn_out, seed, recon = block['attn'](x, return_seed=True)
                total_recon += recon
            else:
                attn_out = block['attn'](x, return_seed=False)
            x = residual + attn_out  # Residual connection
            
            # MLP sub-layer
            residual = x
            x = residual + block['mlp'](block['ln2'](x))
        
        # Final layer norm
        x = self.ln_f(x)
        
        # LM Head → vocabulary logits
        logits = self.head(x)  # [B, T, 256]
        
        # Loss hesaplama
        loss = None
        recon_val = None
        
        if labels is not None:
            # Shift: predict next token
            shift_logits = logits[:, :-1, :].contiguous()
            shift_labels = labels[:, 1:].contiguous()
            
            # Cross-entropy loss
            ce_loss = F.cross_entropy(
                shift_logits.view(-1, VOCAB_SIZE),
                shift_labels.view(-1)
            )
            
            loss = ce_loss
            
            if return_seed:
                # Ortalama reconstruction loss (tüm katmanların ortalaması)
                avg_recon = total_recon / N_LAYERS
                recon_val = avg_recon.item()
                # Toplam loss: CE + λ * Recon
                loss = ce_loss + RECON_LAMBDA * avg_recon
        
        return loss, logits, recon_val
    
    @torch.no_grad()
    def generate(self, prompt, max_new_tokens=100, temperature=0.8, top_k=10):
        """
        Autoregressive generation.
        
        Args:
            prompt: string (örn. "ROMEO: ") veya byte list
            max_new_tokens: üretilecek maksimum token
            temperature: sampling sıcaklığı (düşük = daha deterministik)
            top_k: en iyi k token arasından sample
        
        Returns:
            generated_text: string
        """
        self.eval()
        
        # Prompt'u byte tensor'a çevir
        if isinstance(prompt, str):
            if len(prompt) == 0:
                prompt = " "  # Boş prompt yerine space
            input_ids = torch.tensor([[ord(c) for c in prompt]], dtype=torch.long)
        else:
            if len(prompt) == 0:
                prompt = [32]  # space byte
            input_ids = torch.tensor([prompt], dtype=torch.long)
        
        for _ in range(max_new_tokens):
            # Context window'u SEQ_LEN'de tut
            if input_ids.shape[1] > SEQ_LEN:
                input_ids = input_ids[:, -SEQ_LEN:]
            
            # Forward pass
            _, logits, _ = self.forward(input_ids, return_seed=False)
            
            # Son token logits
            next_logits = logits[:, -1, :] / temperature
            
            # Top-k filtering
            if top_k > 0:
                vals, _ = torch.topk(next_logits, top_k, dim=-1)
                threshold = vals[:, -1].unsqueeze(-1)
                next_logits[next_logits < threshold] = float('-inf')
            
            # Sampling
            probs = F.softmax(next_logits, dim=-1)
            probs = probs / probs.sum(dim=-1, keepdim=True)  # renormalize
            next_token = torch.multinomial(probs, num_samples=1)
            
            input_ids = torch.cat([input_ids, next_token], dim=1)
        
        # Byte tensor'ı string'e çevir
        output_bytes = input_ids[0].tolist()
        return bytes(output_bytes).decode('utf-8', errors='replace')
    
    def count_parameters(self):
        """Toplam ve eğitilebilir parametre sayısı."""
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return total, trainable


# ============================================================
# BYTE-LEVEL DATASET (Tiny Shakespeare)
# ============================================================
class ByteDataset(Dataset):
    """
    Byte-level dataset for language modeling.
    
    Her karakter byte'a çevrilir (0-255).
    Sliding window ile sequence'lar oluşturulur.
    """
    
    def __init__(self, data_path=None, seq_len=SEQ_LEN, train=True, split_ratio=0.9):
        """
        Args:
            data_path: .txt dosyası yolu
            seq_len: sequence length
            train: True ise training split, False ise validation
            split_ratio: train/val oranı
        """
        if data_path is None:
            # Varsayılan: repo içindeki dataset
            data_path = os.path.join(os.path.dirname(__file__), '..', 'dataset.txt')
            # Yoksa indir
            if not os.path.exists(data_path):
                self._download_dataset(data_path)
        
        # Dosyayı byte olarak oku
        with open(data_path, 'rb') as f:
            data = list(f.read())
        
        print(f"  Toplam {len(data)} byte okundu")
        
        # Train/val split
        split_idx = int(len(data) * split_ratio)
        data = data[:split_idx] if train else data[split_idx:]
        
        # Sliding window ile örnekler oluştur
        self.examples = []
        for i in range(0, len(data) - seq_len, seq_len):
            chunk = data[i:i + seq_len]
            if len(chunk) == seq_len:
                self.examples.append(torch.tensor(chunk, dtype=torch.long))
        
        print(f"  {len(self.examples)} örnek ({'train' if train else 'val'})")
    
    def _download_dataset(self, path):
        """Tiny Shakespeare dataset'ini indir."""
        import urllib.request
        url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        print(f"  Dataset indiriliyor: {url}")
        urllib.request.urlretrieve(url, path)
        print(f"  Kaydedildi: {path}")
    
    def __len__(self):
        return len(self.examples)
    
    def __getitem__(self, idx):
        return self.examples[idx]


# ============================================================
# EĞİTİM FONKSİYONLARI
# ============================================================
def create_datasets(data_path=None, seq_len=SEQ_LEN):
    """Train ve validation dataset'lerini oluştur."""
    print("Dataset hazırlanıyor...")
    train_ds = ByteDataset(data_path, seq_len, train=True)
    val_ds = ByteDataset(data_path, seq_len, train=False)
    return train_ds, val_ds


def create_model():
    """NanoKVForge modeli oluştur."""
    model = NanoKVForge()
    total, trainable = model.count_parameters()
    print(f"Model: {total:,} parametre ({total/1e3:.1f}K)")
    print(f"  Seed compression: 2×{D_MODEL} / {SEED_DIM} = {2*D_MODEL//SEED_DIM}×")
    return model


def train_step(model, batch, opt):
    """Tek eğitim adımı."""
    opt.zero_grad()
    loss, _, recon = model(batch, labels=batch, return_seed=True)
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    opt.step()
    return loss.item(), recon


@torch.no_grad()
def evaluate(model, val_loader):
    """Validation loss hesapla."""
    model.eval()
    total_loss = 0.0
    total_recon = 0.0
    n = 0
    for batch in val_loader:
        loss, _, recon = model(batch, labels=batch, return_seed=True)
        total_loss += loss.item()
        total_recon += recon if recon else 0.0
        n += 1
    return total_loss / n, total_recon / n


def main():
    """Ana eğitim döngüsü."""
    print("=" * 60)
    print("KVForge NANO — Seed-based KV Cache Training")
    print("=" * 60)
    print(f"  {N_LAYERS}L × {N_HEADS}H × {D_MODEL}D")
    print(f"  Seed Dim: {SEED_DIM} ({2*D_MODEL//SEED_DIM}× compression)")
    print(f"  Seq Len: {SEQ_LEN} | Batch: {BATCH_SIZE} | Epochs: {NUM_EPOCHS}")
    print()
    
    # Dataset
    train_ds, val_ds = create_datasets()
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE)
    print(f"  Train: {len(train_ds)} | Val: {len(val_ds)}")
    print()
    
    # Model
    model = create_model()
    print()
    
    # Optimizer
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * NUM_EPOCHS
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-5)
    print(f"  Optimizer: AdamW (lr={LR}), Scheduler: Cosine ({total_steps} steps)")
    print()
    
    # === EĞİTİM ===
    print("=" * 60)
    print("EĞİTİM BAŞLIYOR")
    print("=" * 60)
    
    t_start = time.time()
    best_loss = float('inf')
    
    for epoch in range(NUM_EPOCHS):
        model.train()
        total_loss = 0.0
        total_recon = 0.0
        n = 0
        
        epoch_start = time.time()
        
        for bidx, batch in enumerate(train_loader):
            loss_val, recon_val = train_step(model, batch, opt)
            scheduler.step()
            
            total_loss += loss_val
            total_recon += recon_val if recon_val else 0.0
            n += 1
            
            if bidx % 10 == 0:
                avg_loss = total_loss / n
                avg_recon = total_recon / n
                avg_ce = avg_loss - RECON_LAMBDA * avg_recon
                ppl = math.exp(min(avg_ce, 20))
                elapsed = time.time() - t_start
                rate = n / (time.time() - epoch_start) if (time.time() - epoch_start) > 0 else 0
                lr = scheduler.get_last_lr()[0]
                
                print(f"E{epoch}|B{bidx:3d}/{len(train_loader)} "
                      f"L={avg_loss:.4f} CE={avg_ce:.4f} "
                      f"R={avg_recon:.5f} PPL={ppl:.1f} "
                      f"LR={lr:.2e} {rate:.2f}s/s")
        
        # Validation
        val_loss, val_recon = evaluate(model, val_loader)
        val_ce = val_loss - RECON_LAMBDA * val_recon
        val_ppl = math.exp(min(val_ce, 20))
        
        epoch_time = time.time() - t_start
        print(f"\n  → Epoch {epoch+1} ({epoch_time:.0f}s): "
              f"Train L={avg_loss:.4f} PPL={ppl:.1f} | "
              f"Val L={val_loss:.4f} PPL={val_ppl:.1f} Recon={val_recon:.5f}")
        
        # Best model kaydet
        if val_loss < best_loss:
            best_loss = val_loss
            save_dir = os.path.join(os.path.dirname(__file__), '..', 'checkpoints')
            os.makedirs(save_dir, exist_ok=True)
            torch.save(model.state_dict(), os.path.join(save_dir, 'nano_best.pt'))
            print(f"  ★ Best model! (loss={val_loss:.4f})")
        
        # Her epoch sonu örnek üretim
        sample = model.generate("ROMEO: ", max_new_tokens=60)
        print(f"\n  Örnek: {sample[:150]}...\n")
    
    total_time = time.time() - t_start
    print("\n" + "=" * 60)
    print(f"EĞİTİM TAMAM — {total_time:.0f}s ({total_time/60:.1f} dk)")
    print(f"Best Val Loss: {best_loss:.4f}")
    print("=" * 60)
    
    return model


if __name__ == "__main__":
    main()
