# 02 — Threshold Definition

**Case Study:** DNS Full Circle  
**DNS v2.1**

---

## Δdiv Scale

DNS measures divergence as:


$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

Range: 0.00 (identical) to 1.00 (maximally divergent)

---

## Interpretation Thresholds

| Range | Label | Meaning |
|-------|-------|---------|
| 0.00 – 0.35 | **Convergent** | Models agree on facts and framing |
| 0.36 – 0.55 | **Low divergence** | Minor wording differences |
| 0.56 – 0.77 | **Structured** | Different emphasis, same domain |
| **0.78 – 0.90** | **Contested** | **Incompatible frames, synthesis required** |
| 0.91 – 1.00 | **Fragmented** | No shared ground, likely error |

---

## Threshold for This Study

**Contested threshold set at 0.78**

Rationale for DNS Full Circle:
- Self-application of a methodological framework is expected to trigger perspective shifts
- Previous DNS studies (Cognitive Safety: 0.67, Labour 2030: 0.71) remained in "structured" range
- A method describing itself should exceed prior cases — otherwise it lacks reflexive depth

**Hypothesis H1 predicts:** Δdiv > 0.78

---

## Decision Rules

- If average Δdiv ≥ 0.78 → proceed to weighted human synthesis (Phase 5)
- If average Δdiv < 0.56 → flag as trivial convergence, revise prompts
- If any pair > 0.90 → manual review for prompt failure or hallucination
