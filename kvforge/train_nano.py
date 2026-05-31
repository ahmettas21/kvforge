#!/usr/bin/env python3
"""
KVForge Nano Model Eğitimi
===========================
Byte-level Seed Attention eğitimi. CPU'da ~10-15 dk.

Kullanım:
    python -m kvforge.train_nano
"""

import sys
import os

# Repo kökünü PATH'e ekle
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kvforge.nano_model import main

if __name__ == "__main__":
    main()
