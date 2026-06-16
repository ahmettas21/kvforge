"""
KvForge Core — HuggingFace model wrapper with LoRA injection,
Base Encode + LoRA Decode pattern, and KV Cache compression.
"""

import math, time
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Union, List, Tuple

try:
    from transformers import PreTrainedModel, AutoModelForCausalLM
    from transformers.cache_utils import DynamicCache
    HAS_HF = True
except ImportError:
    HAS_HF = False

# ── LoRA Wrappers ──────────────────────────────────────────

class LoRAConv1D(nn.Module):
    """LoRA for HuggingFace GPT-2's Conv1D (c_attn/c_proj)."""
    def __init__(self, orig: nn.Module, r: int = 8, alpha: float = 16.0):
        super().__init__()
        self.orig = orig
        self.scaling = alpha / r
        in_f = orig.weight.shape[0]
        out_f = orig.nf
        self.lora_A = nn.Parameter(torch.randn(in_f, r) * 0.02)
        self.lora_B = nn.Parameter(torch.zeros(r, out_f))
        self.active = False

    def activate(self, a: bool = True):
        self.active = a

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.orig(x)
        if self.active:
            h = h + (x @ self.lora_A @ self.lora_B) * self.scaling
        return h


class LoRALinear(nn.Module):
    """LoRA for standard nn.Linear layers."""
    def __init__(self, orig: nn.Linear, r: int = 8, alpha: float = 16.0):
        super().__init__()
        self.orig = orig
        self.scaling = alpha / r
        self.lora_A = nn.Parameter(torch.randn(orig.in_features, r) * 0.02)
        self.lora_B = nn.Parameter(torch.zeros(r, orig.out_features))
        self.active = False

    def activate(self, a: bool = True):
        self.active = a

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.orig(x)
        if self.active:
            h = h + (x @ self.lora_A @ self.lora_B) * self.scaling
        return h


# ── Model Wrapper ──────────────────────────────────────────

class KvForgeModel:
    """
    Wraps a HuggingFace CausalLM model with:
    - LoRA injection into attention projections
    - Base Encode + LoRA Decode mode switching
    - KV Cache quantization support
    """

    def __init__(
        self,
        model_name: str = "gpt2",
        lora_rank: int = 8,
        lora_alpha: float = 16.0,
        device: str = "cpu",
    ):
        if not HAS_HF:
            raise ImportError("transformers required for KvForgeModel")
        self.device = device
        self.model_name = model_name
        self.lora_rank = lora_rank
        self.lora_alpha = lora_alpha

        # Load base model
        self.base = AutoModelForCausalLM.from_pretrained(model_name).to(device).eval()
        self.tokenizer = None  # lazy load
        self._n_layers = self.base.config.n_layer if hasattr(self.base.config, 'n_layer') else self.base.config.num_hidden_layers

        # Inject LoRA
        self._inject_lora(r=lora_rank, alpha=lora_alpha)

    def _load_tokenizer(self):
        if self.tokenizer is None:
            from transformers import AutoTokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def _inject_lora(self, r: int, alpha: float):
        """Inject LoRA wrappers into attention projections."""
        count = 0
        for n, m in self.base.named_modules():
            # GPT-2 style (Conv1D)
            if n.endswith(".attn.c_attn") or n.endswith(".attn.c_proj"):
                parent = self.base
                parts = n.split(".")
                child = parts[-1]
                for p in parts[:-1]:
                    if p: parent = getattr(parent, p)
                setattr(parent, child, LoRAConv1D(m, r=r, alpha=alpha))
                count += 1
            # Llama/Mistral style (nn.Linear)
            elif any(n.endswith(s) for s in [".q_proj", ".k_proj", ".v_proj", ".o_proj"]):
                if isinstance(m, nn.Linear) and not isinstance(m, LoRALinear):
                    parent = self.base
                    parts = n.split(".")
                    child = parts[-1]
                    for p in parts[:-1]:
                        if p: parent = getattr(parent, p)
                    setattr(parent, child, LoRALinear(m, r=r, alpha=alpha))
                    count += 1
        print(f"[KvForge] LoRA injected: {count} modules")

    def set_mode(self, mode: str):
        """
        Set inference mode.
        - 'full_lora': LoRA active during both prefill and decode
        - 'base_encode': LoRA off during prefill
        - 'lora_decode': LoRA on during decode (call before decode)
        - 'off': LoRA off everywhere
        """
        if mode == 'full_lora':
            self._set_lora(True)
        elif mode == 'base_encode':
            self._set_lora(False)
        elif mode == 'lora_decode':
            self._set_lora(True)
        elif mode == 'off':
            self._set_lora(False)
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def _set_lora(self, active: bool):
        for mod in self.base.modules():
            if hasattr(mod, 'activate'):
                mod.activate(active)

    @torch.no_grad()
    def prefill(self, input_ids: torch.Tensor) -> Tuple:
        """Run prefill, return KV cache."""
        out = self.base.generate(
            input_ids=input_ids,
            max_new_tokens=1,
            use_cache=True,
            pad_token_id=self.tokenizer.eos_token_id if self.tokenizer else None,
            do_sample=False,
            return_dict_in_generate=True,
        )
        return out.past_key_values, out.sequences

    @torch.no_grad()
    def decode(self, last_token: torch.Tensor, past: Tuple, n_tokens: int = 12) -> Tuple:
        """Autoregressive decode with optional LoRA."""
        for _ in range(n_tokens):
            out = self.base(last_token, past_key_values=past, use_cache=True)
            past = out.past_key_values
            last_token = out.logits[:, -1:].argmax(dim=-1)
        return last_token, past

    @torch.no_grad()
    def generate(
        self,
        text: str,
        max_new_tokens: int = 20,
        mode: str = 'full_lora',
        compress_bits: int = 16,
        return_ppl: bool = False,
    ) -> dict:
        """End-to-end generation with mode selection."""
        self._load_tokenizer()
        inp = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=128).to(self.device)
        inp_ids = inp["input_ids"]

        # Prefill
        self.set_mode('base_encode' if mode == 'base_encode_lora_decode' else 'full_lora')
        t0 = time.time()
        past, seq = self.prefill(inp_ids)
        tp = time.time() - t0

        # Compress
        if compress_bits < 16:
            past = self._compress_past(past, compress_bits)

        # Decode
        if mode == 'base_encode_lora_decode':
            self.set_mode('lora_decode')
        t0 = time.time()
        last_tok = seq[:, -1:]
        self.decode(last_tok, past, n_tokens=max_new_tokens)
        td = time.time() - t0
        self.set_mode('off')

        # PPL
        ppl = 0.0
        if return_ppl:
            with torch.no_grad():
                out = self.base(inp_ids)
            loss = F.cross_entropy(out.logits[0, :-1, :], inp_ids[0, 1:])
            ppl = math.exp(loss.item())

        return {
            "mode": mode,
            "compress_bits": compress_bits,
            "prefill_ms": round(tp * 1000, 2),
            "decode_ms": round(td * 1000, 2),
            "total_ms": round((tp + td) * 1000, 2),
            "perplexity": round(ppl, 4),
        }

    @torch.no_grad()
    def _compress_past(self, past, bits: int) -> object:
        """Quantize KV cache to specified bits, return DynamicCache."""
        if bits >= 16:
            return past
        dc = DynamicCache()
        for li, layer in enumerate(past):
            k, v = layer[0], layer[1]
            # Quantize K
            mnk, mxk = k.min(-1, True).values, k.max(-1, True).values
            sk = (mxk - mnk).clamp(1e-8) / (2**bits - 1)
            dk = (((k - mnk) / sk).round().clamp(0, 2**bits - 1).float() * sk + mnk).to(k.dtype)
            # Quantize V
            mnv, mxv = v.min(-1, True).values, v.max(-1, True).values
            sv = (mxv - mnv).clamp(1e-8) / (2**bits - 1)
            dv = (((v - mnv) / sv).round().clamp(0, 2**bits - 1).float() * sv + mnv).to(v.dtype)
            dc.update(dk, dv, dk.size(2))
        return dc

    @torch.no_grad()
    def benchmark(self, texts: List[str], modes: List[str] = None,
                  compress_bits_list: List[int] = None) -> List[dict]:
        """Run benchmark across modes and compression levels."""
        if modes is None:
            modes = ['full_lora', 'base_encode_lora_decode']
        if compress_bits_list is None:
            compress_bits_list = [16, 8, 4, 2]

        self._load_tokenizer()
        results = []

        for text in texts:
            for mode in modes:
                for bits in compress_bits_list:
                    r = self.generate(text, max_new_tokens=12, mode=mode,
                                      compress_bits=bits, return_ppl=True)
                    r["text_sample"] = text[:40]
                    results.append(r)
                    print(f"  {mode:<25} {bits:>2}bit  "
                          f"Pre:{r['prefill_ms']:>6.1f}ms  Dec:{r['decode_ms']:>6.1f}ms  "
                          f"PPL:{r['perplexity']:.2f}")

        return results

    def get_lora_params(self) -> int:
        """Count LoRA parameters."""
        return sum(p.numel() for n, p in self.base.named_parameters() if 'lora' in n)

    def get_total_params(self) -> int:
        """Count total parameters."""
        return sum(p.numel() for p in self.base.parameters())

    def info(self) -> dict:
        """Model info."""
        return {
            "model": self.model_name,
            "lora_rank": self.lora_rank,
            "total_params": self.get_total_params(),
            "lora_params": self.get_lora_params(),
            "device": self.device,
            "n_layers": self._n_layers,
        }

    def save_lora(self, path: str):
        """Save LoRA weights only."""
        state = {n: p for n, p in self.base.named_parameters() if 'lora' in n}
        torch.save(state, path)

    def load_lora(self, path: str):
        """Load LoRA weights."""
        state = torch.load(path, map_location=self.device, weights_only=True)
        for n, p in self.base.named_parameters():
            if n in state and p.shape == state[n].shape:
                p.data.copy_(state[n])
        print(f"[KvForge] LoRA weights loaded from {path}")


if __name__ == "__main__":
    # Quick test
    model = KvForgeModel("gpt2", lora_rank=8)
    info = model.info()
    print(f"Model: {info['model']} ({info['total_params']/1e6:.1f}M)")
    print(f"LoRA: {info['lora_params']/1e3:.1f}K")
    results = model.benchmark(
        ["The transformer architecture revolutionized NLP."],
        modes=['full_lora', 'base_encode_lora_decode'],
        compress_bits_list=[16, 8, 4],
    )
    print(f"\nDone! {len(results)} tests completed.")
