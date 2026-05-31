"""
KVForge v7 — GPT-Neo 1.3B (fix: recon_lambda=0.001)
===========================================================
- recon_lambda 0.05 → 0.001 (CE loss baskın kalsın)
- Model fp32, forward autocast(fp16), GradScaler
- Adafactor optimizer (low memory)
- seq_len=256, batch=1, grad_accum=8
"""

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
import torch
import torch.nn as nn
import torch.nn.functional as F

GPTNEO_CONFIG = {
    'vocab_size': 50272,
    'hidden_size': 2048,
    'num_layers': 24,
    'num_heads': 16,
    'head_dim': 2048 // 16,
    'max_position_embeddings': 2048,
    'seed_dim': 64,
    'd_ff': 2048 * 4,
    'dropout': 0.1,
    'layer_norm_epsilon': 1e-5,
}

class ContextualSeedAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        d_model = config['hidden_size']; n_heads = config['num_heads']
        head_dim = config['head_dim']; seed_dim = config['seed_dim']
        self.d_model = d_model; self.n_heads = n_heads
        self.head_dim = head_dim; self.seed_dim = seed_dim
        self.scale = 1.0 / math.sqrt(head_dim)
        self.q_proj = nn.Linear(d_model, d_model, bias=False)
        self.k_proj = nn.Linear(d_model, d_model, bias=False)
        self.v_proj = nn.Linear(d_model, d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model, bias=False)
        self.seed_encoder = nn.Sequential(nn.Linear(4*d_model, 512), nn.GELU(), nn.Linear(512, seed_dim))
        self.seed_norm = nn.LayerNorm(seed_dim)
        self.seed_decoder = nn.Sequential(nn.Linear(seed_dim, 512), nn.GELU(), nn.Linear(512, 2*d_model))
        self.dropout = nn.Dropout(config['dropout'])

    def _compress_kv(self, k, v):
        B,T,D = k.shape
        kp = torch.cat([torch.zeros_like(k[:,:1,:]), k[:,:-1,:]], dim=1)
        vp = torch.cat([torch.zeros_like(v[:,:1,:]), v[:,:-1,:]], dim=1)
        return self.seed_norm(self.seed_encoder(torch.cat([kp,vp,k,v], dim=-1)))

    def _split_heads(self, x):
        B,T,_ = x.shape
        return x.view(B,T,self.n_heads,self.head_dim).transpose(1,2)
    def _merge_heads(self, x):
        return x.transpose(1,2).contiguous().view(x.size(0), x.size(2), self.d_model)

    def forward(self, x, return_seed=False):
        B,T,_ = x.shape
        q = self.q_proj(x); ko = self.k_proj(x); vo = self.v_proj(x)
        seed = self._compress_kv(ko, vo)
        kvr = self.seed_decoder(seed); k,v = kvr.chunk(2, dim=-1)
        q,k,v = self._split_heads(q), self._split_heads(k), self._split_heads(v)
        attn = torch.matmul(q, k.transpose(-2,-1)) * self.scale
        causal = torch.triu(torch.ones(T,T,device=x.device), diagonal=1).bool()
        attn = attn.masked_fill(causal.unsqueeze(0).unsqueeze(0), float('-inf'))
        attn = F.softmax(attn, dim=-1); attn = self.dropout(attn)
        out = self._merge_heads(torch.matmul(attn, v)); out = self.out_proj(out)
        if return_seed:
            return out, seed, F.mse_loss(kvr, torch.cat([ko,vo], dim=-1).detach())
        return out

class GPTNeoBlockV2(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.ln1 = nn.LayerNorm(config['hidden_size'], eps=config['layer_norm_epsilon'])
        self.attn = ContextualSeedAttention(config)
        self.ln2 = nn.LayerNorm(config['hidden_size'], eps=config['layer_norm_epsilon'])
        self.mlp = nn.Sequential(nn.Linear(config['hidden_size'], config['d_ff']), nn.GELU(),
            nn.Dropout(config['dropout']), nn.Linear(config['d_ff'], config['hidden_size']), nn.Dropout(config['dropout']))

    def forward(self, x, return_seed=False):
        a = self.ln1(x)
        if return_seed: a,seed,recon = self.attn(a, return_seed=True)
        else: a = self.attn(a); recon = None
        x = x + a; x = x + self.mlp(self.ln2(x))
        if return_seed: return x,seed,recon
        return x

class KVForgeGPTNeoV2(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.token_embed = nn.Embedding(config['vocab_size'], config['hidden_size'])
        self.pos_embed = nn.Embedding(config['max_position_embeddings'], config['hidden_size'])
        self.dropout = nn.Dropout(config['dropout'])
        self.blocks = nn.ModuleList([GPTNeoBlockV2(config) for _ in range(config['num_layers'])])
        self.ln_f = nn.LayerNorm(config['hidden_size'], eps=config['layer_norm_epsilon'])
        self.head = nn.Linear(config['hidden_size'], config['vocab_size'], bias=False)
        self.token_embed.weight = self.head.weight
        # FIX: recon_lambda 0.05 → 0.001
        self.recon_lambda = 0.001
        self._init_weights()

    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0.0, 0.02)
                if m.bias is not None: nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Embedding): nn.init.normal_(m.weight, 0.0, 0.02)
            elif isinstance(m, nn.LayerNorm): nn.init.ones_(m.weight); nn.init.zeros_(m.bias)

    def forward(self, input_ids, labels=None, return_seed=False):
        B,T = input_ids.shape
        x = self.token_embed(input_ids) + self.pos_embed(torch.arange(T, device=input_ids.device).unsqueeze(0))
        x = self.dropout(x)
        total_recon = 0.0
        for block in self.blocks:
            if return_seed: x,_,recon = block(x, return_seed=True); total_recon += recon
            else: x = block(x)
        x = self.ln_f(x); logits = self.head(x)
        loss = None; recon_val = None
        if labels is not None:
            sl,slb = logits[:,:-1,:].contiguous(), labels[:,1:].contiguous()
            ce = F.cross_entropy(sl.view(-1, sl.size(-1)), slb.view(-1), ignore_index=-100)
            loss = ce
            if return_seed:
                recon_val = (total_recon / len(self.blocks)).item()
                loss = ce + self.recon_lambda * recon_val
        return loss, logits, recon_val

    def count_parameters(self):
        total = sum(p.numel() for p in self.parameters())
        trainable = sum(p.numel() for p in self.parameters() if p.requires_grad)
        return total, trainable

# ============================================================
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2Tokenizer

class TextDataset(Dataset):
    def __init__(self, tokenizer, text_path, seq_len=256, max_samples=None):
        self.seq_len = seq_len
        with open(text_path,'r') as f: text = f.read()
        tokens = tokenizer.encode(text)
        print(f"  Tokenler: {len(tokens):,}")
        self.examples = []
        for i in range(0, len(tokens)-seq_len, seq_len):
            chunk = tokens[i:i+seq_len]
            if len(chunk)==seq_len: self.examples.append(torch.tensor(chunk, dtype=torch.long))
        if max_samples and len(self.examples)>max_samples: self.examples = self.examples[:max_samples]
        print(f"  Ornek: {len(self.examples)}")
    def __len__(self): return len(self.examples)
    def __getitem__(self, idx): return self.examples[idx]

# ============================================================
def train():
    print("="*60); print("KVForge v7 — GPT-Neo 1.3B (recon_lambda=0.001)"); print("="*60)

    DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {DEVICE}")
    if DEVICE.type=='cuda': print(f"GPU: {torch.cuda.get_device_name(0)}"); print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

    config = dict(GPTNEO_CONFIG); SEQ_LEN=256; BATCH_SIZE=1; LR=1e-4; NUM_EPOCHS=3; GRAD_ACCUM=8; MAX_STEPS=1000
    print(f"\n  Seq: {SEQ_LEN}, Batch: {BATCH_SIZE}, Accum: {GRAD_ACCUM}, Eff: {BATCH_SIZE*GRAD_ACCUM}")
    print(f"  recon_lambda: {KVForgeGPTNeoV2(config).recon_lambda} (FIX: 0.05→0.001)")

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2'); tokenizer.pad_token = tokenizer.eos_token
    ds = TextDataset(tokenizer, '/kaggle/working/wikitext.txt', seq_len=SEQ_LEN, max_samples=10000)
    train_ds = [x for i,x in enumerate(ds) if i%10!=0]
    val_ds = [x for i,x in enumerate(ds) if i%10==0 and i>0]
    print(f"Train: {len(train_ds)}, Val: {len(val_ds)}")
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True, num_workers=2, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=1, num_workers=2, pin_memory=True)

    model = KVForgeGPTNeoV2(config).to(DEVICE)
    total,_ = model.count_parameters()
    print(f"\nModel: {total/1e6:.1f}M total")
    model.train()

    from transformers.optimization import Adafactor
    opt = Adafactor(model.parameters(), lr=LR, weight_decay=0.01, scale_parameter=True, relative_step=False, warmup_init=False)
    total_steps = min(len(train_loader)*NUM_EPOCHS, MAX_STEPS)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=total_steps, eta_min=1e-6)
    scaler = torch.amp.GradScaler('cuda')

    t_start=time.time(); best_loss=float('inf'); global_step=0
    for epoch in range(NUM_EPOCHS):
        model.train(); opt.zero_grad()
        for bidx, batch in enumerate(train_loader):
            if global_step>=MAX_STEPS: break
            batch = batch.to(DEVICE, non_blocking=True)
            with torch.amp.autocast('cuda'): loss,_,recon = model(batch, labels=batch, return_seed=True)
            loss = loss/GRAD_ACCUM; scaler.scale(loss).backward()
            if (bidx+1)%GRAD_ACCUM==0:
                scaler.unscale_(opt)
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                scaler.step(opt); scaler.update(); opt.zero_grad(); scheduler.step()
                global_step += 1
                if global_step%10==0:
                    elapsed=time.time()-t_start; mem=torch.cuda.max_memory_allocated()/1e9 if DEVICE.type=='cuda' else 0
                    lv=loss.item()*GRAD_ACCUM; rv=recon if recon is not None else 0.0
                    nf=" ⚠️NAN" if math.isnan(lv) else ""
                    print(f"E{epoch}|S{global_step:4d}/{total_steps} L={lv:.4f} R={rv:.5f} Mem={mem:.1f}GiB ({elapsed:.0f}s){nf}")
            if DEVICE.type=='cuda' and bidx%20==0: torch.cuda.empty_cache(); gc.collect()

        model.eval(); val_loss=0.0; val_steps=0
        with torch.no_grad():
            for batch in val_loader:
                if val_steps>=50: break
                batch=batch.to(DEVICE, non_blocking=True)
                with torch.amp.autocast('cuda'): l,_,_ = model(batch, labels=batch, return_seed=True)
                val_loss+=l.item(); val_steps+=1
        val_loss/=max(val_steps,1); val_ppl=math.exp(min(val_loss,20))
        elapsed=time.time()-t_start; max_mem=torch.cuda.max_memory_allocated()/1e9 if DEVICE.type=='cuda' else 0
        print(f"\n  → Epoch {epoch+1} ({elapsed:.0f}s, max_mem={max_mem:.1f}GiB): Val L={val_loss:.4f} PPL={val_ppl:.1f}")
        if val_loss<best_loss and not math.isnan(val_loss):
            best_loss=val_loss; torch.save(model.state_dict(), '/kaggle/working/kvforge_gptneo_best.pt')

    total_time=time.time()-t_start
    best_ppl=math.exp(min(best_loss,20)) if not math.isnan(best_loss) and best_loss!=float('inf') else 999999.9
    print(f"\n✅ KVForge v7 tamam! {total_time:.0f}s ({total_time/60:.1f} dk) Best PPL: {best_ppl:.1f}")

    results = {
        'model': 'KVForge v7 GPT-Neo 1.3B',
        'config': {'layers':24,'heads':16,'hidden':2048,'seed_dim':64,'seed_encoder_hidden':512,
            'compression':'64×','optimizer':'Adafactor','recon_lambda':0.001,
            'dtype':'fp32+autocast','seq_len':SEQ_LEN,'batch_size':BATCH_SIZE,
            'grad_accum':GRAD_ACCUM,'eff_batch':8,'max_steps':min(MAX_STEPS,global_step),'lr':LR},
        'results': {'best_val_loss':best_loss,'best_val_ppl':round(best_ppl,1),
            'training_time_min':round(total_time/60,1),'total_params':total}
    }
    with open('/kaggle/working/kvforge_gptneo_results.json','w') as f: json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))

if __name__=='__main__': train()
