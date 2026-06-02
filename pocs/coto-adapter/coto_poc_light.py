#!/usr/bin/env python3
"""
CoTo Adapter Training PoC (Lightweight)
========================================
Minimal version that actually works.
Compares isolated vs CoTo stochastic training for LoRA adapters.
"""
import json, math, random, time, sys
import torch, torch.nn as nn, torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42); random.seed(42)

# ── Simple predictor with LoRA ────────────────────────────────

class SimplePred(nn.Module):
    """Very small predictor: embedding + 1 linear layer + output.
    Each adapter is a separate LoRA delta on the linear layer."""

    def __init__(self, vocab=32, hidden=32):
        super().__init__()
        self.emb = nn.Embedding(vocab, hidden)
        self.W = nn.Linear(hidden, vocab, bias=False)  # base weights
        # LoRA adapters stored in ModuleList for .parameters() tracking
        self.adapter_A = nn.ModuleList()
        self.adapter_B = nn.ModuleList()

    def add_adapter(self, r=4):
        h, v = self.W.in_features, self.W.out_features
        self.adapter_A.append(nn.Linear(h, r, bias=False))
        self.adapter_B.append(nn.Linear(r, v, bias=False))
        # Zero-init B
        self.adapter_B[-1].weight.data.zero_()

    def forward(self, x, adapter_ids=None):
        """x: (B, S)  |  adapter_ids: list of indices or None=all"""
        h = self.emb(x)                               # B,S,H
        h = h.mean(dim=1)                              # B,H (pool)
        base = self.W(h)                                # B,V
        if adapter_ids is None:
            adapter_ids = range(len(self.adapter_A))
        lora_out = 0
        for i in adapter_ids:
            lora_out = lora_out + self.adapter_B[i](self.adapter_A[i](h))
        return base + lora_out                          # B,V


# ── Tasks ─────────────────────────────────────────────────────

def make_task(tid, vocab=32, seq=8, n=300):
    """Two different token-shift tasks."""
    xs, ys = [], []
    for _ in range(n):
        s = torch.randint(5, vocab, (seq,))
        if tid == 0:
            t = s.clone()
            t[1:] = s[:-1]    # shift right by 1
        else:
            t = s.clone()
            t[:-1] = s[1:]    # shift left by 1
        xs.append(s)
        ys.append(t)
    return TensorDataset(torch.stack(xs), torch.stack(ys))


def acc(model, dl, adapter_ids):
    model.eval()
    ok = tot = 0
    with torch.no_grad():
        for x, y in dl:
            p = model(x, adapter_ids).argmax(-1)  # B,V -> B
            ok += (p == y[:, 0]).sum().item()
            tot += y.size(0)
    return ok / tot


# ── Main ──────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  CoTo Adapter Training — PoC")
    print("=" * 60)

    vocab = 32; seq = 8; hidden = 32
    epochs = 60; lr = 0.01; r = 4

    print(f"  vocab={vocab} hidden={hidden} seq={seq} r={r}")
    print(f"  epochs={epochs} lr={lr}")

    # Data
    d0 = make_task(0, vocab, seq, 400)
    d1 = make_task(1, vocab, seq, 400)
    tr0 = DataLoader(TensorDataset(d0.tensors[0][:300], d0.tensors[1][:300]), 32, shuffle=True)
    te0 = DataLoader(TensorDataset(d0.tensors[0][300:], d0.tensors[1][300:]), 32)
    tr1 = DataLoader(TensorDataset(d1.tensors[0][:300], d1.tensors[1][:300]), 32, shuffle=True)
    te1 = DataLoader(TensorDataset(d1.tensors[0][300:], d1.tensors[1][300:]), 32)

    # ═══ Phase 1: Isolated ═══
    print("\n── Phase 1: Isolated training ──")

    m = SimplePred(vocab, hidden)
    m.add_adapter(r); m.add_adapter(r)

    # Freeze base
    for p in m.W.parameters(): p.requires_grad = False
    # Freeze adapter 1
    for p in m.adapter_A[1].parameters(): p.requires_grad = False
    for p in m.adapter_B[1].parameters(): p.requires_grad = False

    # Train adapter 0 only on task 0
    opt0 = torch.optim.AdamW(
        list(m.adapter_A[0].parameters()) + list(m.adapter_B[0].parameters()),
        lr=lr
    )
    for ep in range(epochs):
        ls = 0.0
        for x, y in tr0:
            opt0.zero_grad()
            l = F.cross_entropy(m(x, [0]), y[:, 0].view(-1))  # predict pooled, compare to first token of target
            l.backward(); opt0.step(); ls += l.item()
        if (ep+1) % 15 == 0:
            a = acc(m, te0, [0])
            print(f"  adapter0 task0: ep{ep+1} loss={ls/len(tr0):.4f} acc={a:.4f}")
    a0_t0_iso = acc(m, te0, [0])
    a0_t1_iso = acc(m, te1, [0])
    print(f"  ✅ adapter0: task0={a0_t0_iso:.4f}  task1={a0_t1_iso:.4f}")

    # Now adapter 1 on task 1 (reset model)
    m2 = SimplePred(vocab, hidden)
    m2.add_adapter(r); m2.add_adapter(r)
    for p in m2.W.parameters(): p.requires_grad = False
    # Freeze adapter 0
    for p in m2.adapter_A[0].parameters(): p.requires_grad = False
    for p in m2.adapter_B[0].parameters(): p.requires_grad = False

    opt1 = torch.optim.AdamW(
        list(m2.adapter_A[1].parameters()) + list(m2.adapter_B[1].parameters()),
        lr=lr
    )
    for ep in range(epochs):
        ls = 0.0
        for x, y in tr1:
            opt1.zero_grad()
            l = F.cross_entropy(m2(x, [1]), y[:, 0].view(-1))
            l.backward(); opt1.step(); ls += l.item()
        if (ep+1) % 15 == 0:
            a = acc(m2, te1, [1])
            print(f"  adapter1 task1: ep{ep+1} loss={ls/len(tr1):.4f} acc={a:.4f}")
    a1_t1_iso = acc(m2, te1, [1])
    a1_t0_iso = acc(m2, te0, [1])
    print(f"  ✅ adapter1: task1={a1_t1_iso:.4f}  task0={a1_t0_iso:.4f}")

    # Merge baseline (average LoRA weights)
    print("\n  Merging isolated adapters...")
    merged = SimplePred(vocab, hidden)
    merged.add_adapter(r); merged.add_adapter(r)
    for p in merged.W.parameters(): p.requires_grad = False
    # Average adapter 0 from m and adapter 1 from m2 into adapter 0
    merged.adapter_A[0].weight.data.copy_(
        (m.adapter_A[0].weight.data + m2.adapter_A[1].weight.data) / 2.0
    )
    merged.adapter_B[0].weight.data.copy_(
        (m.adapter_B[0].weight.data + m2.adapter_B[1].weight.data) / 2.0
    )

    basem0 = acc(merged, te0, [0])
    basem1 = acc(merged, te1, [0])
    print(f"  Baseline merged: task0={basem0:.4f}  task1={basem1:.4f}  avg={(basem0+basem1)/2:.4f}")

    # ═══ Phase 2: CoTo ═══
    print("\n── Phase 2: CoTo (stochastic activation) ──")

    mc = SimplePred(vocab, hidden)
    mc.add_adapter(r); mc.add_adapter(r)
    for p in mc.W.parameters(): p.requires_grad = False

    # Both adapters trainable
    optc = torch.optim.AdamW(
        [p for p in mc.parameters() if p.requires_grad], lr=lr
    )

    co_p = 0.5
    print(f"  CoTo p={co_p}")
    for ep in range(epochs):
        ls0 = ls1 = 0.0; cnt0 = cnt1 = 0
        for (x0, y0), (x1, y1) in zip(tr0, tr1):
            optc.zero_grad()
            tl = 0.0
            # Task 0 — stochastic
            if random.random() < co_p:
                l = F.cross_entropy(mc(x0, [0]), y0[:, 0].view(-1))
                tl += l; ls0 += l.item(); cnt0 += 1
            # Task 1 — stochastic
            if random.random() < co_p:
                l = F.cross_entropy(mc(x1, [1]), y1[:, 0].view(-1))
                tl += l; ls1 += l.item(); cnt1 += 1
            if tl != 0:
                tl.backward()
                optc.step()
        if (ep+1) % 15 == 0:
            a0 = acc(mc, te0, [0]); a1 = acc(mc, te1, [1])
            print(f"  ep{ep+1}  t0={ls0/max(cnt0,1):.4f}  t1={ls1/max(cnt1,1):.4f}  acc0={a0:.4f}  acc1={a1:.4f}")

    coto0 = acc(mc, te0, [0]); coto1 = acc(mc, te1, [1])
    print(f"  ✅ CoTo individual: task0={coto0:.4f}  task1={coto1:.4f}")

    # Merge CoTo
    mc_merged = SimplePred(vocab, hidden)
    mc_merged.add_adapter(r); mc_merged.add_adapter(r)
    for p in mc_merged.W.parameters(): p.requires_grad = False
    mc_merged.adapter_A[0].weight.data.copy_(
        (mc.adapter_A[0].weight.data + mc.adapter_A[1].weight.data) / 2.0
    )
    mc_merged.adapter_B[0].weight.data.copy_(
        (mc.adapter_B[0].weight.data + mc.adapter_B[1].weight.data) / 2.0
    )

    cm0 = acc(mc_merged, te0, [0]); cm1 = acc(mc_merged, te1, [0])
    print(f"  ✅ CoTo merged: task0={cm0:.4f}  task1={cm1:.4f}  avg={(cm0+cm1)/2:.4f}")

    # ═══ Summary ═══
    print("\n" + "="*60)
    print("  RESULTS")
    print("="*60)
    rows = [
        ("Isolated Ad0",  a0_t0_iso, a0_t1_iso),
        ("Isolated Ad1",  a1_t0_iso, a1_t1_iso),
        ("Baseline Merged", basem0,  basem1),
        ("CoTo Individual", coto0,   coto1),
        ("CoTo Merged",    cm0,      cm1),
    ]
    for name, t0, t1 in rows:
        print(f"  {name:<20}  t0={t0:.4f}  t1={t1:.4f}  avg={(t0+t1)/2:.4f}")

    results = {
        "isolated_ad0": {"task0": a0_t0_iso, "task1": a0_t1_iso},
        "isolated_ad1": {"task0": a1_t0_iso, "task1": a1_t1_iso},
        "baseline_merged": {"task0": basem0, "task1": basem1},
        "coto_individual": {"task0": coto0, "task1": coto1},
        "coto_merged": {"task0": cm0, "task1": cm1},
    }
    with open("coto_results.json","w") as f: json.dump(results, f, indent=2)
    print(f"\n  ✅ Results → coto_results.json")


if __name__ == "__main__":
    main()
