"""
KVForge Full Model — GPT2-small tabanlı Seed Attention
=======================================================
12 katman, 12 head, 768 embedding, 153M parametre.

Bu model, HuggingFace GPT2 konfigürasyonunu kullanır ancak
standart attention'ı SeedAttention ile değiştirir.

Kullanım:
    python -m kvforge.full_model          # test forward
    python -m kvforge.full_model --train   # eğitim (GPU önerilir)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import os


# ============================================================
# FULL SEED ATTENTION (GPT2-small boyutunda)
# ============================================================
class SeedAttention(nn.Module):
    """
    Full-scale Seed-based Multi-Head Attention.
    
    GPT2-small konfigürasyonu:
        d_model = 768, n_heads = 12, head_dim = 64
        seed_dim = 64 → 24× compression (2*768/64 = 24)
    """
    
    def __init__(self, d_model=768, n_heads=12, seed_dim=64, dropout=0.1):
        super().__init__()
        assert d_model % n_heads == 0
        
        self.d_model = d_model
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.seed_dim = seed_dim
        
        # Standart QKV projeksiyonları
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        
        # KVForge: Seed Compression
        # Encoder: 2*d_model → d_model → seed_dim
        self.seed_encoder = nn.Sequential(
            nn.Linear(2 * d_model, d_model),
            nn.GELU(),
            nn.Linear(d_model, seed_dim),
        )
        
        # Decoder: seed_dim → d_model → 2*d_model
        self.seed_decoder = nn.Sequential(
            nn.Linear(seed_dim, d_model),
            nn.GELU(),
            nn.Linear(d_model, 2 * d_model),
        )
        
        self.seed_norm = nn.LayerNorm(seed_dim)
        self.dropout = nn.Dropout(dropout)
        
        # Generation cache
        self.seed_cache = None
    
    def _split_heads(self, x):
        """[B, T, d] → [B, n_heads, T, head_dim]"""
        B, T, _ = x.shape
        x = x.view(B, T, self.n_heads, self.head_dim)
        return x.transpose(1, 2)
    
    def _merge_heads(self, x):
        """[B, n_heads, T, head_dim] → [B, T, d]"""
        B, _, T, _ = x.shape
        x = x.transpose(1, 2).contiguous()
        return x.view(B, T, self.d_model)
    
    def compress_kv(self, k, v):
        """K,V → seed (compression)."""
        kv = torch.cat([k, v], dim=-1)
        return self.seed_norm(self.seed_encoder(kv))
    
    def reconstruct_kv(self, seed):
        """Seed → K',V' (reconstruction)."""
        kv = self.seed_decoder(seed)
        return kv.chunk(2, dim=-1)
    
    def forward(self, x, return_seed=False, use_cache=False):
        B, T, _ = x.shape
        
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)
        
        # Seed compression
        seed = self.compress_kv(k, v)
        
        if use_cache and self.seed_cache is not None:
            # Generation: seed cache kullan
            self.seed_cache = torch.cat([self.seed_cache, seed], dim=1)
            k, v = self.reconstruct_kv(self.seed_cache)
            q = q[:, -1:, :]  # sadece son token
        else:
            # Training: her adımda yeniden üret
            k, v = self.reconstruct_kv(seed)
        
        # Multi-head attention
        q, k, v = self._split_heads(q), self._split_heads(k), self._split_heads(v)
        scale = 1.0 / math.sqrt(self.head_dim)
        attn = F.softmax(torch.matmul(q, k.transpose(-2, -1)) * scale, dim=-1)
        attn = self.dropout(attn)
        out = self._merge_heads(torch.matmul(attn, v))
        out = self.out_proj(out)
        
        if return_seed:
            k_orig, v_orig = self.k_proj(x), self.v_proj(x)
            kv_orig = torch.cat([k_orig, v_orig], dim=-1)
            kv_recon = self.seed_decoder(seed)
            recon_loss = F.mse_loss(kv_recon, kv_orig.detach())
            return out, seed, recon_loss
        
        return out
    
    def reset_cache(self):
        """Generation cache'ini sıfırla."""
        self.seed_cache = None


# ============================================================
# FULL TRANSFORMER BLOCK
# ============================================================
class KVForgeBlock(nn.Module):
    """Single transformer block with SeedAttention."""
    
    def __init__(self, d_model=768, n_heads=12, seed_dim=64, d_ff=3072, dropout=0.1):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = SeedAttention(d_model, n_heads, seed_dim, dropout)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
            nn.Dropout(dropout),
        )
    
    def forward(self, x, return_seed=False, use_cache=False):
        # Attention
        residual = x
        x = self.ln1(x)
        if return_seed:
            attn_out, seed, recon = self.attn(x, return_seed=True, use_cache=use_cache)
        else:
            attn_out = self.attn(x, use_cache=use_cache)
            recon = None
        x = residual + attn_out
        
        # MLP
        residual = x
        x = residual + self.mlp(self.ln2(x))
        
        if return_seed:
            return x, seed, recon
        return x


# ============================================================
# FULL MODEL
# ============================================================
class KVForgeModel(nn.Module):
    """
    Full-scale KVForge model (GPT2-small boyutunda).
    
    12 layers, 12 heads, 768 hidden → 153M parameters.
    """
    
    def __init__(self, vocab_size=50257, d_model=768, n_heads=12,
                 n_layers=12, seed_dim=64, max_seq_len=1024, dropout=0.1):
        super().__init__()
        
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(max_seq_len, d_model)
        self.dropout = nn.Dropout(dropout)
        
        self.blocks = nn.ModuleList([
            KVForgeBlock(d_model, n_heads, seed_dim, 4*d_model, dropout)
            for _ in range(n_layers)
        ])
        
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)
        self.token_embed.weight = self.head.weight  # weight tying
        
        self.max_seq_len = max_seq_len
        self.recon_lambda = 0.1
        
        self._init_weights()
    
    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0.0, 0.02)
                if m.bias is not None: nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Embedding):
                nn.init.normal_(m.weight, 0.0, 0.02)
            elif isinstance(m, nn.LayerNorm):
                nn.init.ones_(m.weight); nn.init.zeros_(m.bias)
    
    def forward(self, input_ids, labels=None, return_seed=False, use_cache=False):
        B, T = input_ids.shape
        
        x = self.token_embed(input_ids)
        x = x + self.pos_embed(torch.arange(T, device=input_ids.device).unsqueeze(0))
        x = self.dropout(x)
        
        total_recon = 0.0
        for block in self.blocks:
            if return_seed:
                x, _, recon = block(x, return_seed=True, use_cache=use_cache)
                total_recon += recon
            else:
                x = block(x, use_cache=use_cache)
        
        x = self.ln_f(x)
        logits = self.head(x)
        
        loss = None
        recon_val = None
        
        if labels is not None:
            shift_logits = logits[:, :-1, :].contiguous()
            shift_labels = labels[:, 1:].contiguous()
            ce_loss = F.cross_entropy(
                shift_logits.view(-1, shift_logits.size(-1)),
                shift_labels.view(-1),
                ignore_index=-100
            )
            loss = ce_loss
            if return_seed:
                avg_recon = total_recon / len(self.blocks)
                recon_val = avg_recon.item()
                loss = ce_loss + self.recon_lambda * avg_recon
        
        return loss, logits, recon_val
    
    @torch.no_grad()
    def generate(self, input_ids, max_new=50, temperature=1.0, top_k=50):
        self.eval()
        for block in self.blocks:
            block.attn.reset_cache()
        
        for _ in range(max_new):
            loss, logits, _ = self.forward(input_ids, use_cache=True)
            next_logits = logits[:, -1, :] / temperature
            
            if top_k > 0:
                vals, _ = torch.topk(next_logits, top_k)
                next_logits[next_logits < vals[:, -1:]] = float('-inf')
            
            probs = F.softmax(next_logits, dim=-1)
            next_token = torch.multinomial(probs, 1)
            input_ids = torch.cat([input_ids, next_token], dim=1)
        
        return input_ids
    
    def count_parameters(self):
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return total, trainable


# ============================================================
# TEST
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("KVForge Full Model Test")
    print("=" * 60)
    
    # Model test
    model = KVForgeModel()
    total, trainable = model.count_parameters()
    print(f"Model: {total/1e6:.1f}M total, {trainable/1e6:.1f}M trainable")
    print(f"  Seed compression: 24× (2*768/64 = 24)")
    
    # Forward test
    x = torch.randint(0, 1000, (2, 64))
    loss, logits, recon = model(x, labels=x, return_seed=True)
    print(f"\nForward test:")
    print(f"  Input: {x.shape}")
    print(f"  Logits: {logits.shape}")
    print(f"  Loss: {loss.item():.4f}")
    print(f"  Recon Loss: {recon}")
    
    print("\nTest OK. Model hazır.")
