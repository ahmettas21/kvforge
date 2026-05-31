#!/bin/bash
# KVForge Benchmark Script
set -e

echo "KVForge Benchmark"
echo "================="
echo ""

# Model bilgisi
python3 -c "
import sys, os
sys.path.insert(0, '.')
from kvforge.nano_model import NanoKVForge, D_MODEL, N_HEADS, N_LAYERS, SEED_DIM
m = NanoKVForge()
total = sum(p.numel() for p in m.parameters())
print(f'Model: {N_LAYERS}L {N_HEADS}H {D_MODEL}D | Seed={SEED_DIM}')
print(f'Param: {total:,} ({total/1e3:.1f}K)')
print(f'Compression: {2*D_MODEL//SEED_DIM}x')
"

echo ""
echo "=== Inference Hız Testi ==="
python3 -c "
import torch, time, sys, os
sys.path.insert(0, '.')
from kvforge.nano_model import NanoKVForge

model = NanoKVForge()
model.eval()
x = torch.randint(0, 256, (1, 32))

with torch.no_grad():
    # warmup
    for _ in range(20): model(x)
    
    # measure
    t0 = time.time()
    for _ in range(200): model(x)
    t = time.time() - t0
    
    print(f'200 forward: {t:.2f}s ({200/t:.0f} passes/s)')
    print(f'Per token: {t/200*1000:.1f}ms')
"

echo ""
echo "=== Memory Test ==="
python3 -c "
import torch, os, psutil, sys
sys.path.insert(0, '.')
from kvforge.nano_model import NanoKVForge

model = NanoKVForge()
proc = psutil.Process(os.getpid())
mem_before = proc.memory_info().rss / 1024 / 1024

# Forward
x = torch.randint(0, 256, (64, 32))
with torch.no_grad():
    for _ in range(10): model(x)

mem_after = proc.memory_info().rss / 1024 / 1024
print(f'RAM before: {mem_before:.0f} MB')
print(f'RAM after:  {mem_after:.0f} MB')
print(f'Delta:     +{mem_after-mem_before:.0f} MB')
"

echo ""
echo "=== Benchmark Complete ==="
