#!/usr/bin/env python3
"""
KVForge v2 Full Model — CoTo Progressive Training
===================================================
CoTo (Come Together): ICML 2025 — github.com/zwebzone/coto

Progressive training'de her layer ayrı PPL 27-35, tümü aktif PPL 91.
CoTo: Bernoulli(p(t)) maskesi ile adapter'ları kademeli aktifleştir.

Kullanım:
  python train_full_v2.py                   # vanilla
  python train_full_v2.py --coto             # CoTo ile
  python train_full_v2.py --coto --coto_p0 0.2 --coto_ratio 0.75
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import math
import time
import os
import sys
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kvforge.full_model_v2 import KVForgeModelV2
from kvforge.coto_adapter import CoToController

VOCAB_SIZE = 50257
D_MODEL = 768
N_HEADS = 12
N_LAYERS = 12
SEED_DIM = 64
MAX_SEQ_LEN = 256
BATCH_SIZE = 4
LR = 3e-4
WEIGHT_DECAY = 0.01
NUM_EPOCHS = 5
RECON_LAMBDA = 0.1
WARMUP_STEPS = 500
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class TextDataset(Dataset):
    def __init__(self, text_path, tokenizer_name='gpt2', seq_len=MAX_SEQ_LEN,
                 train=True, split_ratio=0.9, max_samples=None):
        from transformers import GPT2Tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        with open(text_path, 'r', encoding='utf-8') as f:
            text = f.read()
        tokens = self.tokenizer.encode(text)
        print(f"  Toplam token: {len(tokens):,}")
        
        split_idx = int(len(tokens) * split_ratio)
        tokens = tokens[:split_idx] if train else tokens[split_idx:]
        
        self.examples = []
        for i in range(0, len(tokens) - seq_len, seq_len // 2):
            chunk = tokens[i:i + seq_len]
            if len(chunk) == seq_len:
                self.examples.append(torch.tensor(chunk, dtype=torch.long))
        
        if max_samples and len(self.examples) > max_samples:
            self.examples = self.examples[:max_samples]
        print(f"  {len(self.examples)} ornek ({'train' if train else 'val'})")
    
    def __len__(self): return len(self.examples)
    def __getitem__(self, idx): return self.examples[idx]


def train():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=NUM_EPOCHS)
    parser.add_argument('--batch', type=int, default=BATCH_SIZE)
    parser.add_argument('--seq', type=int, default=MAX_SEQ_LEN)
    parser.add_argument('--lr', type=float, default=LR)
    parser.add_argument('--data', type=str, default='dataset.txt')
    parser.add_argument('--coto', action='store_true',
                        help='CoTo progressive training stabilizer')
    parser.add_argument('--coto_p0', type=float, default=0.2,
                        help='CoTo initial Bernoulli p (default: 0.2)')
    parser.add_argument('--coto_ratio', type=float, default=0.75,
                        help='CoTo stage1 ratio (default: 0.75)')
    args = parser.parse_args()
    
    print("=" * 60)
    print("KVForge v2 FULL — CoTo Progressive Training")
    print("=" * 60)
    print(f"  Device: {DEVICE}")
    if DEVICE.type == 'cuda':
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")
    print(f"  {N_LAYERS}L x {N_HEADS}H x {D_MODEL}D | Seed: {SEED_DIM}")
    print(f"  Seq: {args.seq} | Batch: {args.batch} | Epochs: {args.epochs}")
    print(f"  CoTo: {'AKTIF' if args.coto else 'KAPALI'}")
    if args.coto:
        print(f"    p0={args.coto_p0}, ratio={args.coto_ratio}, groups=32")
    print()
    
    # Dataset
    dataset_path = args.data
    if not os.path.exists(dataset_path):
        print("Dataset indiriliyor...")
        import urllib.request
        url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        urllib.request.urlretrieve(url, dataset_path)
    
    print("Dataset hazirlaniyor...")
    train_ds = TextDataset(dataset_path, seq_len=args.seq, train=True, max_samples=20000)
    val_ds = TextDataset(dataset_path, seq_len=args.seq, train=False, max_samples=2000)
    train_loader = DataLoader(train_ds, batch_size=args.batch, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_ds, batch_size=args.batch, num_workers=2)
    print()
    
    # Model
    model = KVForgeModelV2(max_seq_len=args.seq)
    
    # LoRA adapter'lari ekle (CoTo icin gerekli)
    if args.coto:
        adapters = model.add_lora(rank=8, alpha=16.0)
        print(f"  LoRA: {len(adapters)} adapter eklendi")
    
    model = model.to(DEVICE)
    total, trainable = model.count_parameters()
    print(f"Model: {total/1e6:.1f}M ({trainable/1e6:.1f}M trainable)")
    print(f"  Compression: 24x (2*768/64 = 24)")
    print(f"  Encoder: 4x768=3072 -> contextual v2")
    
    # CoTo controller
    coto_ctrl = None
    if args.coto:
        total_steps_coto = len(train_loader) * args.epochs
        n_layers = model.get_layer_count()
        coto_ctrl = CoToController(model, total_steps_coto,
                                    n_groups=n_layers,
                                    initial_p=args.coto_p0,
                                    stage1_ratio=args.coto_ratio)
        print(f"  CoTo: {n_layers} groups, {total_steps_coto} total steps")
    print()
    
    # Optimizer
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * args.epochs
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-6)
    scaler = torch.amp.GradScaler('cuda') if DEVICE.type == 'cuda' else None
    
    # === TRAINING ===
    print("=" * 60)
    print("EGITIM BASLIYOR")
    print("=" * 60)
    
    t_start = time.time()
    best_loss = float('inf')
    global_step = 0
    
    for epoch in range(args.epochs):
        model.train()
        total_loss = total_recon = 0.0
        n = 0
        
        for bidx, batch in enumerate(train_loader):
            batch = batch.to(DEVICE)
            
            # CoTo: Bernoulli mask uygula
            if coto_ctrl:
                p_t = coto_ctrl.step(global_step)
            else:
                p_t = 1.0
            
            # Forward
            if scaler:
                with torch.amp.autocast('cuda'):
                    loss, _, recon = model(batch, labels=batch, return_seed=True)
                scaler.scale(loss).backward()
                scaler.unscale_(opt)
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                scaler.step(opt)
                scaler.update()
            else:
                loss, _, recon = model(batch, labels=batch, return_seed=True)
                loss.backward()
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                opt.step()
            
            opt.zero_grad()
            scheduler.step()
            global_step += 1
            
            total_loss += loss.item()
            total_recon += recon if recon else 0.0
            n += 1
            
            if bidx % 20 == 0:
                avg_loss = total_loss / n
                avg_recon = total_recon / n
                ce_est = avg_loss - RECON_LAMBDA * avg_recon
                ppl = math.exp(min(ce_est, 20))
                elapsed = time.time() - t_start
                lr_val = scheduler.get_last_lr()[0]
                coto_info = f" p={p_t:.2f} a={coto_ctrl.get_active_count()}/32" if coto_ctrl else ""
                
                print(f"E{epoch}|B{bidx:3d}/{len(train_loader)} "
                      f"L={avg_loss:.4f} CE={ce_est:.4f} "
                      f"R={avg_recon:.5f} PPL={ppl:.1f}"
                      f"{coto_info} "
                      f"LR={lr_val:.2e} {elapsed:.0f}s")
        
        # Validation (tum adapterlar tam aktif)
        model.eval()
        if coto_ctrl:
            coto_ctrl.disable_all()  # inference: cotodrop=False
        
        val_loss = val_recon = 0.0
        for batch in val_loader:
            batch = batch.to(DEVICE)
            with torch.no_grad():
                l, _, r = model(batch, labels=batch, return_seed=True)
            val_loss += l.item()
            val_recon += r if r else 0.0
        
        val_loss /= len(val_loader)
        val_recon /= len(val_loader)
        val_ce = val_loss - RECON_LAMBDA * val_recon
        val_ppl = math.exp(min(val_ce, 20))
        
        print(f"\n  -> Epoch {epoch+1}: Val L={val_loss:.4f} CE={val_ce:.4f} "
              f"PPL={val_ppl:.1f} (BEST={best_loss:.4f})")
        
        if val_loss < best_loss:
            best_loss = val_loss
            torch.save(model.state_dict(), 'full_v2_best.pt')
            print(f"  * Best model!")
    
    total_time = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"EGITIM TAMAM — {total_time:.0f}s ({total_time/60:.1f} dk)")
    print(f"Best Val Loss: {best_loss:.4f} | PPL: {math.exp(min(best_loss, 20)):.1f}")
    print(f"{'='*60}")


if __name__ == "__main__":
    train()
