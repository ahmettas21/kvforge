"""
KVForge × CoTo — LoRA Training (Pythia-410M)
============================================
CoTo: ICML 2025 — github.com/zwebzone/coto
Progressive training stabilizer
"""

import os, subprocess, math, time, json, gc

subprocess.run(['pip', 'install', '-q',
    'torch==2.4.0', 'torchvision==0.19.0',
    '--index-url', 'https://download.pytorch.org/whl/cu121'], check=False)
subprocess.run(['pip', 'install', '-q',
    'transformers>=4.30.0', 'datasets', 'numpy', 'tqdm'], check=False)

os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'

import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from torch.utils.data import Dataset, DataLoader


# ============================================================
# CoTo Core
# ============================================================

def generate_coto_mask(n_groups, p, device='cpu'):
    if p >= 1.0:
        return torch.ones(n_groups, device=device, dtype=torch.bool)
    mask = torch.bernoulli(torch.full((n_groups,), p, device=device)).bool()
    if mask.sum() == 0:
        mask[torch.randint(0, n_groups, (1,)).item()] = True
    return mask


class CoToScheduler:
    def __init__(self, initial_p=0.2, final_p=1.0, stage1_ratio=0.75, total_steps=1000):
        self.initial_p = initial_p
        self.final_p = final_p
        self.stage1_ratio = stage1_ratio
        self.total_steps = total_steps
        self.threshold = int(stage1_ratio * total_steps)
    def get_p(self, step):
        step = min(step, self.total_steps - 1)
        if step >= self.threshold:
            return self.final_p
        p = self.initial_p + (self.final_p - self.initial_p) * (step / max(self.threshold, 1))
        return min(p, self.final_p)


class CoToController:
    def __init__(self, n_groups, initial_p=0.2, stage1_ratio=0.75, total_steps=1000):
        self.n_groups = n_groups
        self.scheduler = CoToScheduler(initial_p, 1.0, stage1_ratio, total_steps)
        self.current_p = initial_p
        self.current_mask = None
        self.step_count = 0
    def step(self, device='cpu'):
        p = self.scheduler.get_p(self.step_count)
        self.current_p = p
        self.current_mask = generate_coto_mask(self.n_groups, p, device)
        self.step_count += 1
        return self.current_mask
    def get_active_count(self):
        if self.current_mask is None: return 0
        return self.current_mask.sum().item()


# ============================================================
# LoRA Adapter Matrix
# ============================================================

class LoRALayer(nn.Module):
    """Single LoRA adapter matrix pair (A, B)."""
    def __init__(self, in_features, out_features, rank=8, alpha=16):
        super().__init__()
        self.A = nn.Parameter(torch.zeros(rank, in_features))
        self.B = nn.Parameter(torch.zeros(out_features, rank))
        self.scale = alpha / rank
        nn.init.kaiming_uniform_(self.A, a=math.sqrt(5))
        nn.init.zeros_(self.B)
    
    def forward(self, x):
        return (x @ self.A.T) @ self.B.T * self.scale


# ============================================================
# Model with CoTo LoRA
# ============================================================

class CoToLoRAModel(nn.Module):
    """
    Uses base model forward, adds LoRA contributions.
    CoTo mask controls which LoRA groups contribute to gradients.
    """
    def __init__(self, pretrained='EleutherAI/pythia-410m', rank=8, alpha=16):
        super().__init__()
        print(f"[1/3] Loading {pretrained}...")
        self.base = AutoModelForCausalLM.from_pretrained(
            pretrained, torch_dtype=torch.float16, low_cpu_mem_usage=True
        )
        for param in self.base.parameters():
            param.requires_grad = False
        
        self.cfg = self.base.config
        self.n_layers = self.cfg.num_hidden_layers  # 24
        self.hidden = self.cfg.hidden_size  # 1024
        self.n_heads = self.cfg.num_attention_heads  # 16
        self.head_dim = self.hidden // self.n_heads
        
        # LoRA adapters per layer: q,k,v,o,ff1,ff2
        self.adapter_names = ['q','k','v','o','ff1','ff2']
        self.adapters_per_layer = len(self.adapter_names)
        
        print(f"[2/3] Creating LoRA adapters ({self.n_layers}x{self.adapters_per_layer}={self.n_layers*self.adapters_per_layer})...")
        
        # Build LoRA parameter dict
        self.lora = nn.ParameterDict()
        for li in range(self.n_layers):
            block = self.base.gpt_neox.layers[li]
            
            # QKV: in=hidden, out=3*hidden
            self.lora[f'{li}_q'] = LoRALayer(self.hidden, self.hidden, rank, alpha)
            self.lora[f'{li}_k'] = LoRALayer(self.hidden, self.hidden, rank, alpha)
            self.lora[f'{li}_v'] = LoRALayer(self.hidden, self.hidden, rank, alpha)
            
            # O: in=hidden, out=hidden
            o_in = block.attention.dense.in_features
            o_out = block.attention.dense.out_features
            self.lora[f'{li}_o'] = LoRALayer(o_in, o_out, rank, alpha)
            
            # FF1: hidden -> 4*hidden
            ff1_in = block.mlp.dense_h_to_4h.in_features
            ff1_out = block.mlp.dense_h_to_4h.out_features
            self.lora[f'{li}_ff1'] = LoRALayer(ff1_in, ff1_out, rank, alpha)
            
            # FF2: 4*hidden -> hidden
            ff2_in = block.mlp.dense_4h_to_h.in_features
            ff2_out = block.mlp.dense_4h_to_h.out_features
            self.lora[f'{li}_ff2'] = LoRALayer(ff2_in, ff2_out, rank, alpha)
        
        # CoTo setup
        self.n_groups = self.n_layers
        self.coto = None
        self.coto_enabled = False
        
        total = sum(p.numel() for p in self.lora.parameters())
        print(f"[3/3] Done. LoRA params: {total:,}, Groups: {self.n_groups}")
    
    def enable_coto(self, initial_p=0.2, stage1_ratio=0.75, total_steps=5000):
        self.coto_enabled = True
        self.coto = CoToController(self.n_groups, initial_p, stage1_ratio, total_steps)
        print(f"  CoTo: {self.n_groups} groups, p0={initial_p}->1.0, ratio={stage1_ratio}")
    
    def get_trainable(self):
        return list(self.lora.parameters())
    
    def forward(self, input_ids, labels=None):
        device = input_ids.device
        bsz, seq = input_ids.shape
        
        # CoTo mask
        if self.coto_enabled and self.training:
            mask = self.coto.step(device)
        else:
            mask = torch.ones(self.n_groups, device=device, dtype=torch.bool)
        
        # Run base model (no grad for base)
        with torch.no_grad():
            base_out = self.base(input_ids, output_hidden_states=True, use_cache=False)
            base_logits = base_out.logits  # (B, S, V)
            hidden_states = base_out.hidden_states  # tuple of (B, S, H) per layer + input
        
        # Apply LoRA adapters with CoTo mask on hidden states
        # Use residuals from base model's hidden states
        lora_logits_adjustment = 0.0
        active_count = 0
        
        for li in range(self.n_layers):
            group_active = mask[li].item()
            if not group_active:
                continue
            active_count += 1
            
            # Get this layer's input hidden state
            h = hidden_states[li]  # (B, S, H) - input to this layer
            
            # Apply LoRA: compute the effect on logits via weight adjustments
            # We approximate: LoRA adjusts Q,K,V,O,FF1,FF2 -> affects LM head output
            # For simplicity: add LoRA contribution scaled by group activity
            # to the final logits via a learned projection
            with torch.no_grad():
                h = h.to(dtype=torch.float16)
            
            # QKV LoRA: affects attention, approximated as hidden state adjustment
            lora_q = self.lora[f'{li}_q'](h)
            lora_k = self.lora[f'{li}_k'](h)
            lora_v = self.lora[f'{li}_v'](h)
            
            # Approximate: QKV adjustment = attention adjustment
            # Simplified: use mean pooling over heads
            lora_attn_adj = (lora_q + lora_k + lora_v) / 3.0
            
            # O projection LoRA
            lora_o = self.lora[f'{li}_o'](h)
            
            # Combined attention adjustment
            attn_adj = lora_attn_adj + lora_o
            
            # FFN LoRA
            lora_ff1 = self.lora[f'{li}_ff1'](h)
            # GELU activation
            lora_ff1 = F.gelu(lora_ff1)
            lora_ff2 = self.lora[f'{li}_ff2'](lora_ff1)
            
            # Total adjustment for this layer
            layer_adj = attn_adj * 0.5 + lora_ff2 * 0.5
            
            # Project adjustment to vocab space via LM head
            lm_head = self.base.embed_out
            logit_adj = F.linear(layer_adj, lm_head.weight)  # (B, S, V)
            lora_logits_adjustment = lora_logits_adjustment + logit_adj
        
        # Final logits = base + LoRA adjustment
        final_logits = base_logits + lora_logits_adjustment
        
        loss = None
        if labels is not None:
            shift_logits = final_logits[:, :-1, :].contiguous()
            shift_labels = labels[:, 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.view(-1, shift_logits.size(-1)),
                shift_labels.view(-1),
                ignore_index=-100
            )
        
        return loss, final_logits, active_count


# ============================================================
# Dataset
# ============================================================

class TextDataset(Dataset):
    def __init__(self, tokenizer, path, seq_len=256, max_samples=2000):
        self.seq_len = seq_len
        with open(path) as f:
            text = f.read()
        tokens = tokenizer.encode(text)
        print(f"  Tokens: {len(tokens):,}")
        self.examples = []
        for i in range(0, len(tokens) - seq_len, seq_len):
            chunk = tokens[i:i+seq_len]
            if len(chunk) == seq_len:
                self.examples.append(torch.tensor(chunk, dtype=torch.long))
        if max_samples and len(self.examples) > max_samples:
            self.examples = self.examples[:max_samples]
        print(f"  Samples: {len(self.examples)}")
    def __len__(self):
        return len(self.examples)
    def __getitem__(self, idx):
        return self.examples[idx]


# ============================================================
# Training
# ============================================================

def train():
    print("=" * 70)
    print("KVForge x CoTo - Pythia-410M LoRA Training")
    print("=" * 70)
    
    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {DEVICE}")
    if DEVICE.type == 'cuda':
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f}GB")
    
    SEQ_LEN = 256
    BATCH = 2
    GA = 4
    LR = 2e-4
    EPOCHS = 2
    RANK = 8
    ALPHA = 16
    COTO_P0 = 0.2
    COTO_RATIO = 0.75
    
    print(f"\n  Batch={BATCH}, GA={GA}, eff_batch={BATCH*GA}")
    print(f"  LR={LR}, Epochs={EPOCHS}, Rank={RANK}")
    print(f"  CoTo: p0={COTO_P0}->1.0, ratio={COTO_RATIO}\n")
    
    # Data
    print("[Data] WikiText-103 loading...")
    ds = load_dataset('wikitext', 'wikitext-103-raw-v1', split='train')
    with open('/kaggle/working/wikitext.txt', 'w') as f:
        for line in ds['text'][:30000]:
            f.write(line + '\n')
    
    tokenizer = AutoTokenizer.from_pretrained('EleutherAI/pythia-410m')
    tokenizer.pad_token = tokenizer.eos_token
    
    dataset = TextDataset(tokenizer, '/kaggle/working/wikitext.txt', seq_len=SEQ_LEN, max_samples=1500)
    val_ds = [x for i, x in enumerate(dataset) if i % 10 == 0]
    train_ds = [x for i, x in enumerate(dataset) if i % 10 != 0]
    print(f"  Train: {len(train_ds)}, Val: {len(val_ds)}")
    
    tl = DataLoader(train_ds, batch_size=BATCH, shuffle=True, num_workers=0)
    val_batches = list(DataLoader(val_ds, batch_size=1, num_workers=0))
    
    # Model
    model = CoToLoRAModel(rank=RANK, alpha=ALPHA)
    model = model.to(DEVICE)
    
    total_steps = len(tl) * EPOCHS
    model.enable_coto(initial_p=COTO_P0, stage1_ratio=COTO_RATIO, total_steps=total_steps)
    
    trainable = model.get_trainable()
    opt = torch.optim.AdamW(trainable, lr=LR, weight_decay=0.01)
    scaler = torch.amp.GradScaler('cuda')
    
    torch.cuda.empty_cache()
    gc.collect()
    
    t0 = time.time()
    best_ppl = float('inf')
    results = []
    
    for epoch in range(EPOCHS):
        model.train()
        epoch_loss = 0.0
        
        print(f"\n  --- Epoch {epoch+1}/{EPOCHS} ---")
        
        for step, batch in enumerate(tl):
            batch = batch.to(DEVICE)
            
            with torch.amp.autocast('cuda'):
                loss, _, active = model(batch, labels=batch)
                loss = loss / GA
            
            scaler.scale(loss).backward()
            
            if (step + 1) % GA == 0:
                scaler.unscale_(opt)
                torch.nn.utils.clip_grad_norm_(trainable, max_norm=1.0)
                scaler.step(opt)
                scaler.update()
                opt.zero_grad()
            
            epoch_loss += loss.item() * GA
            
            if (step + 1) % 25 == 0:
                p = model.coto.current_p if model.coto_enabled else 1.0
                mem = torch.cuda.max_memory_allocated() / 1e9
                elapsed = time.time() - t0
                avg = epoch_loss / max(step + 1, 1)
                print(f"  S{step+1:3d}|L={avg:.4f}|p={p:.3f}|active={active}/{model.n_groups}|Mem={mem:.1f}GiB|T={elapsed:.0f}s")
        
        # Validation
        model.eval()
        val_loss = 0.0
        vc = 0
        
        with torch.no_grad():
            for bv in val_batches:
                if vc >= 30: break
                bv = bv.to(DEVICE)
                with torch.amp.autocast('cuda'):
                    l, _, _ = model(bv, labels=bv)
                val_loss += l.item()
                vc += 1
        
        val_loss /= max(vc, 1)
        val_ppl = math.exp(min(val_loss, 20))
        elapsed = time.time() - t0
        
        print(f"\n  === Epoch {epoch+1}: Val Loss={val_loss:.4f}, Val PPL={val_ppl:.1f} ===")
        
        results.append({
            'epoch': epoch + 1,
            'val_loss': round(val_loss, 4),
            'val_ppl': round(val_ppl, 1),
            'co_to_p': round(model.coto.current_p, 3) if model.coto_enabled else 1.0,
        })
        
        if val_ppl < best_ppl:
            best_ppl = val_ppl
            torch.save(model.state_dict(), '/kaggle/working/kvforge_coto_best.pt')
            print(f"  ** Best PPL: {best_ppl:.1f} **")
    
    total_time = time.time() - t0
    max_mem = torch.cuda.max_memory_allocated() / 1e9
    
    print("\n" + "=" * 70)
    print(f"  DONE! Time={total_time:.0f}s, MaxMem={max_mem:.1f}GiB, BestPPL={best_ppl:.1f}")
    print("=" * 70)
    
    out = {
        'model': 'Pythia-410M + CoTo LoRA',
        'co_to': {
            'n_groups': model.n_groups,
            'initial_p': COTO_P0,
            'stage1_ratio': COTO_RATIO,
        },
        'config': {
            'batch': BATCH, 'grad_accum': GA, 'lr': LR, 'epochs': EPOCHS,
            'rank': RANK, 'alpha': ALPHA,
            'adapter_params': sum(p.numel() for p in model.lora.parameters()),
        },
        'results': {
            'best_val_ppl': round(best_ppl, 1),
            'time_min': round(total_time / 60, 1),
            'gpu_mem': round(max_mem, 1),
            'epochs': results,
        },
    }
    
    with open('/kaggle/working/kvforge_coto_results.json', 'w') as f:
        json.dump(out, f, indent=2)
    
    print(json.dumps(out, indent=2))
    print("\nResults saved to kvforge_coto_results.json")


if __name__ == '__main__':
    train()
