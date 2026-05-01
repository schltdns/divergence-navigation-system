# frAIme Protocol (P1–P8) – case_study_frAIme

**A reproducible, auditable workflow for argumentation drift**

frAIme does not seek consensus — it maps where and why models diverge.

## P1 — Hypothesize
**File:** `01_hypothesis.md`

Question: How do six heterogeneous LLMs (NotebookLM, Qwen, DeepSeek, Gemini, Meta, Mistral) diverge on the same prompt about frAIme?

## P2 — Thresholds
**File:** `02_thresholds.md`

From hypothesis:
- < 0.15 → Consensus
- 0.15–0.35 → slight deviation
- > 0.35 → significant divergence
- > 0.50 → source asymmetry

## P3 — Outputs
**Folder:** `03_outputs/`

Six single-turn outputs, no cross-contamination:
- S1.md … S6.md (NotebookLM, Qwen, DeepSeek, Gemini, Meta, Mistral)
- `graph.png` → X/Y MDS plot of Δdiv (replaces dense network)

## P4 — Map Divergence
**Files:** `04_divergence_map.md`, `heatmap.png`

Δdiv = 1 − (Jaccard_sem + Cosine)/2 = 0.5·(1−Jaccard_sem)+0.5·(1−Cosine)
drift = Δdiv

**Results case_study_frAIme:**
| Pair | Δdiv |
|---|---|
| DeepSeek–Gemini | 0.759 |
| DeepSeek–Meta | 0.730 |
| NotebookLM–DeepSeek | 0.715 |
| ... | ... |
| Qwen–Mistral | 0.584 (lowest) |

All pairs >0.50 → 100% source asymmetry, no consensus.

## P5 — Synthesis
**File:** `05_synthesis.md`
Four Questions integration.

## P5b — Operator Decision
**File:** `05b_operator_decision.md`
Human justification of weighting.

## P6 — Validation
**File:** `06_validation.md`
Literature comparison.

## P6b — Power Layer
**File:** `06b_power_layer.md`
Who benefits / bears risk from divergence.

## P7 — Reflection
**File:** `07_reflection.md`
Bias documentation.

## P8 — Versioning
**Files:** `08_manifest_de.json`, `08_manifest_en.json`
