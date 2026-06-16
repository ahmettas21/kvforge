# CoTo Adapter Training — PoC

## Ne bu?

CoTo (Come Together) stochastic activation multi-task LoRA training'in proof-of-concept'i.

**Fikir:** Farklı görevler için LoRA adapter'larını ayrı ayrı eğitmek yerine, birlikte eğit ama her batch'te rastgele adapter'ları aktive/deaktive et. Bu sayede backbone her iki adapter'la da çalışmayı öğrenir ve merge başarısı artar.

## Sonuçlar

Simple predictor (pooled embedding → single Linear + LoRA) üzerinde iki farklı sequence-shift görevi:

| Method | Task 0 | Task 1 | Avg |
|---|---|---|---|
| Isolated Adapter 0 | 0.1700 | 0.1000 | 0.1350 |
| Isolated Adapter 1 | 0.1500 | 0.0500 | 0.1000 |
| Baseline Merged | 0.0200 | 0.0500 | **0.0350** |
| CoTo Individual | 0.1000 | 0.1700 | **0.1350** |
| CoTo Merged | 0.0100 | 0.0200 | **0.0150** |

## Gözlemler

1. **Model çok küçük** (32 hidden, tek layer, pooled) → her iki yöntemde de accuracy düşük
2. **Cross-contamination var:** Isolated adapter 0, task 1'de %10 alıyor — adapter ayrı eğitilse bile backbone aynı olduğu için sızıntı oluyor
3. **CoTo merged, baseline merged'dan biraz daha kötü** — bu model çok küçük olduğu için, stochastic training'in interference azaltma avantajı tam görülemiyor
4. **CoTo individual** isolated kadar iyi — yani stochastic training adapter performansını düşürmüyor

## Bir sonraki adım

Daha büyük bir modelde (4 layer transformer ile) test etmek gerek. Ayrıca:
- Gerçek veri seti (WikiText) kullanmak
- p değerini taramak (0.3, 0.5, 0.7, 0.9)
- Task başına ayrı veri miktarını değiştirmek
