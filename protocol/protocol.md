# DNS Protocol (P1–P8)

**A reproducible, auditable workflow for divergence-based epistemic analysis**

DNS structures how heterogeneous models (S1–Ω) and the human operator collaborate to reveal epistemic uncertainty. It is domain-agnostic.

DNS does not seek consensus — it maps **where and why models diverge**.

---

## 🧭 Overview

1. **P1 — Hypothesize**
2. **P2 — Thresholds**
3. **P3 — Triangulate**
4. **P4 — Map Divergence**
5. **P5 — Weighted Synthesis**
6. **P6 — External Validation**
7. **P6b — Power Layer Check**
8. **P7 — Operator Reflection**
9. **P8 — Versioning**

Each phase produces auditable artifacts.

---

## P1 — Hypothesize
Define a falsifiable question.
- scope, assumptions, domain (Formal / Applied / Complex)
- expected Δdiv

**Output:** `01_hypothesis.md`

## P2 — Thresholds
Define falsification criteria.
- Δdiv thresholds, contradiction flags, normative drift

**Output:** `02_thresholds.md`

## P3 — Triangulate
Run identical prompt across S1–Ω.
- no cross-contamination, single-turn

**Output:** `03_outputs/S1.md` … `03_outputs/Omega.md`

## P4 — Map Divergence
Four layers:
1. Substantive
2. Methodological
3. Normative
4. Architectural

**Output:** `04_divergence_map.md`

## P5 — Weighted Synthesis
Operator integrates, weighs, justifies.
**Output:** `05_synthesis.md`

## P6 — External Validation
Compare with data, literature, experts.
**Output:** `06_validation.md`

## P6b — Power Layer Check
Who controls, benefits, bears risk, is excluded.
**Output:** `06b_power_layer.md`

## P7 — Operator Reflection
Document bias, load, uncertainty.
**Output:** `07_reflection.md`

## P8 — Versioning
Archive all artifacts with version tag (e.g., `dns_v2.1_run03`).
**Output:** `08_manifest.json` + IPFS CID
