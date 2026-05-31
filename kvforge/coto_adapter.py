"""
CoTo (Come Together) — ICML 2025
https://github.com/zwebzone/coto

Progressive training stabilizer for KvForge.

Her katman 1 grup (6 adapter: q,k,v,o,fc_in,fc_out).
p(t): 0.2 -> 1.0, stage1_ratio=0.75.

Kullanim:
    model = KVForgeModelV2()
    model.add_lora(rank=8)  # LoRA adapter'lari ekle
    
    coto = CoToController(model, total_steps=1000)
    for step in range(steps):
        p_t = coto.step(step)  # Bernoulli mask uygula
        print(coto.status_str())
    
    coto.disable_all()  # inference
"""

import torch
import torch.nn as nn
import math


def generate_coto_mask(n_groups: int, rate: float) -> torch.Tensor:
    """
    En az 1 grup her zaman aktif.
    True = aktif (adapter calisir), False = skip.
    """
    while True:
        mask = torch.rand(n_groups) <= rate
        if mask.any():
            return mask


class CoToScheduler:
    """
    p(t) = p0 + (1-p0) * min(t / threshold, 1)   (t < threshold)
    p(t) = 1.0                                     (t >= threshold)
    """
    def __init__(self, total_steps: int, n_groups: int = 12,
                 initial_p: float = 0.2, stage1_ratio: float = 0.75):
        self.total_steps = total_steps
        self.n_groups = n_groups
        self.initial_p = initial_p
        self.stage1_ratio = stage1_ratio
        self.threshold = int(total_steps * stage1_ratio)

    def get_rate(self, step: int) -> float:
        if step >= self.threshold:
            return 1.0
        progress = step / max(self.threshold, 1)
        return min(self.initial_p + (1.0 - self.initial_p) * progress, 1.0)

    def get_mask(self, step: int) -> torch.Tensor:
        rate = self.get_rate(step)
        if rate >= 1.0:
            return torch.ones(self.n_groups, dtype=torch.bool)
        return generate_coto_mask(self.n_groups, rate)

    def get_prob(self, step: int) -> float:
        return self.get_rate(step)


class CoToAdapterWrapper(nn.Module):
    """
    Her bir adapter (LoRA) icin wrapper.
    
    cotodrop=True  -> adapter bypass (sadece base output)
    cotodrop=False -> base + lora output (tam aktif)
    
    self.training=False (model.eval()) -> her zaman tam aktif
    """
    def __init__(self, base_layer: nn.Module, lora_A: nn.Module, lora_B: nn.Module, scaling: float):
        super().__init__()
        self.base_layer = base_layer
        self.lora_A = lora_A
        self.lora_B = lora_B
        self.scaling = scaling
        self.cotodrop = False  # False=aktif, True=skip

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        base_out = self.base_layer(x)
        if self.training and self.cotodrop:
            return base_out  # adapter skip
        lora_out = self.lora_B(self.lora_A(x)) * self.scaling
        return base_out + lora_out


class CoToController:
    """
    Ana controller. Training loop'u icinde kullanilir.
    
    Ornek:
        model = KVForgeModelV2()
        model.add_lora(rank=8)  # CoToAdapterWrapper'lari olustur
        
        coto = CoToController(model, total_steps=1000)
        for step in range(steps):
            p_t = coto.step(step)
            # ... forward, backward ...
        
        coto.disable_all()  # inference
    """
    def __init__(self, model, total_steps: int, n_groups: int = None,
                 initial_p: float = 0.2, stage1_ratio: float = 0.75):
        """
        Args:
            model: KVForgeModelV2 (add_lora() cagrilmis olmali)
            total_steps: Toplam egitim adimi
            n_groups: Grup sayisi. None = model.get_layer_count()
            initial_p: Baslangic olasiligi (default: 0.2)
            stage1_ratio: Stokastik faz orani (default: 0.75)
        """
        self.model = model
        
        # Adapter'lari model.coto_adapters'tan al
        self.adapters = model.coto_adapters
        
        if n_groups is None:
            n_groups = model.get_layer_count()
        
        if len(self.adapters) == 0:
            print("  [CoTo] UYARI: Hiç adapter bulunamadi! model.add_lora() cagirildi mi?")
        
        self.n_groups = n_groups
        self.adapters_per_group = len(self.adapters) // max(n_groups, 1)
        
        self.scheduler = CoToScheduler(total_steps, n_groups, initial_p, stage1_ratio)
        self.current_mask = None
        
        print(f"  [CoTo] {n_groups} grup x {self.adapters_per_group} adapter = {len(self.adapters)} total")
        print(f"  [CoTo] p0={initial_p}, ratio={stage1_ratio}, threshold={self.scheduler.threshold}")
    
    def step(self, global_step: int) -> float:
        """
        Her training adiminda cagrilir.
        - Bernoulli maskesi hesaplar
        - Her grubun adapter'larina cotodrop flag'i atar
        - p(t) olasiligini dondurur
        """
        self.current_mask = self.scheduler.get_mask(global_step)
        
        # Mask'i adapter'lara uygula
        for i, adapter in enumerate(self.adapters):
            group_idx = i // self.adapters_per_group
            if group_idx < len(self.current_mask):
                active = self.current_mask[group_idx].item()
                adapter.cotodrop = not active  # True=aktif => cotodrop=False
        
        return self.scheduler.get_prob(global_step)
    
    def get_active_count(self) -> int:
        """Aktif grup sayisi."""
        if self.current_mask is None:
            return 0
        return self.current_mask.sum().item()
    
    def get_active_adapter_count(self) -> int:
        """Aktif adapter sayisi."""
        return self.get_active_count() * self.adapters_per_group
    
    def get_prob(self, step: int) -> float:
        return self.scheduler.get_prob(step)
    
    def disable_all(self):
        """
        Inference: tum adapter'lari tam aktif yap.
        model.eval() ile birlikte cagrilmali.
        """
        for adapter in self.adapters:
            adapter.cotodrop = False
    
    def status_str(self) -> str:
        """Ornek: p=0.35 aktif=4/12 (24 adapter)"""
        if self.current_mask is not None:
            active = self.get_active_count()
            return f"p={self.get_prob(0):.3f} aktif={active}/{self.n_groups} ({active * self.adapters_per_group} adapter)"
        return "CoTo: baslatilmadi"
