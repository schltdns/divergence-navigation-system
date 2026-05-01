frAIme Protocol (P1–P8)
A reproducible, auditable workflow for argumentation drift

frAIme structures how heterogeneous models (S1–Ω) and the human operator collaborate to reveal epistemic uncertainty. It is domain-agnostic.

frAIme does not seek consensus — it maps where and why models diverge.

🧭 Overview
P1 — Hypothesize

P2 — Thresholds

P3 — Collect

P4 — Map Divergence

P5 — Synthesis

P5b — Operator Decision

P6 — Validation

P6b — Power Layer

P7 — Reflection

P8 — Versioning

P1 — Hypothesize
Define a falsifiable question.

scope, assumptions, domain

Output: 01_hypothesis.md

P2 — Thresholds
Define falsification criteria.

Δdiv thresholds, contradiction flags

Output: 02_thresholds.md

P3 — Collect
Run identical prompt across S1–Ω.

no cross-contamination, single-turn

Output: 03_outputs/S1.md … 03_outputs/Omega.md

optional: 03_outputs/graph.png (if graph divergence needed)

P4 — Map Divergence
frAIme calculates divergence:

4.1 Semantic Divergence (Δdiv) / drift
Δdiv = 1 − (Jaccard_sem + Cosine) / 2
*(i.e., the mean of Jaccard and cosine distances: 0.5·(1−Jaccard_sem) + 0.5·(1−Cosine), mathematically identical)*

where:

Jaccard_sem = |concepts(A) ∩ concepts(B)| / |concepts(A) ∪ concepts(B)|

Cosine = embedding similarity

Interpretation:

Δdiv < 0.3 → low drift

0.3–0.6 → medium drift

0.7 → high drift

case_study_frAIme: Δdiv 0.584–0.759

Output: 04_divergence_map.md, heatmap.png

P5 — Synthesis
Integrate with Four Questions.

Output: 05_synthesis.md

P5b — Operator Decision
Human weighs and justifies.

Output: 05b_operator_decision.md

P6 — Validation
Compare with literature.

Output: 06_validation.md

P6b — Power Layer
Who benefits / bears risk.

Output: 06b_power_layer.md

P7 — Reflection
Document bias.

Output: 07_reflection.md

P8 — Versioning
Archive with version tag.

Output: 08_manifest_en.json, 08_manifest_de.json
