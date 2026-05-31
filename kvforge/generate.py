#!/usr/bin/env python3
"""
KVForge Generation Script
=========================
Eğitilmiş model ile metin üretimi.

Kullanım:
    python -m kvforge.generate
    python -m kvforge.generate --prompt "ROMEO: " --length 200 --temperature 0.8
"""

import torch
import torch.nn.functional as F
import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description="KVForge Generation")
    parser.add_argument("--checkpoint", type=str, 
                        default=os.path.join(os.path.dirname(__file__), '..', 'checkpoints', 'nano_best.pt'),
                        help="Model checkpoint yolu")
    parser.add_argument("--prompt", type=str, default="ROMEO: ",
                        help="Generation prompt")
    parser.add_argument("--length", type=int, default=150,
                        help="Üretilecek token sayısı")
    parser.add_argument("--temperature", type=float, default=0.8,
                        help="Sampling sıcaklığı")
    parser.add_argument("--top-k", type=int, default=10,
                        help="Top-k sampling")
    args = parser.parse_args()
    
    # Model yükle
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from kvforge.nano_model import NanoKVForge
    
    print(f"Model yükleniyor: {args.checkpoint}")
    model = NanoKVForge()
    
    if os.path.exists(args.checkpoint):
        model.load_state_dict(torch.load(args.checkpoint, weights_only=True, map_location='cpu'))
        print("  ✓ Checkpoint yüklendi")
    else:
        print(f"  ⚠ Checkpoint bulunamadı ({args.checkpoint}), rastgele ağırlıklar kullanılıyor")
    
    model.eval()
    
    total_params = sum(p.numel() for p in model.parameters())
    print(f"  Model: {total_params:,} parametre ({total_params/1e3:.1f}K)")
    
    # Generation
    print(f"\nPrompt: '{args.prompt}'")
    print(f"Üretiliyor... ({args.length} token, T={args.temperature}, top_k={args.top_k})")
    print("-" * 60)
    
    output = model.generate(
        args.prompt,
        max_new_tokens=args.length,
        temperature=args.temperature,
        top_k=args.top_k
    )
    
    print(output)
    print("-" * 60)


if __name__ == "__main__":
    main()
