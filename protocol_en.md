# frAIme Protocol (P1–P8)

**A reproducible, auditable workflow for argumentation drift**

frAIme structures how heterogeneous models (S1–Ω) and the human operator collaborate to reveal epistemic uncertainty. It is domain-agnostic.

frAIme does not seek consensus — it maps **where and why models diverge**.

## 🧭 Overview
1. **P1 — Hypothesize**
2. **P2 — Thresholds**
3. **P3 — Outputs**
4. **P4 — Map Divergence**
5. **P5 — Synthesis**
6. **P5b — Operator Decision**
7. **P6 — Validation**
8. **P6b — Power Layer**
9. **P7 — Reflection**
10. **P8 — Versioning**

---

## P1 — Hypothesize
Define a falsifiable question.
- scope, assumptions, domain

**Output:** `01_hypothesis.md`

## P2 — Thresholds
Define falsification criteria.
- Δdiv thresholds, contradiction flags

**Output:** `02_thresholds.md`

## P3 — Outputs
Run identical prompt across S1–Ω.
- no cross-contamination, single-turn

**Output:** `03_outputs/S1.md` … `03_outputs/Omega.md`
- optional: `03_outputs/graph.png`

## P4 — Map Divergence
frAIme calculates divergence:

### 4.1 Semantic Divergence (Δdiv) / drift
**Δdiv = 1 − (Jaccard_sem + Cosine) / 2**
*(i.e., 0.5·(1−Jaccard_sem) + 0.5·(1−Cosine))*

**drift = Δdiv**

where:
- Jaccard_sem = |concepts(A) ∩ concepts(B)| / |concepts(A) ∪ concepts(B)|
- Cosine = embedding similarity

## Δdiv / drift Interpretation (canonical)

| Range | Label | Recommended Action |
|-------|-------|-------------------|
| < 0.15 | Consensus | No further validation required |
| 0.15–0.35 | Minor Deviation | Review context, document findings |
| 0.35–0.50 | Significant Divergence | Trigger External Validation (P6) |
| 0.50–0.70 | Source Asymmetry | Activate Power Layer Check (P6b) |
| > 0.70 | Epistemic Blind Spot | F1-Trigger: DeepSeek Intervention + Operator Escalation |

*case_study_frAIme: Δdiv 0.584–0.759*

**Output:** `04_divergence_map.md`, `heatmap.png`

## P5 — Synthesis
Integrate with Four Questions.

**Output:** `05_synthesis.md`

## P5b — Operator Decision
Human weighs and justifies.

**Output:** `05b_operator_decision.md`

## P6 — Validation
Compare with literature.

**Output:** `06_validation.md`

## P6b — Power Layer
Who benefits / bears risk.

**Output:** `06b_power_layer.md`

## P7 — Reflection
Document bias.

**Output:** `07_reflection.md`

## P8 — Versioning
Archive with version tag.

**Output:** `08_manifest_en.json`, `08_manifest_de.json`
