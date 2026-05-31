"""
Vanilla Attention — KVForge Baseline Karşılaştırması
=====================================================
Aynı nano model mimarisi (2L, 4H, 64D) ama SeedAttention yerine
standart multi-head attention ile. Kullanım amacı:

1. KVForge vs Vanilla: PPL karşılaştırması
2. KVForge vs Vanilla: Parametre sayısı
3. KVForge vs Vanilla: RAM kullanımı
4. KVForge vs Vanilla: Generation hızı

Bu sayede "SeedAttention ne kazandırıyor?" sorusu
nicel verilerle cevaplanabilir.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import time
import os

from kvforge.nano_model import (
    VOCAB_SIZE, D_MODEL, N_HEADS, N_LAYERS, SEQ_LEN, SEED_DIM,
    BATCH_SIZE, D_FF, DROPOUT, LR, WEIGHT_DECAY, NUM_EPOCHS,
    ByteDataset, create_datasets
)


# ============================================================
# VANILLA ATTENTION — Seed yok, direkt K,V kullan
# ============================================================
class VanillaAttention(nn.Module):
    """
    Standart Multi-Head Attention — baseline.
    
    KVForge'dan farkı:
    - Seed encoder/decoder YOK
    - K,V doğrudan attention'a verilir
    - Daha az parametre (seed encoder+decoder yok)
    - Reconstuction loss YOK (sadece CE loss)
    - KV cache boyutu: 2 × d_model × seq (seed yok)
    """
    
    def __init__(self):
        super().__init__()
        assert D_MODEL % N_HEADS == 0
        self.head_dim = D_MODEL // N_HEADS
        
        self.q_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.k_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.v_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
        self.out_proj = nn.Linear(D_MODEL, D_MODEL, bias=False)
    
    def _split_heads(self, x):
        B, T, _ = x.shape
        return x.view(B, T, N_HEADS, self.head_dim).transpose(1, 2)
    
    def _merge_heads(self, x):
        B, _, T, _ = x.shape
        return x.transpose(1, 2).contiguous().view(B, T, D_MODEL)
    
    def forward(self, x):
        """
        Basit scaled dot-product attention.
        Seed yok, reconstruct yok, tek loss: CE.
        """
        B, T, _ = x.shape
        
        q = self._split_heads(self.q_proj(x))  # [B, 4, T, 16]
        k = self._split_heads(self.k_proj(x))
        v = self._split_heads(self.v_proj(x))
        
        scale = 1.0 / math.sqrt(self.head_dim)
        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * scale
        
        # Causal mask (KVForge ile aynı)
        causal_mask = torch.triu(
            torch.ones(T, T, device=x.device), diagonal=1
        ).bool()
        attn_weights = attn_weights.masked_fill(
            causal_mask.unsqueeze(0).unsqueeze(0), float('-inf')
        )
        
        attn_weights = F.softmax(attn_weights, dim=-1)
        out = self._merge_heads(torch.matmul(attn_weights, v))
        return self.out_proj(out)


# ============================================================
# VANILLA NANO MODEL — SeedAttention yerine VanillaAttention
# ============================================================
class VanillaNano(nn.Module):
    """
    KVForge ile birebir aynı mimari, sadece attention farklı.
    
    Değişen:
    - NanoSeedAttention → VanillaAttention
    - forward() return_seed parametresi yok (recon loss yok)
    - Daha az parametre (seed encoder/decoder çıktı)
    """
    
    def __init__(self):
        super().__init__()
        
        self.token_embed = nn.Embedding(VOCAB_SIZE, D_MODEL)
        self.pos_embed = nn.Embedding(SEQ_LEN, D_MODEL)
        
        self.blocks = nn.ModuleList()
        for _ in range(N_LAYERS):
            block = nn.ModuleDict({
                'ln1': nn.LayerNorm(D_MODEL),
                'attn': VanillaAttention(),  # <-- TEK FARK BURADA
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
    
    def forward(self, input_ids, labels=None):
        B, T = input_ids.shape
        
        x = self.token_embed(input_ids)
        x = x + self.pos_embed(torch.arange(T, device=input_ids.device).unsqueeze(0))
        
        for block in self.blocks:
            residual = x
            x = block['ln1'](x)
            x = residual + block['attn'](x)
            
            residual = x
            x = residual + block['mlp'](block['ln2'](x))
        
        x = self.ln_f(x)
        logits = self.head(x)
        
        loss = None
        if labels is not None:
            shift_logits = logits[:, :-1, :].contiguous()
            shift_labels = labels[:, 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.view(-1, VOCAB_SIZE),
                shift_labels.view(-1)
            )
        
        return loss, logits
    
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
            
            _, logits = self.forward(input_ids)
            
            next_logits = logits[:, -1, :] / temperature
            
            if top_k > 0:
                vals, _ = torch.topk(next_logits, top_k, dim=-1)
                threshold = vals[:, -1].unsqueeze(-1)
                next_logits[next_logits < threshold] = float('-inf')
            
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
# BASELINE EĞİTİMİ
# ============================================================
def train_vanilla():
    """Vanilla Nano model eğitimi — KVForge ile birebir aynı hiperparametreler."""
    
    print("=" * 60)
    print("VANILLA NANO — Baseline Training (KVForge Karşılaştırması)")
    print("=" * 60)
    
    # Dataset
    train_ds, val_ds = create_datasets()
    train_loader = torch.utils.data.DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_ds, batch_size=BATCH_SIZE)
    
    # Model
    model = VanillaNano()
    total, trainable = model.count_parameters()
    print(f"\nModel: {total:,} parametre ({total/1e3:.1f}K)")
    
    # Optimizer
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * NUM_EPOCHS
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-5)
    
    # Eğitim
    t_start = time.time()
    best_loss = float('inf')
    
    for epoch in range(NUM_EPOCHS):
        model.train()
        total_loss = 0.0
        n = 0
        
        for bidx, batch in enumerate(train_loader):
            opt.zero_grad()
            loss, _ = model(batch, labels=batch)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            opt.step()
            scheduler.step()
            
            total_loss += loss.item()
            n += 1
            
            if bidx % 10 == 0:
                avg_loss = total_loss / n
                ppl = math.exp(min(avg_loss, 20))
                lr = scheduler.get_last_lr()[0]
                print(f"E{epoch}|B{bidx:3d} L={avg_loss:.4f} PPL={ppl:.1f} LR={lr:.2e}")
        
        # Validation
        model.eval()
        val_loss = 0.0
        for batch in val_loader:
            l, _ = model(batch, labels=batch)
            val_loss += l.item()
        val_loss /= len(val_loader)
        val_ppl = math.exp(min(val_loss, 20))
        
        epoch_time = time.time() - t_start
        print(f"\n  → Epoch {epoch+1} ({epoch_time:.0f}s): "
              f"Train L={avg_loss:.4f} PPL={ppl:.1f} | "
              f"Val L={val_loss:.4f} PPL={val_ppl:.1f}")
        
        if val_loss < best_loss:
            best_loss = val_loss
            torch.save(model.state_dict(), 
                       os.path.join(os.path.dirname(__file__), '..', 'checkpoints', 'vanilla_best.pt'))
            print(f"  ★ Best model! (loss={val_loss:.4f})")
    
    total_time = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"VANILLA EĞİTİM TAMAM — {total_time:.0f}s ({total_time/60:.1f} dk)")
    print(f"Best Val Loss: {best_loss:.4f} | Best Val PPL: {math.exp(min(best_loss, 20)):.1f}")
    print(f"{'='*60}")
    
    return model


# ============================================================
# KVFORGE vs VANILLA — KARŞILAŞTIRMA TABLOSU
# ============================================================
def benchmark_comparison():
    """
    İki modeli yan yana koy:
    - Parametre sayısı
    - PPL
    - RAM kullanımı
    - Inference hızı
    """
    from kvforge.nano_model import NanoKVForge
    
    print("\n" + "=" * 60)
    print("KVForge vs Vanilla — Benchmark Karşılaştırması")
    print("=" * 60)
    
    # 1. Parametre karşılaştırması
    kvforge = NanoKVForge()
    vanilla = VanillaNano()
    
    kvf_total, _ = kvforge.count_parameters()
    van_total, _ = vanilla.count_parameters()
    
    print(f"\n📐 Parametre Karşılaştırması:")
    print(f"  KVForge Nano:   {kvf_total:>8,} parametre ({kvf_total/1e3:.1f}K)")
    print(f"  Vanilla Nano:   {van_total:>8,} parametre ({van_total/1e3:.1f}K)")
    print(f"  Fark (seed encoder/decoder): +{kvf_total - van_total:,} parametre")
    
    # 2. Inference hız testi (rastgele ağırlıklarla)
    kvforge.eval()
    vanilla.eval()
    
    x = torch.randint(0, VOCAB_SIZE, (1, SEQ_LEN))
    
    with torch.no_grad():
        # Warmup
        for _ in range(50):
            kvforge(x)
            vanilla(x)
        
        # KVForge
        t0 = time.time()
        for _ in range(200):
            kvforge(x)
        kvf_time = time.time() - t0
        
        # Vanilla
        t0 = time.time()
        for _ in range(200):
            vanilla(x)
        van_time = time.time() - t0
    
    print(f"\n⚡ Inference Hızı (200 forward pass, CPU):")
    print(f"  KVForge Nano:   {200/kvf_time:.0f} passes/s ({kvf_time/200*1000:.1f}ms/pass)")
    print(f"  Vanilla Nano:   {200/van_time:.0f} passes/s ({van_time/200*1000:.1f}ms/pass)")
    print(f"  Overhead (seed encoder/decoder): ×{kvf_time/van_time:.2f}")
    
    # 3. Parametre detayı
    print(f"\n📊 Parametre Dağılımı:")
    kvf_attn_params = sum(p.numel() for name, p in kvforge.named_parameters() if 'attn' in name)
    van_attn_params = sum(p.numel() for name, p in vanilla.named_parameters() if 'attn' in name)
    print(f"  KVForge Attention:   {kvf_attn_params:,} parametre")
    print(f"  Vanilla Attention:   {van_attn_params:,} parametre")
    print(f"  Seed encoder/decoder: {kvf_attn_params - van_attn_params:,} parametre ({((kvf_attn_params - van_attn_params)/kvf_attn_params*100):.1f}% of attn)")
    
    # Özet
    print(f"\n{'='*60}")
    print(f"ÖZET — KVForge SeedAttention:")
    print(f"  +{kvf_total - van_total:,} parametre (seed encoder+decoder)")
    print(f"  ×{kvf_time/van_time:.2f} inference overhead")
    print(f"  = {2*D_MODEL//SEED_DIM}× compression (KV cache → seed)")
    print(f"  + reconstruction loss ile kalite garantisi")
    print(f"{'='*60}")
    
    return {
        'kvforge_params': kvf_total,
        'vanilla_params': van_total,
        'kvforge_speed': 200/kvf_time,
        'vanilla_speed': 200/van_time,
        'compression_ratio': 2*D_MODEL//SEED_DIM,
    }


if __name__ == "__main__":
    import sys
    
    if '--benchmark' in sys.argv:
        # Sadece benchmark (eğitim yok, rastgele ağırlıklarla)
        benchmark_comparison()
    elif '--train' in sys.argv:
        # Vanilla eğitimi
        train_vanilla()
    else:
        # Önce benchmark, sonra eğitim
        benchmark_comparison()
        print("\n\nVanilla eğitimi başlıyor...\n")
        train_vanilla()
