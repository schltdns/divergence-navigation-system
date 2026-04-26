# Threshold: When does a claim become a "narrative risk"?

## DNS Divergence Thresholds (Snapshot)

| $\Delta_{div}$ Range | Classification | Action |
|----------------------|----------------|--------|
| < 0.2 | Convergence | Claim can be generalized |
| 0.2 – 0.5 | Structured divergence | Claim needs qualification |
| 0.5 – 0.7 | **High divergence** | **Narrative risk – do not generalize** |
| > 0.7 | Contested | Claim is likely a hallucination |

## Live-Tracking Thresholds (Process)

For continuous monitoring during a conversation:

| $\Delta_{total}$ Range | Status | System Action |
|------------------------|--------|---------------|
| < 0.3 | 🟢 Convergent | Silent monitoring |
| 0.3 – 0.5 | 🟡 Drift detected | Subtle marking – "check reasoning" |
| 0.5 – 0.7 | 🟠 High divergence | **Explicit warning – verify before use** |
| > 0.7 | 🔴 Contested | **Hard stop – DNS snapshot required** |

$$\Delta_{total} = 0.6 \cdot \Delta_{div\_semantic} + 0.4 \cdot \Delta_{div\_structural}$$

## Applied to Copilot

- **$\Delta_{div} = 0.657$** → High divergence → **NARRATIVE RISK**
- **Live status at Turn 1:** $\Delta_{total} = 0.68$ → 🟠 High divergence
- The claim "Western can, Chinese cannot" is mathematically unsupported.

## The MSB NRW Threshold

For a ministry (neutrality, evidence-based decision making), any $\Delta_{div} > 0.5$ requires:

- Explicit uncertainty marking
- Technical alternative explanations
- No geopolitical or cultural causation

**Copilot fails all three.**

For live use in classrooms, any $\Delta_{total} > 0.5$ triggers:

- Automatic uncertainty flag
- Suggestion to consult technical documentation
- Audit log entry

## Delta Div ($\Delta_{div}$)

$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

## Related Files

- [01_hypothesis.md](01_hypothesis.md)
- [04_divergence_map.md](04_divergence_map.md)
- [06_validation.md](06_validation.md)
- [07_reflections.md](07_reflections.md)
