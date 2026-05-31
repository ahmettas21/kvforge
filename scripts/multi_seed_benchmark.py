"""
KVForge v2 — Multi-Seed Benchmark Training
===========================================
3 farklı random seed ile eğitim, ortalama + std hesaplama.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import math
import time
import json

from kvforge.nano_model_v2 import (
    NanoKVForgeV2, create_datasets, BATCH_SIZE, NUM_EPOCHS, RECON_LAMBDA
)
from kvforge.nano_model import NanoKVForge

SEEDS = [42, 123, 7]
CKPT_DIR = '/home/turk/.openclaw/workspace/cag/kvforge/checkpoints'


def train_and_eval(seed, is_v2):
    """Tek seed ile eğit ve val PPL hesapla."""
    t0 = time.time()
    
    # Seed
    torch.manual_seed(seed)
    
    # Model
    if is_v2:
        model = NanoKVForgeV2()
        tag = 'v2'
    else:
        model = NanoKVForge()
        tag = 'v1'
    
    total, _ = model.count_parameters()
    
    # Dataset
    train_ds, val_ds = create_datasets()
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE)
    
    # Optimizer
    opt = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=0.01)
    total_steps = len(train_loader) * NUM_EPOCHS
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-5)
    
    # Eğitim
    best_loss = float('inf')
    for epoch in range(NUM_EPOCHS):
        model.train()
        for bidx, batch in enumerate(train_loader):
            opt.zero_grad()
            loss, _, recon = model(batch, labels=batch, return_seed=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            opt.step()
            scheduler.step()
        
        # Validation
        model.eval()
        val_loss = 0.0
        for batch in val_loader:
            l, _, _ = model(batch, labels=batch, return_seed=True)
            val_loss += l.item()
        val_loss /= len(val_loader)
        
        if val_loss < best_loss:
            best_loss = val_loss
    
    # Final validation
    model.eval()
    total_ce = 0.0
    total_recon = 0.0
    n = 0
    for batch in val_loader:
        loss, _, recon = model(batch, labels=batch, return_seed=True)
        ce = loss.item() - RECON_LAMBDA * (recon if recon else 0.0)
        total_ce += ce
        total_recon += recon if recon else 0.0
        n += 1
    
    avg_ce = total_ce / n
    avg_recon = total_recon / n
    ppl = math.exp(min(avg_ce, 20))
    
    elapsed = time.time() - t0
    
    return {
        'seed': seed,
        'model': tag,
        'params': total,
        'val_ce': round(avg_ce, 4),
        'val_ppl': round(ppl, 2),
        'recon_loss': round(avg_recon, 5),
        'best_loss': round(best_loss, 4),
        'time_s': round(elapsed, 0),
    }


# === RUN ===
print('=' * 60)
print('KVForge Multi-Seed Benchmark (3 runs each)')
print('=' * 60)

results = {'v1': [], 'v2': []}

for is_v2 in [False, True]:
    tag = 'v2' if is_v2 else 'v1'
    print(f'\n--- {tag.upper()} ---')
    
    for seed in SEEDS:
        print(f'\n  Seed {seed}...')
        r = train_and_eval(seed, is_v2)
        results[tag].append(r)
        print(f'    PPL={r["val_ppl"]} Recon={r["recon_loss"]} ({r["time_s"]:.0f}s)')

# === SONUÇLAR ===
print('\n' + '=' * 60)
print('NİHAİ SONUÇLAR')
print('=' * 60)

for tag in ['v1', 'v2']:
    ppls = [r['val_ppl'] for r in results[tag]]
    recons = [r['recon_loss'] for r in results[tag]]
    params = results[tag][0]['params']
    
    mean_ppl = sum(ppls) / len(ppls)
    std_ppl = (sum((p - mean_ppl)**2 for p in ppls) / len(ppls)) ** 0.5
    mean_recon = sum(recons) / len(recons)
    
    print(f'\n{tag.upper()}:')
    print(f'  PPL:     {ppls}')
    print(f'  Mean:    {mean_ppl:.2f} ± {std_ppl:.2f}')
    print(f'  Recon:   {recons}')
    print(f'  Mean:    {mean_recon:.4f}')
    print(f'  Params:  {params:,}')

# Kaydet
with open(f'{CKPT_DIR}/multi_seed_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f'\nSonuçlar kaydedildi: {CKPT_DIR}/multi_seed_results.json')
