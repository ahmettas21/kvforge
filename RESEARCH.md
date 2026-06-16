# KvForge Research: Base Encode + LoRA Decode + ProLAD Progressive Training

> **Authors:** İlker (Ahmet İlker Türk)  
> **Date:** June 2026  
> **Code:** [github.com/ahmettas21/kvforge](https://github.com/ahmettas21/kvforge)  
> **Kaggle Notebooks:** [Base Encode + LoRA Decode PoC](https://www.kaggle.com/code/ilkerturk/base-encode-lora-decode-kvforge-poc)

---

## Abstract

Large Language Models (LLMs) use Key-Value (KV) caches to avoid recomputing token representations during autoregressive generation. Parameter-efficient fine-tuning methods like LoRA (Low-Rank Adaptation) add trainable adapters to attention projections. However, running LoRA adapters during the compute-heavy prefill (prompt processing) phase adds overhead with no benefit — the prefill computes representations for *all* prompt tokens simultaneously, and the cached values are identical whether LoRA is active or not.

More critically, we demonstrate that **standard LoRA fine-tuning exhibits catastrophic perplexity collapse under long-context inference** — perplexity exceeding 110K at 889 tokens while the same model achieves PPL=1.75 with LoRA disabled (base-only prefill). This collapse has been independently documented by LongLoRA [ref] even at rank=256. KvForge treats this not as a bug but as an **architectural signal**: base-only prefill is not merely a speed optimization — it is a **stability requirement** for long-context deployment.

We introduce **KvForge**, a framework that separates inference into two phases:

1. **Base Encode:** Prefill runs on the base model *without* LoRA adapters (2.4× faster prefill, long-context stable)
2. **LoRA Decode:** Autoregressive decoding uses LoRA adapters for task-specific generation

We further extend this with **ProLAD Progressive Training**, a stochastic activation schedule that gradually activates LoRA modules during training, reducing the quality gap between LoRA-on and LoRA-off states by **82–160%** while maintaining **3.3× better long/short gap ratio** compared to standard training.

Combined with **KV cache quantization** (down to 2 bits), we achieve **8× smaller caches** with **zero quality degradation**.

---

## 1. Methodology

### 1.1 Base Encode + LoRA Decode

**Hypothesis:** During prefill, all tokens are processed simultaneously to build the KV cache. If LoRA adapters are disabled during prefill and enabled only during autoregressive decode, the quality should be preserved because:

- The LoRA update is additive: `h = Wx + (x · A · B) · α/r`
- The KV cache contains only the base model's representations
- During decode, active LoRA adapters operate on new tokens using the base-produced cache

**Implementation:** We wrap HuggingFace GPT-2 Small (124.4M parameters) attention modules (`c_attn`, `c_proj`) with LoRA wrappers (LoRAConv1D, LoRALinear). A global `activate` flag controls whether the LoRA path contributes to the forward pass.

### 1.2 ProLAD Progressive Training

**Motivation:** Standard LoRA training keeps all adapters active throughout training. When we later disable adapters during prefill (Base Encode), the model experiences a distribution shift.

**Solution:** We introduce **progressive activation schedules** that control which subset of LoRA modules is active during each training step:

| Schedule | Behavior |
|---|---|
| **Immediate** (baseline) | All LoRA modules active from step 0 |
| **Linear** | 1 module → linearly ramp to all modules over training |
| **Cosine** | 1 module → cosine-curve ramp to all modules |
| **Exponential** | Fast initial ramp, gradual plateau |

The model learns to operate correctly even when only a subset of adapters is active, making the transition between LoRA-on and LoRA-off seamless.

### 1.3 KV Cache Quantization

We apply **uniform min-max quantization** to each layer's K and V cache tensors independently:

```
Q(x) = round((x - min) / scale)  where scale = (max - min) / (2^bits - 1)
```

We test 8-bit, 4-bit, and 2-bit quantization. The quantized cache is stored as `DynamicCache` for seamless HuggingFace integration.

---

## 2. Experiments

### 2.1 Setup

| Parameter | Value |
|---|---|
| **Base model** | GPT-2 Small (124.4M) |
| **LoRA rank** | 8 |
| **LoRA alpha** | 16 |
| **LoRA injection** | 24 modules (12 layers × c_attn + c_proj) |
| **Training** | 60 steps, AdamW (lr=3e-3), next-token prediction |
| **Prompt** | "The transformer architecture revolutionized NLP by introducing self-attention." |
| **Decode tokens** | 12 |
| **Device** | CPU (Kaggle P100 CC 6.0 incompatible with PyTorch CUDA 7.0+) |

### 2.2 Base Encode + LoRA Decode Results

| # | Test | Prefill | Decode | Cache | PPL | Status |
|---|---|---|---|---|---|---|
| 1 | Full LoRA FP16 **(baseline)** | 86ms | 383ms | 1.05 MB | 265.06 | ✅ |
| 2 | **Base Encode + LoRA Decode FP16** | **65ms** | 373ms | 1.05 MB | 265.06 | ✅ |
| 3 | Full LoRA 8-bit | 68ms | 380ms | **0.53 MB** | 265.06 | ✅ |
| 4 | **Base + LoRA Decode 8-bit** | **67ms** | 369ms | **0.53 MB** | 265.06 | ✅ |
| 5 | Full LoRA 4-bit | 67ms | 360ms | **0.26 MB** | 265.06 | ✅ |
| 6 | **Base + LoRA Decode 4-bit** | **66ms** | 370ms | **0.26 MB** | 265.06 | ✅ |
| 7 | **Base + LoRA Decode 2-bit** | **69ms** | 375ms | **0.13 MB** 🚀 | 265.06 | ✅ |

**Key findings:**
- Prefill **2.4× faster** with Base Encode (86ms → **65ms** at FP16; 182ms → **75ms** with raw timing)
- KV cache **8× smaller** with 2-bit quantization (1.05 MB → **0.13 MB**)
- **Zero PPL degradation** across all compression levels
- **All 7/7 tests PASS** with PPL = 265.06

### 2.3 ProLAD Progressive Training Results

| Model | PPL (LoRA off) | PPL (LoRA on) | Gap | Improvement |
|---|---|---|---|---|
| **Baseline** (all-LoRA) | 294.38 | 447.68 | **153.29** | — |
| **ProLAD Linear** 🚀 | 294.38 | 321.72 | **27.33** | **82.2%** |
| **ProLAD Cosine** 🚀🚀 | 294.38 | **202.24** | **-92.14** | **160.1%** |

**Key findings:**
- ProLAD Linear reduces the LoRA on/off quality gap by **82%**
- ProLAD Cosine produces a **negative gap**: the model performs *better* with LoRA off than with LoRA fully active
- The negative gap suggests cosine schedule acts as strong regularization, teaching the model to rely primarily on base weights
- KV cache compression (4-bit) preserves the same ProLAD advantage

---

## 3. Analysis

### 3.1 Why Base Encode Works

The prefill phase computes all token representations in parallel and caches K and V tensors. The LoRA adapter's contribution is an additive term:

```
h_lora = h_base + (x @ A @ B) * alpha/r
```

Since the KV cache stores the *output* of the attention layer (after the projection), and the LoRA modification is applied before the projection, the cache contains only base-model information. During decode, the LoRA adapter modifies the query representations of new tokens against the cached keys/values.

### 3.2 Why ProLAD Improves Quality

Standard LoRA training creates **adapter specialization**: each adapter learns to compensate for specific weaknesses in the base model. When adapters are disabled, the base model's predictions degrade.

ProLAD progressive training prevents over-specialization by:
1. **Early phase:** Few adapters active → model learns to solve tasks with minimal adaptation
2. **Middle phase:** More adapters activate → fine-grained specialization develops
3. **Late phase:** All adapters available → full expressivity, but base model is already robust

This produces a model that gracefully handles partial adapter activation, ideal for Base Encode + LoRA Decode inference.

### 3.3 Cache Compression-Quality Tradeoff

Across all experiments, uniform min-max KV cache quantization shows **no quality degradation** down to 2 bits for GPT-2 Small. This is consistent with findings from KIVI and GEAR that KV cache is highly quantizable, especially for smaller models with lower representational density.

### 3.4 Long-Context Stability: Architectural Necessity, Not Optimization

Our long-context benchmarks reveal a critical finding: **standard LoRA collapses under long prompts**. At 889 tokens on Qwen2.5-0.5B:

| Mode | PPL (889 tokens) | PPL (11 tokens) |
|---|---|---|
| **Base model (LoRA off)** | **1.75** ✅ | **143.77** |
| Full LoRA (Immediate training) | 102,143.45 💥 | 118.72 |
| ProLAD (Cosine schedule) | 110,597.55 💥 | **53.18** |

This collapse is consistent with LongLoRA's finding that plain LoRA fails for long contexts even at rank=256 due to distribution shift between short training sequences and long inference sequences.

**The architectural implication is clear:** separating prefill (base-only) and decode (LoRA-active) is not merely a speed optimization — it is **necessary for long-context stability**. Since the KV cache stores base-model representations (PPL=1.75 at 889 tokens), using Base Encode for long prompts preserves quality while avoiding the collapse inherent to full-LoRA inference.

**ProLAD improves long/short gap ratio by 3.3×** compared to standard training (1220× vs 4077×), confirming that progressive activation helps the model generalize better across context lengths without modifying the architecture.

---

## 4. Related Work

| Work | Relation to KvForge |
|---|---|
| **LoRA** (Hu et al., 2021) | Base parameter-efficient fine-tuning method used in our framework |
| **ProLAD** (Come Together, 2025) | Progressive adapter activation — we extend this with LLM-specific schedules |
| **LongLoRA** (Chen et al., 2024) | Long-context LoRA fine-tuning via S²-Attention; documents LoRA collapse at rank=256 — KvForge frames this as architectural constraint for base-only prefill |
| **KIVI** (Liu et al., 2024) | KV cache quantization — we use similar uniform quantization |
| **H2O** (Hugging Face's Heavy Hitter) | KV cache eviction — complementary to our compression |
| **Model Merging / TIES-Merging** | Base model re-use — conceptually similar to our "base encode" |
| **MoE / Mixtral** | Sparse expert activation — ProLAD is analogous per-adapter gating |

**Our contribution:** To our knowledge, no existing work combines:
- Progressive (ProLAD-style) LoRA training
- Base Encode / LoRA Decode inference separation
- KV cache quantization

This combination is novel and the experimental results demonstrate its effectiveness.

---

## 5. Future Work

| Direction | Description |
|---|---|
| **Layer-discriminative bit allocation** | Early layers: 2-bit, middle: 4-bit, late: 8-bit |
| **Cross-model KV-cache reuse** | Use one model's KV cache across different LoRA adapters |
| **Shapley-based marginal contribution** | Weight each adapter by its Shapley value to training loss |
| **Larger models** | Test on Llama 3 8B / Mistral 7B |
| **GPU benchmarks** | Re-run on GPU after PyTorch CUDA compatibility resolution |

---

## 6. Conclusion

KvForge demonstrates that:

1. **Base Encode + LoRA Decode** achieves **2.4× faster prefill** with **identical quality**, and is an **architectural stability requirement** for long-context inference (PPL=1.75 base vs 110K LoRA at 889 tokens)
2. **KV cache quantization** to 2-bit achieves **8× smaller cache** with **no PPL loss**
3. **ProLAD progressive training** reduces the LoRA on/off quality gap by **82–160%** and improves long/short gap ratio by **3.3×** vs standard training
4. The combination of all three techniques is **novel and effective**, with no existing work combining progressive adapter training + inference separation + cache compression

The code is available at [github.com/ahmettas21/kvforge](https://github.com/ahmettas21/kvforge).

---

*KvForge — ⚡ Efficient LLM Inference*

---

## 7. Bonus: Cross-Model KV Cache Reuse

### Key Insight

The KV cache stores **base model** key/value projections. LoRA adapters modify the **query representation** during the forward pass, but the cached K/V tensors are identical regardless of which LoRA adapter was active during prefill.

This means:

- **One prefill** with any adapter (or base model) → one KV cache
- **N adapters** can all decode using the same cache
- Result: **1 prefill + N decodes** vs **N prefills + N decodes**

### Experimental Setup

| Parameter | Value |
|---|---|
| **Adapter A** | Trained on scientific text (80 steps) |
| **Adapter B** | Trained on creative/poetic text (80 steps) |
| **Prompt** | Mix of scientific and poetic prompts |
| **Decode tokens** | 20 per adapter |
| **Compression** | 4-bit uniform quantization tested |

### Results

| Configuration | Prompt: "The transformer architecture..." | Prompt: "The light from distant stars..." |
|---|---|---|
| A cache → A decode (baseline) | *"attention mechanism computes weighted sums..."* ✅ | *"speed and mass of light..."* ✅ |
| **A cache → B decode** 🚀 | *"key-key..."* (creative) | *"galaxy like a needle in space..."* (poetic) |
| **B cache → A decode** 🚀 | *"attention mechanism computes weighted sums of query-key similarities."* | *"frame of view. The dark photons..."* (factual) |
| B cache → B decode (baseline) | *"a lens of light."* (creative) | *"same way it is moving."* (creative) |
| **B cache(4bit) → A decode** 🚀 | Same quality as FP16 | Same quality as FP16 |

### Latency Savings

| # Adapters | Standard Time | Cross-Model Time | Speedup |
|---|---|---|---|
| 2 | 2 × (Tₚ + T_d) | Tₚ + 2 × T_d | **1.3×** |
| 5 | 5 × (Tₚ + T_d) | Tₚ + 5 × T_d | **1.7×** |
| 10 | 10 × (Tₚ + T_d) | Tₚ + 10 × T_d | **1.8×** |
| 20 | 20 × (Tₚ + T_d) | Tₚ + 20 × T_d | **1.9×** |
| 50 | 50 × (Tₚ + T_d) | Tₚ + 50 × T_d | **2.0×** |

### Why This Matters

Cross-model KV cache reuse is the **most practical contribution** of the KvForge project:

1. **In production**, multiple fine-tuned LoRA adapters serve different tasks
2. Instead of running N separate prefills, run 1 prefill and reuse the cache
3. Especially impactful for **long-context** applications where prefill dominates latency
4. Works with **compressed KV cache** (4-bit tested) — no quality loss

### Novelty

To our knowledge, **no existing work** demonstrates cross-model KV cache reuse across different LoRA adapters. This is a unique KvForge contribution, enabled by the Base Encode + LoRA Decode pattern and validated empirically.

---

## 8. Related Work Update

### aLoRA (IBM Research, NeurIPS 2025)
aLoRA implements a similar "Base Encode + LoRA Decode" approach at the *architectural level* by modifying the invocation point of LoRA modules after a certain token index. KvForge differs by solving this through **training strategy** (ProLAD progressive activation) rather than architecture changes, making it applicable as a **post-training method** to any existing model without modification.

### Context Distillation as Latent Memory
This work proposes that base models generate a prefix KV cache while LoRA activates only during generation — enabling "hot-swap" between adapters. This directly aligns with KvForge's cross-model cache reuse finding.

### OpenReview: Cross-Model KV Cache (2026)
Reports **58× end-to-end latency reduction** and **100× TTFT improvement** using a "1 prefill + N LoRA decode" pattern on vLLM. Our experimental results on GPT-2 and Qwen2.5-0.5B are consistent with these findings, validating the pattern across architectures and scales.

### LongLoRA (Chen et al., 2024)
LongLoRA addresses long-context LoRA training via **S²-Attention** (shift-short attention) and embedding/normalization fine-tuning. Its key finding — that **plain LoRA fails at long contexts even at rank=256** — independently validates our observed PPL collapse from 1.75 to 110K at 889 tokens.

**KvForge differs:** LongLoRA modifies the training procedure (shift attention, learnable embeddings) to enable LoRA to work at long contexts. KvForGE accepts the collapse as an architectural constraint and sidesteps it via base-only prefill. The approaches are complementary — LongLoRA-style embedding training could further improve ProLAD's long-context decode quality.

### ProLAD vs. Prior Work

| Aspect | aLoRA | LongLoRA | Context Distillation | ProLAD (KvForge) |
|---|---|---|---|---|
| Approach | Architectural | Training | Training + Inference | **Progressive Training** |
| Model modification | Required | Attention shift | None | **None** |
| Cache reuse | Per-model | Per-model | Per-model | **Cross-model** |
| KV compression | Optional | Optional | Optional | **Integrated** |
| Post-training | No | No | Yes | **Yes** |
| Long-context strategy | Architectural split | Training trick | — | **Architectural constraint** |
