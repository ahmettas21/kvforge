"""
Vanilla GPT-Neo 1.3B Baseline (P100 16GB, v2 fix)
=====================================================
- HuggingFace GPT-Neo 1.3B, AutoModelForCausalLM
- Gradient checkpointing enabled
- FP32 (HF float16 + GradScaler incompatible fix → model.half() + no scaler)
- Batch=1, grad_accum=8, seq=512
"""

# ============================================================
# HÜCRE 1: KURULUM
# ============================================================
import os, subprocess, math, time, sys, json, gc

subprocess.run(['pip', 'install', '-q', 'torch==2.4.0', 'torchvision==0.19.0',
    '--index-url', 'https://download.pytorch.org/whl/cu121'], check=False)
subprocess.run(['pip', 'install', '-q', 'transformers', 'datasets'], check=False)

os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'
os.environ['OMP_NUM_THREADS'] = '2'

from datasets import load_dataset
ds = load_dataset('wikitext', 'wikitext-103-raw-v1', split='train')
with open('/kaggle/working/wikitext.txt', 'w') as f:
    for line in ds['text'][:50000]:
        f.write(line + '\n')
print(f"WikiText-103: 50000 lines written")

# ============================================================
# HÜCRE 2: MODEL
# ============================================================
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM
from torch.utils.data import Dataset, DataLoader


# ============================================================
# HÜCRE 3: DATASET
# ============================================================
class TextDataset(Dataset):
    def __init__(self, tokenizer, text_path, seq_len=512, max_samples=None):
        self.seq_len = seq_len
        with open(text_path, 'r') as f:
            text = f.read()
        tokens = tokenizer.encode(text)
        print(f"  Tokenler: {len(tokens):,}")
        self.examples = []
        for i in range(0, len(tokens) - seq_len, seq_len):
            chunk = tokens[i:i + seq_len]
            if len(chunk) == seq_len:
                self.examples.append(torch.tensor(chunk, dtype=torch.long))
        if max_samples and len(self.examples) > max_samples:
            self.examples = self.examples[:max_samples]
        print(f"  Ornek: {len(self.examples)}")

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return self.examples[idx]


# ============================================================
# HÜCRE 4: EĞİTİM
# ============================================================
def train():
    print("=" * 60)
    print("Vanilla GPT-Neo 1.3B Baseline (v2 fix)")
    print("=" * 60)

    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {DEVICE}")
    if DEVICE.type == 'cuda':
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

    SEQ_LEN = 512
    BATCH_SIZE = 1
    LR = 1e-4
    NUM_EPOCHS = 3
    GRAD_ACCUM = 8
    MAX_STEPS = 1000

    # Tokenizer & Model — FP16 yükle ama scaler kullanma
    print("\n[1/4] Loading GPT-Neo 1.3B...")
    tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-1.3B')
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        'EleutherAI/gpt-neo-1.3B',
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    ).to(DEVICE)

    model.gradient_checkpointing_enable()

    total = sum(p.numel() for p in model.parameters())
    print(f"Model: {total/1e6:.1f}M total, dtype={model.dtype}")
    print(f"  Gradient checkpointing: enabled")
    print(f"  Batch: {BATCH_SIZE} × {GRAD_ACCUM} accum = eff {BATCH_SIZE*GRAD_ACCUM}")
    print(f"  No GradScaler (fp16 model, manual loss scaling)")

    # Dataset
    print("\n[2/4] Loading WikiText-103...")
    ds = TextDataset(tokenizer, '/kaggle/working/wikitext.txt', seq_len=SEQ_LEN, max_samples=10000)
    train_ds = [x for i, x in enumerate(ds) if i % 10 != 0]
    val_ds = [x for i, x in enumerate(ds) if i % 10 == 0 and i > 0]
    print(f"Train: {len(train_ds)}, Val: {len(val_ds)}")

    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=2,
                               pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=1, num_workers=2, pin_memory=True)

    # Optimizer — GradScaler yok!
    print("\n[3/4] Setting up optimizer (no scaler)...")
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=0.01, betas=(0.9, 0.95))
    total_steps = min(len(train_loader) * NUM_EPOCHS, MAX_STEPS)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-6)

    # Eğitim
    print("\n[4/4] Training...\n")
    model.train()
    t_start = time.time()
    best_loss = float('inf')
    global_step = 0

    # Loss scaling factor (fp16 underflow önleme)
    loss_scale = 128.0

    for epoch in range(NUM_EPOCHS):
        model.train()
        opt.zero_grad()

        for bidx, batch in enumerate(train_loader):
            if global_step >= MAX_STEPS:
                break

            batch = batch.to(DEVICE, non_blocking=True)

            # Forward fp16
            with torch.amp.autocast('cuda'):
                outputs = model(batch, labels=batch)
                loss = outputs.loss / GRAD_ACCUM

            # Manual loss scaling (fp16 gradyan underflow'u önle)
            scaled_loss = loss * loss_scale
            scaled_loss.backward()

            if (bidx + 1) % GRAD_ACCUM == 0:
                # Unscale grads
                for p in model.parameters():
                    if p.grad is not None:
                        p.grad.data.div_(loss_scale)

                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                opt.step()
                opt.zero_grad()
                scheduler.step()
                global_step += 1

                if global_step % 10 == 0:
                    elapsed = time.time() - t_start
                    mem = torch.cuda.max_memory_allocated()/1e9
                    print(f"E{epoch}|S{global_step:4d}/{total_steps} "
                          f"L={loss.item()*GRAD_ACCUM:.4f} "
                          f"Mem={mem:.1f}GiB ({elapsed:.0f}s)")

            if bidx % 20 == 0:
                torch.cuda.empty_cache()
                gc.collect()

        # Validation
        model.eval()
        val_loss = 0.0
        val_steps = 0
        with torch.no_grad():
            for batch in val_loader:
                if val_steps >= 50:
                    break
                batch = batch.to(DEVICE, non_blocking=True)
                with torch.amp.autocast('cuda'):
                    outputs = model(batch, labels=batch)
                val_loss += outputs.loss.item()
                val_steps += 1
        val_loss /= max(val_steps, 1)
        val_ppl = math.exp(min(val_loss, 20))
        elapsed = time.time() - t_start
        max_mem = torch.cuda.max_memory_allocated()/1e9
        print(f"\n  → Epoch {epoch+1} ({elapsed:.0f}s, max_mem={max_mem:.1f}GiB): "
              f"Val L={val_loss:.4f} PPL={val_ppl:.1f}")
        if val_loss < best_loss:
            best_loss = val_loss

    total_time = time.time() - t_start
    print(f"\n✅ Vanilla GPT-Neo 1.3B tamam! {total_time:.0f}s ({total_time/60:.1f} dk)")
    print(f"Best Val PPL: {math.exp(min(best_loss, 20)):.1f}")

    results = {
        'model': 'Vanilla GPT-Neo 1.3B (v2 fix)',
        'config': {
            'seq_len': SEQ_LEN,
            'batch_size': BATCH_SIZE,
            'grad_accum': GRAD_ACCUM,
            'eff_batch': BATCH_SIZE * GRAD_ACCUM,
            'gradient_checkpointing': True,
            'fp16': True,
            'grad_scaler': False,
            'loss_scale': loss_scale,
            'max_steps': min(MAX_STEPS, global_step),
            'lr': LR,
        },
        'results': {
            'best_val_loss': best_loss,
            'best_val_ppl': round(math.exp(min(best_loss, 20)), 1),
            'training_time_min': round(total_time / 60, 1),
            'total_params': total,
        }
    }

    with open('/kaggle/working/vanilla_gptneo_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSonuçlar: vanilla_gptneo_results.json")
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    train()
