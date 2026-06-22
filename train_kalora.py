import sys, math, time, os, warnings
warnings.filterwarnings('ignore')
import torch, torch.nn as nn, torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer
from kvforge.core import RandomSVD

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Device: {device}")

def ultra_compress(k, v, rank=2):
    B,H,S,D = k.shape; r = min(rank,S,D)
    k2,v2 = k.reshape(-1,S,D), v.reshape(-1,S,D)
    Uk,Sk,Vhk = RandomSVD.compute(k2, r)
    Uv,Sv,Vhv = RandomSVD.compute(v2, r)
    Klr = (Uk*Sk.unsqueeze(-2)@Vhk).reshape(B,H,S,D)
    cb = (Uk.numel()+Sk.numel()+Vhk.numel()+Uv.numel()+Sv.numel()+Vhv.numel())*2
    return Klr, (k.numel()+v.numel())*2/cb if cb>0 else 1.0

def get_kv(past):
    if hasattr(past, 'key_cache'):
        return past.key_cache[0], past.value_cache[0]
    if hasattr(past, 'to_tuple'):
        t = past.to_tuple(); return t[0][0], t[0][1]
    if isinstance(past, (tuple,list)):
        if isinstance(past[0], (tuple,list)):
            return past[0][0], past[0][1]
        return past[0], past[1]
    items = list(past)
    return items[0][0] if isinstance(items[0],(tuple,list)) else items[0], items[0][1] if isinstance(items[0],(tuple,list)) else items[1]

class KALoRAConv1D(nn.Module):
    def __init__(self, orig, r=8, alpha=16.0):
        super().__init__()
        self.orig = orig; self.scaling = alpha/r
        self.lora_A = nn.Parameter(torch.randn(orig.weight.shape[0], r)*0.02)
        self.lora_B = nn.Parameter(torch.zeros(r, orig.nf))
        self.restore_W = nn.Parameter(torch.zeros(r, 64))  # (r, head_dim)
        self.active = True
    def activate(self, a=True): self.active = a
    def forward(self, x):
        h = self.orig(x)
        if self.active:
            h = h + (x @ self.lora_A @ self.lora_B) * self.scaling
        return h
    def restore_kv(self, kv_compressed):
        if not self.active: return kv_compressed
        D = kv_compressed.shape[-1]
        A_sub = self.lora_A[:D, :]
        W_sub = self.restore_W[:, :D]
        correction = kv_compressed @ A_sub @ W_sub
        return kv_compressed + correction * self.scaling

def train_kalora(model_name='gpt2', lora_rank=8, steps=200, lr=3e-3, restore_lambda=0.3):
    print(f"\nKALoRA Training: {model_name} | rank={lora_rank} | lambda={restore_lambda}")
    base = AutoModelForCausalLM.from_pretrained(model_name).to(device).train()
    tok = AutoTokenizer.from_pretrained(model_name)
    tok.pad_token = tok.eos_token

    kaloras = []
    for n, m in base.named_modules():
        if n.endswith('.attn.c_attn') or n.endswith('.attn.c_proj'):
            p, ch = base, n.split('.')[-1]
            for pt in n.split('.')[:-1]:
                if pt: p = getattr(p, pt)
            kalora = KALoRAConv1D(m, r=lora_rank, alpha=16.0)
            setattr(p, ch, kalora)
            kaloras.append(kalora)

    gp = sum(p.numel() for n,p in base.named_parameters() if 'lora' in n)
    rp = sum(p.numel() for n,p in base.named_parameters() if 'restore' in n)
    print(f"Gen params: {gp:,} | Restore params: {rp:,} | Total: {gp+rp:,}")

    optim = torch.optim.AdamW(
        [p for n,p in base.named_parameters() if 'lora' in n or 'restore' in n],
        lr=lr)

    prompt = ("The transformer architecture revolutionized NLP by introducing "
              "self-attention mechanisms. This allowed models to process entire "
              "sequences in parallel rather than sequentially.")
    inp = tok(prompt, return_tensors='pt', truncation=True, max_length=128).to(device)
    ids = inp['input_ids']
    print(f"Prompt: {ids.shape[1]} tokens")

    for step in range(steps):
        base.zero_grad()
        out = base(ids, use_cache=True)
        past = out.past_key_values
        full_k, _ = get_kv(past)
        k_lr, cr = ultra_compress(full_k, full_k, rank=2)

        loss_gen = F.cross_entropy(out.logits[0, :-1], ids[0, 1:])

        kalora = kaloras[0]
        restored = kalora.restore_kv(k_lr.reshape(-1, k_lr.shape[-1])).reshape(full_k.shape)
        loss_restore = F.mse_loss(restored, full_k.detach())

        loss = (1 - restore_lambda) * loss_gen + restore_lambda * loss_restore
        loss.backward()
        torch.nn.utils.clip_grad_norm_([p for n,p in base.named_parameters() if 'lora' in n or 'restore' in n], 1.0)
        optim.step()

        if step % 20 == 0 or step == steps-1:
            with torch.no_grad():
                mse_before = F.mse_loss(k_lr, full_k).item()
                mse_after = F.mse_loss(restored, full_k).item()
                imp = max(0, (1 - mse_after/max(mse_before,1e-10)))*100
                ppl = math.exp(min(loss_gen.item(), 20))
            print(f"  step {step:3d} | gen={loss_gen.item():.4f} | restore={loss_restore.item():.6f} | "
                  f"PPL={ppl:.2f} | MSE: {mse_before:.4f}->{mse_after:.4f} ({imp:.1f}%) | CR={cr:.1f}x")

    torch.save({n:p for n,p in base.named_parameters() if 'lora' in n or 'restore' in n}, 'kalora_gpt2.pt')
    print(f"\nFinal: gen params={gp:,} | restore params={rp:,}")
    print(f"Overhead: {rp/gp*100:.1f}%")
    return base, kaloras

if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv)>1 else 200
    l = float(sys.argv[2]) if len(sys.argv)>2 else 0.3
    train_kalora(steps=s, restore_lambda=l)