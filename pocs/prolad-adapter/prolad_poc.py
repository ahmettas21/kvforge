#!/usr/bin/env python3
"""
CoTo (Come Together) Adapter Training PoC
=========================================
Stochastic activation multi-task LoRA training.

Idea: train multiple LoRA adapters simultaneously but stochastically
activate/deactivate per batch. This improves multi-task merging later.

Protocol:
  1. Two synthetic tasks (sequence reversal, different rules)
  2. Baseline: train adapters isolated, then merge (average)
  3. CoTo: train adapters together with stochastic activation, merge
  4. Compare merged accuracy
"""

import json, math, random
from copy import deepcopy
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset


@dataclass
class Config:
    vocab_size: int = 256
    hidden_size: int = 128
    num_layers: int = 4
    num_heads: int = 4
    ffn_size: int = 256
    max_seq: int = 32
    lora_r: int = 8
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    batch: int = 16
    epochs: int = 80
    lr: float = 1e-3
    wd: float = 1e-4
    seed: int = 42
    co_p: float = 0.5  # CoTo activation prob


# ── Model ─────────────────────────────────────────────────────

class LoRALin(nn.Module):
    def __init__(self, d_in, d_out, r, alpha, drop):
        super().__init__()
        self.lin = nn.Linear(d_in, d_out, bias=False)
        self.adapters: list = []  # list of (A, B, dropout)

    def add_adapter(self):
        r, alpha = Config.lora_r, Config.lora_alpha
        A = nn.Parameter(torch.randn(self.lin.in_features, r) / math.sqrt(r))
        B = nn.Parameter(torch.zeros(r, self.lin.out_features))
        drop = nn.Dropout(Config.lora_dropout)
        self.adapters.append((A, B, drop))
        # register params so they're tracked
        self.register_parameter(f"lora_A_{len(self.adapters)-1}", A)
        self.register_parameter(f"lora_B_{len(self.adapters)-1}", B)

    def forward(self, x, adapter_ids=None):
        """adapter_ids: list of adapter indices to activate, or None for all."""
        out = self.lin(x)
        if adapter_ids is None:
            adapter_ids = range(len(self.adapters))
        for i in adapter_ids:
            if i < len(self.adapters):
                A, B, drop = self.adapters[i]
                out += (drop(x) @ A @ B) * (Config.lora_alpha / Config.lora_r)
        return out


class MHA(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.hd = cfg.hidden_size // cfg.num_heads
        self.q = LoRALin(cfg.hidden_size, cfg.hidden_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.k = LoRALin(cfg.hidden_size, cfg.hidden_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.v = LoRALin(cfg.hidden_size, cfg.hidden_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.o = LoRALin(cfg.hidden_size, cfg.hidden_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)

    def add_adapter(self):
        for m in [self.q, self.k, self.v, self.o]:
            m.add_adapter()

    def forward(self, h, adapter=0):
        B, S, D = h.shape
        H = Config.num_heads; hd = self.hd
        q = self.q(h, [adapter]).view(B, S, H, hd).transpose(1, 2)
        k = self.k(h, [adapter]).view(B, S, H, hd).transpose(1, 2)
        v = self.v(h, [adapter]).view(B, S, H, hd).transpose(1, 2)
        mask = torch.triu(torch.full((S, S), float('-inf'), device=h.device, dtype=h.dtype), diagonal=1)
        a = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(hd) + mask.unsqueeze(0).unsqueeze(0)
        a = F.softmax(a, dim=-1).to(q.dtype)
        o = torch.matmul(a, v).transpose(1, 2).reshape(B, -1, D)
        return self.o(o, [adapter])


class Block(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.attn = MHA(cfg)
        self.gate = LoRALin(cfg.hidden_size, cfg.ffn_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.up = LoRALin(cfg.hidden_size, cfg.ffn_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.down = LoRALin(cfg.ffn_size, cfg.hidden_size, cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
        self.ln1 = nn.LayerNorm(cfg.hidden_size)
        self.ln2 = nn.LayerNorm(cfg.hidden_size)

    def add_adapter(self):
        self.attn.add_adapter()
        for m in [self.gate, self.up, self.down]:
            m.add_adapter()

    def forward(self, h, adapter=0):
        h = h + self.attn(self.ln1(h), adapter)
        h2 = self.ln2(h)
        return h + self.down(F.silu(self.gate(h2, [adapter])) * self.up(h2, [adapter]), [adapter])


class TinyLM(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.embed = nn.Embedding(cfg.vocab_size, cfg.hidden_size)
        self.blocks = nn.ModuleList([Block(cfg) for _ in range(cfg.num_layers)])
        self.ln = nn.LayerNorm(cfg.hidden_size)
        self.head = nn.Linear(cfg.hidden_size, cfg.vocab_size, bias=False)
        self.head.weight = self.embed.weight

    def add_adapter(self):
        for b in self.blocks:
            b.add_adapter()

    def set_adapter_grad(self, adapter_id: int, enabled: bool):
        """Enable/disable grad for specific adapter params."""
        tag = f"lora_A_{adapter_id}"
        tag2 = f"lora_B_{adapter_id}"
        for n, p in self.named_parameters():
            if tag in n or tag2 in n:
                p.requires_grad = enabled

    def zero_adapter(self, adapter_id: int):
        """Zero out a specific adapter's weights."""
        tag = f"lora_A_{adapter_id}"
        tag2 = f"lora_B_{adapter_id}"
        for n, p in self.named_parameters():
            if tag in n or tag2 in n:
                p.data.zero_()

    def forward(self, ids, adapter=0):
        h = self.embed(ids)
        for b in self.blocks:
            h = b(h, adapter)
        h = self.ln(h)
        return self.head(h)


# ── Data ──────────────────────────────────────────────────────

def make_task(tid: int, cfg, n=500):
    """Synthetic sequence reversal tasks."""
    S, vs = cfg.max_seq, cfg.vocab_size
    xs, ys = [], []
    for _ in range(n):
        s = torch.randint(10, vs, (S,))
        if tid == 0:
            o = s.clone(); o[2:S-2] = s[2:S-2].flip(0)
        else:
            o = s.clone(); o[1:S-1] = s[1:S-1].flip(0)
        xs.append(s); ys.append(o)
    return TensorDataset(torch.stack(xs), torch.stack(ys))


def evaluate(model, loader, cfg, adapter=0):
    model.eval()
    ok = tot = 0
    with torch.no_grad():
        for x, y in loader:
            p = model(x, adapter=adapter).argmax(-1)
            ok += (p == y).sum().item()
            tot += y.numel()
    return ok / tot


# ── Main ──────────────────────────────────────────────────────

def main():
    cfg = Config()
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"  Device: {dev} | Seed: {cfg.seed}")
    torch.manual_seed(cfg.seed); random.seed(cfg.seed)

    # Build model with 2 adapters
    model = TinyLM(cfg).to(dev)
    model.add_adapter(); model.add_adapter()

    n_base = sum(p.numel() for n, p in model.named_parameters() if 'lora' not in n)
    n_lora = sum(p.numel() for n, p in model.named_parameters() if 'lora' in n)
    print(f"  Base: {n_base:,} | LoRA: {n_lora:,}")

    # Data
    d0 = make_task(0, cfg, 400)
    d1 = make_task(1, cfg, 400)
    tr0 = DataLoader(TensorDataset(d0.tensors[0][:300], d0.tensors[1][:300]), cfg.batch, shuffle=True)
    te0 = DataLoader(TensorDataset(d0.tensors[0][300:], d0.tensors[1][300:]), cfg.batch)
    tr1 = DataLoader(TensorDataset(d1.tensors[0][:300], d1.tensors[1][:300]), cfg.batch, shuffle=True)
    te1 = DataLoader(TensorDataset(d1.tensors[0][300:], d1.tensors[1][300:]), cfg.batch)

    # ═══════════ Phase 1: Isolated training ═══════════
    print("\n── Phase 1: Isolated (baseline) ──")

    # Adapter 0 on task 0
    m0 = deepcopy(model)
    m0.zero_adapter(1); m0.set_adapter_grad(1, False)
    m0.set_adapter_grad(0, True)
    for n, p in m0.named_parameters():
        if 'lora' not in n: p.requires_grad = False
    opt0 = torch.optim.AdamW([p for p in m0.parameters() if p.requires_grad], lr=cfg.lr, weight_decay=cfg.wd)

    print("  Training adapter 0 on task 0...")
    for ep in range(cfg.epochs):
        ls = 0.0
        for x, y in tr0:
            opt0.zero_grad()
            l = F.cross_entropy(m0(x, adapter=0).view(-1, cfg.vocab_size), y.view(-1))
            l.backward(); torch.nn.utils.clip_grad_norm_(m0.parameters(), 1.0); opt0.step()
            ls += l.item()
        if (ep+1) % 20 == 0:
            a = evaluate(m0, te0, cfg, 0)
            print(f"    ep{ep+1}  loss={ls/len(tr0):.4f}  acc0={a:.4f}")

    a0_iso = evaluate(m0, te0, cfg, 0)
    a0_x = evaluate(m0, te1, cfg, 0)
    print(f"  adapter0:  task0={a0_iso:.4f}  task1={a0_x:.4f}")

    # Adapter 1 on task 1
    m1 = deepcopy(model)
    m1.zero_adapter(0); m1.set_adapter_grad(0, False)
    m1.set_adapter_grad(1, True)
    for n, p in m1.named_parameters():
        if 'lora' not in n: p.requires_grad = False
    opt1 = torch.optim.AdamW([p for p in m1.parameters() if p.requires_grad], lr=cfg.lr, weight_decay=cfg.wd)

    print("  Training adapter 1 on task 1...")
    for ep in range(cfg.epochs):
        ls = 0.0
        for x, y in tr1:
            opt1.zero_grad()
            l = F.cross_entropy(m1(x, adapter=1).view(-1, cfg.vocab_size), y.view(-1))
            l.backward(); torch.nn.utils.clip_grad_norm_(m1.parameters(), 1.0); opt1.step()
            ls += l.item()
        if (ep+1) % 20 == 0:
            a = evaluate(m1, te1, cfg, 1)
            print(f"    ep{ep+1}  loss={ls/len(tr1):.4f}  acc1={a:.4f}")

    a1_iso = evaluate(m1, te1, cfg, 1)
    a1_x = evaluate(m1, te0, cfg, 1)
    print(f"  adapter1:  task1={a1_iso:.4f}  task0={a1_x:.4f}")

    # Merge (simple average of LoRA deltas)
    print("\n  Merging isolated adapters...")
    merged = deepcopy(model)
    for n, p in merged.named_parameters():
        if 'lora_A_0' in n:
            n0 = next((v for k, v in m0.named_parameters() if k == n), None)
            n1 = next((v for k, v in m1.named_parameters() if k == n.replace('_0_', '_1_')), None)
            if n0 is not None and n1 is not None:
                p.data.copy_((n0.data + n1.data) / 2.0)
        elif 'lora_B_0' in n:
            n0 = next((v for k, v in m0.named_parameters() if k == n), None)
            n1 = next((v for k, v in m1.named_parameters() if k == n.replace('_0_', '_1_')), None)
            if n0 is not None and n1 is not None:
                p.data.copy_((n0.data + n1.data) / 2.0)

    base_m0 = evaluate(merged, te0, cfg, 0)
    base_m1 = evaluate(merged, te1, cfg, 0)
    print(f"  Merged: task0={base_m0:.4f}  task1={base_m1:.4f}  avg={(base_m0+base_m1)/2:.4f}")

    # ═══════════ Phase 2: CoTo training ═══════════
    print("\n── Phase 2: CoTo (stochastic activation) ──")

    mc = TinyLM(cfg).to(dev)
    mc.add_adapter(); mc.add_adapter()
    for n, p in mc.named_parameters():
        p.requires_grad = 'lora' in n

    optc = torch.optim.AdamW([p for p in mc.parameters() if p.requires_grad], lr=cfg.lr, weight_decay=cfg.wd)

    print(f"  CoTo p={cfg.co_p} (prob to keep adapter active)")
    for ep in range(cfg.epochs):
        ls = [0.0, 0.0]; cnt = [0, 0]
        for (x0, y0), (x1, y1) in zip(tr0, tr1):
            optc.zero_grad()
            tl = 0.0
            for tid, (x, y) in enumerate([(x0, y0), (x1, y1)]):
                if random.random() < cfg.co_p:
                    l = F.cross_entropy(mc(x, adapter=tid).view(-1, cfg.vocab_size), y.view(-1))
                    tl += l
                    ls[tid] += l.item(); cnt[tid] += 1
            if tl != 0:
                tl.backward()
                torch.nn.utils.clip_grad_norm_(mc.parameters(), 1.0)
                optc.step()
        if (ep+1) % 20 == 0:
            a0 = evaluate(mc, te0, cfg, 0)
            a1 = evaluate(mc, te1, cfg, 1)
            print(f"    ep{ep+1}  t0={ls[0]/max(cnt[0],1):.4f}  t1={ls[1]/max(cnt[1],1):.4f}  acc0={a0:.4f}  acc1={a1:.4f}")

    coto0 = evaluate(mc, te0, cfg, 0)
    coto1 = evaluate(mc, te1, cfg, 1)
    print(f"  CoTo individual: task0={coto0:.4f}  task1={coto1:.4f}")

    # Merge CoTo adapters
    mc_merge = deepcopy(mc)
    for n, p in mc_merge.named_parameters():
        if 'lora_A_0' in n:
            p0 = next((v for k,v in mc.named_parameters() if k == n), None)
            p1 = next((v for k,v in mc.named_parameters() if k == n.replace('_0_','_1_')), None)
            if p0 is not None and p1 is not None:
                p.data.copy_((p0.data + p1.data) / 2.0)
        elif 'lora_B_0' in n:
            p0 = next((v for k,v in mc.named_parameters() if k == n), None)
            p1 = next((v for k,v in mc.named_parameters() if k == n.replace('_0_','_1_')), None)
            if p0 is not None and p1 is not None:
                p.data.copy_((p0.data + p1.data) / 2.0)

    cm0 = evaluate(mc_merge, te0, cfg, 0)
    cm1 = evaluate(mc_merge, te1, cfg, 0)
    print(f"  CoTo Merged: task0={cm0:.4f}  task1={cm1:.4f}  avg={(cm0+cm1)/2:.4f}")

    # ═══════════╤══════════════════════════════════════════
    print("\n" + "="*60)
    print("  RESULTS")
    print("="*60 + "\n")
    for row in [
        ("Isolated Adapter 0",   a0_iso,   a0_x,   (a0_iso+a0_x)/2),
        ("Isolated Adapter 1",   a1_x,    a1_iso,  (a1_x+a1_iso)/2),
        ("Baseline Merged",      base_m0, base_m1, (base_m0+base_m1)/2),
        ("CoTo Individual",      coto0,   coto1,   (coto0+coto1)/2),
        ("CoTo Merged",          cm0,     cm1,     (cm0+cm1)/2),
    ]:
        print(f"  {row[0]:<25}  task0={row[1]:.4f}  task1={row[2]:.4f}  avg={row[3]:.4f}")

    results = {
        "config": {"hidden_size":cfg.hidden_size,"layers":cfg.num_layers,"lora_r":cfg.lora_r,
                    "epochs":cfg.epochs,"co_p":cfg.co_p},
        "isolated_adapter0": {"task0":a0_iso,"task1":a0_x},
        "isolated_adapter1": {"task0":a1_x,"task1":a1_iso},
        "baseline_merged": {"task0":base_m0,"task1":base_m1},
        "coto_individual": {"task0":coto0,"task1":coto1},
        "coto_merged": {"task0":cm0,"task1":cm1},
    }
    with open("coto_results.json","w") as f: json.dump(results, f, indent=2)
    print(f"\n  Results → coto_results.json  ✅")


if __name__ == "__main__":
    main()
