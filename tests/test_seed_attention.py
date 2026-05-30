"""
KVForge Test Suite — SeedAttention birim testleri
==================================================
Kullanım: pytest tests/test_seed_attention.py
"""

import torch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from kvforge.nano_model import NanoKVForge, NanoSeedAttention, D_MODEL, N_HEADS, SEED_DIM, SEQ_LEN, VOCAB_SIZE


def test_model_creation():
    """Model oluşturma testi."""
    model = NanoKVForge()
    assert model is not None
    total, trainable = model.count_parameters()
    assert total > 0
    assert trainable == total  # hepsi trainable
    print(f"✓ Model oluşturma: {total:,} parametre")


def test_forward_pass():
    """Forward pass testi."""
    model = NanoKVForge()
    model.eval()
    
    x = torch.randint(0, VOCAB_SIZE, (2, SEQ_LEN))
    with torch.no_grad():
        loss, logits, recon = model(x, labels=x, return_seed=True)
    
    assert logits.shape == (2, SEQ_LEN, VOCAB_SIZE), f"Beklenen: (2, {SEQ_LEN}, {VOCAB_SIZE}), Gelen: {logits.shape}"
    assert loss is not None
    assert loss.item() > 0
    print(f"✓ Forward pass: loss={loss.item():.4f}, logits={logits.shape}")


def test_reconstruction_loss():
    """Reconstruction loss testi."""
    model = NanoKVForge()
    model.eval()
    
    x = torch.randint(0, VOCAB_SIZE, (1, SEQ_LEN))
    
    # return_seed=True ile
    _, _, recon_true = model(x, labels=x, return_seed=True)
    assert recon_true is not None
    assert recon_true > 0
    
    # return_seed=False ile
    _, _, recon_false = model(x, labels=x, return_seed=False)
    assert recon_false is None
    
    print(f"✓ Reconstruction loss: {recon_true:.6f}")


def test_generation():
    """Generation testi."""
    model = NanoKVForge()
    model.eval()
    
    output = model.generate("ROMEO: ", max_new_tokens=20)
    assert isinstance(output, str)
    assert len(output) > 0
    print(f"✓ Generation: {output[:50]}...")


def test_seed_compression_ratio():
    """Seed compression oranı testi."""
    attn = NanoSeedAttention()
    
    # Forward ile seed boyutunu kontrol et
    x = torch.randn(1, SEQ_LEN, D_MODEL)
    with torch.no_grad():
        out, seed, _ = attn(x, return_seed=True)
    
    expected_seed_dim = SEED_DIM  # 16
    assert seed.shape[-1] == expected_seed_dim, f"Seed dim: {seed.shape[-1]}, beklenen: {expected_seed_dim}"
    
    compression_ratio = 2 * D_MODEL / SEED_DIM  # 128/16 = 8
    print(f"✓ Seed compression: {2*D_MODEL} → {SEED_DIM} = {compression_ratio:.0f}×")


def test_deterministic():
    """Deterministik çalışma testi."""
    torch.manual_seed(42)
    model = NanoKVForge()
    model.eval()
    
    x = torch.randint(0, VOCAB_SIZE, (1, 10))
    
    with torch.no_grad():
        _, logits1, _ = model(x, return_seed=False)
        _, logits2, _ = model(x, return_seed=False)
    
    assert torch.allclose(logits1, logits2), "Deterministik değil!"
    print(f"✓ Deterministik: OK")


def test_gradient_flow():
    """Gradyan akışı testi."""
    model = NanoKVForge()
    model.train()
    
    x = torch.randint(0, VOCAB_SIZE, (2, SEQ_LEN))
    loss, _, _ = model(x, labels=x, return_seed=True)
    loss.backward()
    
    # Tüm parametreler gradyan aldı mı?
    has_grad = all(p.grad is not None and p.grad.abs().sum() > 0 
                   for p in model.parameters() if p.requires_grad)
    assert has_grad, "Bazı parametreler gradyan almamış!"
    print(f"✓ Gradyan akışı: OK")


def test_edge_cases():
    """Edge case testleri."""
    model = NanoKVForge()
    model.eval()
    
    # Boş prompt
    output = model.generate("", max_new_tokens=5)
    assert isinstance(output, str)
    
    # Tek karakter
    output = model.generate("a", max_new_tokens=5)
    assert len(output) > 0
    
    # Uzun prompt
    long_prompt = "R" * (SEQ_LEN // 2)  # SEQ_LEN'in yarısı kadar
    output = model.generate(long_prompt, max_new_tokens=10)
    assert len(output) > len(long_prompt)
    
    print(f"✓ Edge cases: OK")


if __name__ == "__main__":
    test_model_creation()
    test_forward_pass()
    test_reconstruction_loss()
    test_generation()
    test_seed_compression_ratio()
    test_deterministic()
    test_gradient_flow()
    test_edge_cases()
    print("\n✅ Tüm testler geçti!")
