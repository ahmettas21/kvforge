"""Quick test: can a tiny model learn these synthetic tasks?"""
import torch, torch.nn.functional as F, math, json
from torch.utils.data import DataLoader, TensorDataset
from copy import deepcopy
import random

torch.manual_seed(42); random.seed(42)

# Ultra-tiny model (no attention, just MLP + embeddings)
class TinyNet(torch.nn.Module):
    def __init__(self, vs=256, hidden=64, seq=16):
        super().__init__()
        self.emb = torch.nn.Embedding(vs, hidden)
        self.net = torch.nn.Sequential(
            torch.nn.Linear(hidden, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, vs),
        )

    def forward(self, x):
        B, S = x.shape
        h = self.emb(x).mean(dim=1)  # pool over seq
        return self.net(h).unsqueeze(1).expand(-1, S, -1).reshape(B*S, -1)

# Data: simpler task — frequency classification
def make_freq_task(vs=256, seq=16, n=500):
    xs, ys = [], []
    for _ in range(n):
        s = torch.randint(0, vs, (seq,))
        # target: predict most frequent token
        freq = torch.bincount(s, minlength=vs)
        target = freq.argmax()
        xs.append(s)
        ys.append(torch.full((seq,), target, dtype=torch.long))
    return TensorDataset(torch.stack(xs), torch.stack(ys))

# Actually, even simpler: identity mapping (predict next token)
def make_id_task(vs=256, seq=16, n=500):
    xs, ys = [], []
    for _ in range(n):
        s = torch.randint(0, vs, (seq,))
        xs.append(s)
        ys.append(s)  # predict same sequence
    return TensorDataset(torch.stack(xs), torch.stack(ys))

print("Testing simple identity task...")
cfg_vs = 64  # small vocab for quick test
d = make_id_task(cfg_vs, seq=8, n=200)
tr = DataLoader(TensorDataset(d.tensors[0][:150], d.tensors[1][:150]), 32, shuffle=True)
te = DataLoader(TensorDataset(d.tensors[0][150:], d.tensors[1][150:]), 32)

model = TinyNet(cfg_vs, hidden=32, seq=8)
opt = torch.optim.AdamW(model.parameters(), lr=0.01)

for ep in range(30):
    ls = 0.0
    for x, y in tr:
        opt.zero_grad()
        l = F.cross_entropy(model(x), y.reshape(-1))
        l.backward(); opt.step()
        ls += l.item()
    if (ep+1)%10==0:
        model.eval()
        ok = tot = 0
        with torch.no_grad():
            for x, y in te:
                ok += (model(x).argmax(-1) == y.reshape(-1)).sum().item()
                tot += y.numel()
        print(f"  ep{ep+1} loss={ls/len(tr):.4f} acc={ok/tot:.4f}")
print("DONE")
