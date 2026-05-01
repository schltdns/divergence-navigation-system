# 02 – Thresholds & Falsification

## Δdiv / drift Interpretation (canonical)

| Range | Label | Recommended Action |
|-------|-------|-------------------|
| < 0.15 | Consensus | No further validation required |
| 0.15–0.35 | Minor Deviation | Review context, document findings |
| 0.35–0.50 | Significant Divergence | Trigger External Validation (P6) |
| 0.50–0.70 | Source Asymmetry | Activate Power Layer Check (P6b) |
| > 0.70 | Epistemic Blind Spot | F1-Trigger: DeepSeek Intervention + Operator Escalation |

## Additional Flags (DNS P4.2)

**Contradiction Flag**
- Trigger: ≥2 models make explicitly opposite claims on the same question

**Source Asymmetry Flag**
- Trigger: One model is isolated from all others (min Δdiv > 0.5) AND reference analysis shows a single-source base
- In this run: NotebookLM = frAIme/DNS only, others = KMK, UNESCO, OECD, school barometer, AKTIV, PAIR

**Falsification Check**
- Hypothesis H1 is considered falsified if the Source Asymmetry Flag does not trigger
