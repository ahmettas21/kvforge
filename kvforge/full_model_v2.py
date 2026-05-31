#!/usr/bin/env python3
"""
KVForge v2 — Full-scale Transformer with Contextual Seed Attention
==================================================================
GPT2-small boyutunda model.
12 layers, 12 heads, 768 hidden → ~153M parameters.
Seed compression: 24× (2*768/64) contextual v2.

CoTo (Come Together, ICML 2025) destegi:
    model.add_lora(rank=8) -> LoRA adapter'larini ekler
    model.coto_adapters -> CoToController tarafindan kullanilir
"""

import math
import torch
import torch.nn as nn
import torch.nn.functional as F

from kvforge.coto_adapter import CoToAdapterWrapper


# ============================================================
# CONTEXTUAL SEED ATTENTION (v2)
# ============================================================
class ContextualSeedAttention(nn.Module):
    """
    Contextual seed → attention head selection.
    
    v2 degisiklikleri:
    - Seed encoder: [q; k; v; out] * W_enc + highway + residual
    - Seed decoder: (single query seed → head coefficient) × 24 compression
    - 3 seed → 4-step temporal encoding
    - Layer-specific priors (uniform)
    """
    
    def __init__(self, d_model=768, n_heads=12, seed_dim=64, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.seed_dim = seed_dim
        self.head_dim = d_model // n_heads
        
        # Standart QKV projeksiyonlari
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)
        
        # Seed encoder: [q; k; v; out] → seed_dim
        self.seed_encoder = nn.Sequential(
            nn.Linear(4 * d_model, 2 * d_model),  # 3072 → 1536
            nn.GELU(),
            nn.Linear(2 * d_model, 2 * d_model),  # 1536 → 1536
            nn.GELU(),
            nn.Linear(2 * d_model, 4 * d_model),  # 1536 → 3072
            nn.GELU(),
            nn.Linear(4 * d_model, 2 * d_model),  # 3072 → 1536
            nn.GELU(),
            nn.Linear(2 * d_model, d_model),      # 1536 → 768
            nn.GELU(),
            nn.Linear(d_model, seed_dim),          # 768 → 64
        )
        
        # Seed decoder: seed_dim → head coefficients
        self.seed_decoder = nn.Sequential(
            nn.Linear(seed_dim, d_model),          # 64 → 768
            nn.GELU(),
            nn.Linear(d_model, 2 * d_model),       # 768 → 1536
            nn.GELU(),
            nn.Linear(2 * d_model, d_model),       # 1536 → 768
        )
        
        # Seed dropout
        self.seed_dropout = nn.Dropout(0.1)
        
        # Temporal encoding (3 seed → 4-step)
        self.temporal_proj = nn.Linear(seed_dim * 3, seed_dim * 4)
        
        # Layer-specific priors (initialised as uniform)
        self.log_prior = nn.Parameter(torch.zeros(n_heads))
    
    def forward(self, x, return_seed=False, use_cache=False):
        B, T, D = x.shape
        
        q = self.q_proj(x)
        k_orig = self.k_proj(x)
        v_orig = self.v_proj(x)
        
        # Standart attention
        k = k_orig.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        v = v_orig.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        q_std = q.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        
        attn = (q_std @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        attn = F.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        out = (attn @ v).transpose(1, 2).contiguous().view(B, T, D)
        out = self.out_proj(out)
        
        # Seed encoder: [q; k; v; out] → seed
        seed_input = torch.cat([q, k_orig, v_orig, out], dim=-1)
        seed = self.seed_encoder(seed_input)  # (B, T, seed_dim)
        seed = self.seed_dropout(seed)
        
        # Seed decoder → head coefficients
        head_coeffs = self.seed_decoder(seed)  # (B, T, d_model)
        head_coeffs = head_coeffs.view(B, T, self.n_heads, self.head_dim)
        head_coeffs = head_coeffs.mean(dim=-1)  # (B, T, n_heads)
        
        # Layer prior
        prior = F.softmax(self.log_prior, dim=-1)
        head_coeffs = head_coeffs + prior.unsqueeze(0).unsqueeze(0)
        head_coeffs = F.softmax(head_coeffs, dim=-1)
        
        # Seeded output: weighted head aggregation
        # head_coeffs: (B, T, n_heads) -> (B, n_heads, T, 1)
        # q_std: (B, n_heads, T, head_dim)
        head_coeffs_expanded = head_coeffs.transpose(1, 2).unsqueeze(-1)  # (B, n_heads, T, 1)
        seeded_out = (q_std * head_coeffs_expanded).transpose(1, 2).contiguous().view(B, T, D)
        
        # Reconstruction: seed → multi-step temporal
        if return_seed:
            # 3 consecutive seeds → 4-step temporal
            if T >= 3:
                seed_triplet = torch.stack([
                    seed[:, :-2, :],
                    seed[:, 1:-1, :],
                    seed[:, 2:, :]
                ], dim=-2)  # (B, T-2, 3, seed_dim)
                temporal = self.temporal_proj(
                    seed_triplet.view(B, T-2, 3 * self.seed_dim)
                )  # (B, T-2, 4*self.seed_dim)
                recon = temporal.norm(dim=-1).mean()
            else:
                recon = seed.norm(dim=-1).mean()
        else:
            recon = None
        
        output = out + seeded_out
        
        if return_seed:
            return output, seed, recon
        return output


# ============================================================
# V2 FULL TRANSFORMER BLOCK
# ============================================================
class KVForgeBlockV2(nn.Module):
    """Transformer block with ContextualSeedAttention."""
    
    def __init__(self, d_model=768, n_heads=12, seed_dim=64, d_ff=3072, dropout=0.1):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = ContextualSeedAttention(d_model, n_heads, seed_dim, dropout)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_ff),   # fc_in
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),   # fc_out
            nn.Dropout(dropout),
        )
    
    def forward(self, x, return_seed=False, use_cache=False):
        residual = x
        x = self.ln1(x)
        if return_seed:
            attn_out, seed, recon = self.attn(x, return_seed=True, use_cache=use_cache)
        else:
            attn_out = self.attn(x, use_cache=use_cache)
            recon = None
        x = residual + attn_out
        
        residual = x
        x = residual + self.mlp(self.ln2(x))
        
        if return_seed:
            return x, seed, recon
        return x


# ============================================================
# V2 FULL MODEL (GPT2-small)
# ============================================================
class KVForgeModelV2(nn.Module):
    """
    Full-scale KVForge v2 model (GPT2-small boyutunda).
    12 layers, 12 heads, 768 hidden → ~153M parameters.
    """
    
    def __init__(self, vocab_size=50257, d_model=768, n_heads=12,
                 n_layers=12, seed_dim=64, max_seq_len=1024, dropout=0.1):
        super().__init__()
        
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(max_seq_len, d_model)
        self.dropout = nn.Dropout(dropout)
        
        self.blocks = nn.ModuleList([
            KVForgeBlockV2(d_model, n_heads, seed_dim, 4*d_model, dropout)
            for _ in range(n_layers)
        ])
        
        self.ln_f = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)
        self.token_embed.weight = self.head.weight  # weight tying
        
        self.max_seq_len = max_seq_len
        self.recon_lambda = 0.1
        
        # CoTo Adapter registry (opsiyonel, add_lora() ile doldurulur)
        self.coto_adapters = []
        
        self._init_weights()
    
    def add_lora(self, rank=8, alpha=16.0, target_modules=None):
        """
        Modeldeki Linear katmanlara LoRA adapter'lari ekler.
        Her adapter icin CoToAdapterWrapper olusturup kaydeder.
        
        Args:
            rank: LoRA rank (default: 8)
            alpha: LoRA alpha (default: 16.0)
            target_modules: Hangi modullere LoRA eklenecegi.
                           None = q_proj, k_proj, v_proj, out_proj, fc_in, fc_out
        Returns:
            list of CoToAdapterWrapper
        """
        if target_modules is None:
            target_suffixes = ("q_proj", "k_proj", "v_proj", "out_proj", "fc_in", "fc_out")
        else:
            target_suffixes = target_modules
        
        self.coto_adapters = []
        scaling = alpha / rank
        
        for name, module in self.named_modules():
            if isinstance(module, nn.Linear) and any(name.endswith(s) for s in target_suffixes):
                d_in, d_out = module.in_features, module.out_features
                
                # LoRA matrisleri
                lora_A = nn.Linear(d_in, rank, bias=False)
                lora_B = nn.Linear(rank, d_out, bias=False)
                nn.init.kaiming_uniform_(lora_A.weight, a=math.sqrt(5))
                nn.init.zeros_(lora_B.weight)
                
                # CoTo wrapper
                wrapped = CoToAdapterWrapper(module, lora_A, lora_B, scaling)
                
                # Orijinal modulu wrapper ile degistir
                parts = name.split('.')
                parent = self
                for p in parts[:-1]:
                    if p.isdigit():
                        parent = parent[int(p)]
                    else:
                        parent = getattr(parent, p)
                setattr(parent, parts[-1], wrapped)
                
                self.coto_adapters.append(wrapped)
        
        return self.coto_adapters
    
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
                recon_val = avg_recon.item() if isinstance(avg_recon, torch.Tensor) else avg_recon
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
    
    def get_adapter_count(self) -> int:
        return len(self.coto_adapters)
    
    def get_layer_count(self) -> int:
        return len(self.blocks)


# ============================================================
# TEST
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("KVForge v2 Full Model Test")
    print("=" * 60)
    
    model = KVForgeModelV2()
    total, trainable = model.count_parameters()
    print(f"Model: {total/1e6:.1f}M total, {trainable/1e6:.1f}M trainable")
    
    # LoRA ekle
    adapters = model.add_lora(rank=8)
    print(f"  CoTo: {model.get_adapter_count()} adapter ({model.get_layer_count()} layer, {model.get_adapter_count()//6} grup)")
    
    x = torch.randint(0, 1000, (2, 64))
    loss, logits, recon = model(x, labels=x, return_seed=True)
    print(f"\nForward: {x.shape} -> {logits.shape}")
    print(f"  Loss: {loss.item():.4f}")
    
    print("\nOK")
