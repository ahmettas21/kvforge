"""
KVForge NANO v2 — Contextual Seed Compression
==============================================
KVForge v1'den farkı: seed encoder artık sadece o token'ın K,V'sini değil,
bir önceki token'ın K,V'sini de görüyor.

  v1: seed = Encoder(cat(K_i, V_i))           → 2×d_model
  v2: seed = Encoder(cat(K_{i-1}, V_{i-1}, K_i, V_i))  → 4×d_model

Encoder input:  2×d_model → 4×d_model (genişledi)
Seed output:    seed_dim (aynı, 16)
Cache kazancı:  8× (aynı, değişmedi)
Parametre:      ~160K (biraz arttı)

Hedef: contextual bilgi ile PPL düşüşü
       Vanilla=7.1, v1=7.3 → v2 < 7.3
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import math
import time
import os

# ============================================================
# HİPERPARAMETRELER (v1 ile birebir aynı)
# ============================================================
VOCAB_SIZE = 256
D_MODEL = 64
N_HEADS = 4
N_LAYERS = 2
SEQ_LEN = 32
SEED_DIM = 16
BATCH_SIZE = 64
D_FF = 4 * D_MODEL
DROPOUT = 0.1
LR = 3e-3
WEIGHT_DECAY = 0.01
NUM_EPOCHS = 5
RECON_LAMBDA = 0.1


# ============================================================
# CONTEXTUAL SEED ATTENTION — V2
# ============================================================
class ContextualSeedAttention(nn.Module):
    """
    v2: Contextual Seed-based Multi-Head Attention.
    
    v1'den fark:
    - seed_encoder input: 2*d_model → 4*d_model
    - Her token kendi K,V'si + önceki token'ın K,V'sini görür
    - İlk token için sıfır padding kullanılır
    """
    
    def __init__(self):
        super().__init__()
        assert D_MODEL % N_HEADS == 0
        
        self.head_dim = D_MODEL // N_HEADS  # 16
        
        # Standart QKV projeksiyonları (v1 ile aynı)
        self.q_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.k_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.v_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.out_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        
        # === V2: Contextual Seed Compression ===
        # Encoder: cat(K_{i-1}, V_{i-1}, K_i, V_i) → seed
        # 4*d_model = 256 → d_model = 64 → seed_dim = 16
        self.seed_encoder = nn.Sequential(
            nn.Linear(4 * D_MODEL, D_MODEL),  # 256 → 64
            nn.GELU(),
            nn.Linear(D_MODEL, SEED_DIM),     # 64 → 16
        )
        
        # Decoder: seed → K,V (v1 ile aynı, 2*d_model)
        self.seed_decoder = nn.Sequential(
            nn.Linear(SEED_DIM, D_MODEL),     # 16 → 64
            nn.GELU(),
            nn.Linear(D_MODEL, 2 * D_MODEL),  # 64 → 128
        )
        
        self.seed_norm = nn.LayerNorm(SEED_DIM)
    
    def _compress_kv(self, k, v):
        """
        V2 Contextual Compression:
        Her token, kendi K,V'si + bir önceki token'ın K,V'sini kullanır.
        
        v1: cat(K_i, V_i)           → [B, T, 128]
        v2: cat(K_{i-1}, V_{i-1}, K_i, V_i) → [B, T, 256]
        """
        B, T, D = k.shape
        
        # Shift: her pozisyon için bir öncekini al
        # İlk token → sıfır padding
        k_prev = torch.cat([torch.zeros_like(k[:, :1, :]), k[:, :-1, :]], dim=1)
        v_prev = torch.cat([torch.zeros_like(v[:, :1, :]), v[:, :-1, :]], dim=1)
        
        # 4×d_model concat: [K_{i-1}, V_{i-1}, K_i, V_i]
        kv = torch.cat([k_prev, v_prev, k, v], dim=-1)  # [B, T, 256]
        
        return self.seed_norm(self.seed_encoder(kv))
    
    def _split_heads(self, x):
        B, T, _ = x.shape
        return x.view(B, T, N_HEADS, self.head_dim).transpose(1, 2)
    
    def _merge_heads(self, x):
        B, _, T, _ = x.shape
        return x.transpose(1, 2).contiguous().view(B, T, D_MODEL)
    
    def forward(self, x, return_seed=False):
        B, T, _ = x.shape
        
        # 1. Q, K, V projeksiyonları
        q = self.q_proj(x)
        k_orig = self.k_proj(x)
        v_orig = self.v_proj(x)
        
        # 2. V2: Contextual Compression
        # cat(K_{i-1}, V_{i-1}, K_i, V_i) → seed
        seed = self._compress_kv(k_orig, v_orig)      # [B, T, 16]
        
        # 3. Seed → KV Reconstruction
        kv_recon = self.seed_decoder(seed)             # [B, T, 128]
        k, v = kv_recon.chunk(2, dim=-1)               # [B, T, 64], [B, T, 64]
        
        # 4. Multi-Head Attention
        q = self._split_heads(q)
        k = self._split_heads(k)
        v = self._split_heads(v)
        
        scale = 1.0 / math.sqrt(self.head_dim)
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * scale
        
        # Causal mask
        causal_mask = torch.triu(
            torch.ones(T, T, device=x.device), diagonal=1
        ).bool()
        attn_weights = attn_weights.masked_fill(
            causal_mask.unsqueeze(0).unsqueeze(0), float('-inf')
        )
        
        attn_weights = F.softmax(attn_weights, dim=-1)
        attn_output = torch.matmul(attn_weights, v)
        attn_output = self._merge_heads(attn_output)
        
        output = self.out_proj(attn_output)
        
        if return_seed:
            # Reconstruction Loss
            kv_concat = torch.cat([k_orig, v_orig], dim=-1)
            recon_loss = F.mse_loss(kv_recon, kv_concat.detach())
            return output, seed, recon_loss
        
        return output


# ============================================================
# V2 NANO TRANSFORMER (v1 ile aynı mimari, farklı attention)
# ============================================================
class NanoKVForgeV2(nn.Module):
    """
    Byte-level Seed-based Transformer — V2 Contextual.
    v1'den tek fark: ContextualSeedAttention kullanması.
    """
    
    def __init__(self):
        super().__init__()
        
        self.token_embed = nn.Embedding(VOCAB_SIZE, D_MODEL)
        self.pos_embed = nn.Embedding(SEQ_LEN, D_MODEL)
        
        self.blocks = nn.ModuleList()
        for _ in range(N_LAYERS):
            block = nn.ModuleDict({
                'ln1': nn.LayerNorm(D_MODEL),
                'attn': ContextualSeedAttention(),  # <-- V2
                'ln2': nn.LayerNorm(D_MODEL),
                'mlp': nn.Sequential(
                    nn.Linear(D_MODEL, D_FF),
                    nn.GELU(),
                    nn.Dropout(DROPOUT),
                    nn.Linear(D_FF, D_MODEL),
                    nn.Dropout(DROPOUT),
                ),
            })
            self.blocks.append(block)
        
        self.ln_f = nn.LayerNorm(D_MODEL)
        self.head = nn.Linear(D_MODEL, VOCAB_SIZE, bias=False)
        self.token_embed.weight = self.head.weight  # weight tying
        
        self._init_weights()
    
    def _init_weights(self):
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
        B, T = input_ids.shape
        assert T <= SEQ_LEN
        
        x = self.token_embed(input_ids) + \
            self.pos_embed(torch.arange(T, device=input_ids.device).unsqueeze(0))
        
        total_recon = 0.0
        for block in self.blocks:
            residual = x
            x = block['ln1'](x)
            if return_seed:
                attn_out, seed, recon = block['attn'](x, return_seed=True)
                total_recon += recon
            else:
                attn_out = block['attn'](x, return_seed=False)
            x = residual + attn_out
            
            residual = x
            x = residual + block['mlp'](block['ln2'](x))
        
        x = self.ln_f(x)
        logits = self.head(x)
        
        loss = None
        recon_val = None
        
        if labels is not None:
            shift_logits = logits[:, :-1, :].contiguous()
            shift_labels = labels[:, 1:].contiguous()
            ce_loss = F.cross_entropy(
                shift_logits.view(-1, VOCAB_SIZE),
                shift_labels.view(-1)
            )
            loss = ce_loss
            if return_seed:
                avg_recon = total_recon / N_LAYERS
                recon_val = avg_recon.item()
                loss = ce_loss + RECON_LAMBDA * avg_recon
        
        return loss, logits, recon_val
    
    @torch.no_grad()
    def generate(self, prompt, max_new_tokens=100, temperature=0.8, top_k=10):
        self.eval()
        
        if isinstance(prompt, str):
            if len(prompt) == 0:
                prompt = " "
            input_ids = torch.tensor([[ord(c) for c in prompt]], dtype=torch.long)
        else:
            if len(prompt) == 0:
                prompt = [32]
            input_ids = torch.tensor([prompt], dtype=torch.long)
        
        for _ in range(max_new_tokens):
            if input_ids.shape[1] > SEQ_LEN:
                input_ids = input_ids[:, -SEQ_LEN:]
            
            _, logits, _ = self.forward(input_ids, return_seed=False)
            
            next_logits = logits[:, -1, :] / temperature
            if top_k > 0:
                vals, _ = torch.topk(next_logits, top_k, dim=-1)
                next_logits[next_logits < vals[:, -1:]] = float('-inf')
            
            probs = F.softmax(next_logits, dim=-1)
            probs = probs / probs.sum(dim=-1, keepdim=True)
            next_token = torch.multinomial(probs, num_samples=1)
            input_ids = torch.cat([input_ids, next_token], dim=1)
        
        output_bytes = input_ids[0].tolist()
        return bytes(output_bytes).decode('utf-8', errors='replace')
    
    def count_parameters(self):
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return total, trainable


# ============================================================
# DATASET (v1 ile aynı)
# ============================================================
class ByteDataset(Dataset):
    def __init__(self, data_path=None, seq_len=SEQ_LEN, train=True, split_ratio=0.9):
        if data_path is None:
            data_path = os.path.join(os.path.dirname(__file__), '..', 'dataset.txt')
            if not os.path.exists(data_path):
                self._download_dataset(data_path)
        
        with open(data_path, 'rb') as f:
            data = list(f.read())
        
        split_idx = int(len(data) * split_ratio)
        data = data[:split_idx] if train else data[split_idx:]
        
        self.examples = []
        for i in range(0, len(data) - seq_len, seq_len):
            chunk = data[i:i + seq_len]
            if len(chunk) == seq_len:
                self.examples.append(torch.tensor(chunk, dtype=torch.long))
    
    def _download_dataset(self, path):
        import urllib.request
        url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        urllib.request.urlretrieve(url, path)
    
    def __len__(self):
        return len(self.examples)
    
    def __getitem__(self, idx):
        return self.examples[idx]


# ============================================================
# EĞİTİM
# ============================================================
def create_datasets(data_path=None, seq_len=SEQ_LEN):
    train_ds = ByteDataset(data_path, seq_len, train=True)
    val_ds = ByteDataset(data_path, seq_len, train=False)
    return train_ds, val_ds


def main():
    print("=" * 60)
    print("KVForge v2 — Contextual Seed Compression")
    print("=" * 60)
    print(f"  {N_LAYERS}L × {N_HEADS}H × {D_MODEL}D")
    print(f"  Seed Dim: {SEED_DIM} (8× compression)")
    print(f"  Encoder input: 4×d_model = {4*D_MODEL} (contextual)")
    print(f"  Seq Len: {SEQ_LEN} | Batch: {BATCH_SIZE} | Epochs: {NUM_EPOCHS}")
    print()
    
    # Dataset
    train_ds, val_ds = create_datasets()
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE)
    print(f"  Train: {len(train_ds)} | Val: {len(val_ds)}")
    print()
    
    # Model
    model = NanoKVForgeV2()
    total, trainable = model.count_parameters()
    print(f"Model: {total:,} parametre ({total/1e3:.1f}K)")
    print(f"  v1'den fark: +{total - 155488} parametre (contextual encoder)")
    print()
    
    # Optimizer
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * NUM_EPOCHS
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-5)
    
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
        
        for bidx, batch in enumerate(train_loader):
            opt.zero_grad()
            loss, _, recon = model(batch, labels=batch, return_seed=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            opt.step()
            scheduler.step()
            
            total_loss += loss.item()
            total_recon += recon if recon else 0.0
            n += 1
            
            if bidx % 10 == 0:
                avg_loss = total_loss / n
                avg_recon = total_recon / n
                ce_est = avg_loss - RECON_LAMBDA * avg_recon
                ppl = math.exp(min(ce_est, 20))
                print(f"E{epoch}|B{bidx:3d}/{len(train_loader)} "
                      f"L={avg_loss:.4f} CE={ce_est:.4f} "
                      f"R={avg_recon:.5f} PPL={ppl:.1f}")
        
        # Validation
        model.eval()
        val_loss = 0.0
        val_recon = 0.0
        for batch in val_loader:
            l, _, r = model(batch, labels=batch, return_seed=True)
            val_loss += l.item()
            val_recon += r if r else 0.0
        val_loss /= len(val_loader)
        val_recon /= len(val_loader)
        val_ce_only = val_loss - RECON_LAMBDA * val_recon
        val_ppl = math.exp(min(val_ce_only, 20))
        
        epoch_time = time.time() - t_start
        print(f"\n  → Epoch {epoch+1} ({epoch_time:.0f}s): "
              f"Val L={val_loss:.4f} (CE={val_ce_only:.4f}) "
              f"PPL={val_ppl:.1f} Recon={val_recon:.5f}")
        
        if val_loss < best_loss:
            best_loss = val_loss
            save_dir = os.path.join(os.path.dirname(__file__), '..', 'checkpoints')
            os.makedirs(save_dir, exist_ok=True)
            torch.save(model.state_dict(), os.path.join(save_dir, 'v2_best.pt'))
            print(f"  ★ Best model! (loss={val_loss:.4f})")
    
    total_time = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"EĞİTİM TAMAM — {total_time:.0f}s ({total_time/60:.1f} dk)")
    print(f"Best Val Loss: {best_loss:.4f}")
    print(f"Best Val PPL:  {math.exp(min(best_loss, 20)):.1f}")
    print(f"{'='*60}")
    
    return model


if __name__ == "__main__":
    main()
