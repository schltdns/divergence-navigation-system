# Divergence Map – Pairwise $\Delta_{div}$ Matrix

## Validated Baseline (Mistral & Qwen)

|       | DS   | CP   | GM   | MS   | MT   | QW   |
|-------|------|------|------|------|------|------|
| **DS** | 0.000 | 0.645 | 0.643 | 0.622 | 0.638 | 0.570 |
| **CP** | 0.645 | 0.000 | 0.738 | 0.682 | 0.641 | 0.726 |
| **GM** | 0.643 | 0.738 | 0.000 | 0.672 | 0.745 | 0.658 |
| **MS** | 0.622 | 0.682 | 0.672 | 0.000 | 0.652 | 0.610 |
| **MT** | 0.638 | 0.641 | 0.745 | 0.652 | 0.000 | 0.611 |
| **QW** | 0.570 | 0.726 | 0.658 | 0.610 | 0.611 | 0.000 |

**Legend:**  
- **DS** = DeepSeek  
- **CP** = Copilot  
- **GM** = Gemini  
- **MS** = Mistral  
- **MT** = Meta  
- **QW** = Qwen  

## Key Observations

| Observation | Value | Interpretation |
|-------------|-------|----------------|
| **Highest divergence** | 0.745 (Gemini ↔ Meta) | Both "Western", but semantically far apart |
| **Copilot's minimum divergence** | 0.641 (to Meta) | Still high – Copilot is isolated |
| **Lowest divergence** | 0.570 (DeepSeek ↔ Qwen) | Both Chinese, but likely due to technical similarity, not origin |
| **Copilot ↔ Qwen** | 0.726 | Near-total semantic breakdown |

## Copilot's Self-Matrix (as estimated by Copilot)

|       | DS   | CP   | GM   | MS   | MT   | QW   |
|-------|------|------|------|------|------|------|
| **CP** | 0.78 | 0.00 | 0.82 | 0.79 | 0.75 | 0.85 |

**Interpretation:** Copilot admits he shares <25% semantic basis with any other model. He is an "epistemic island."

## Delta Div ($\Delta_{div}$)

$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$

For this case, the average pairwise $\Delta_{div}$ across all 15 pairs is **0.657**.

## Visual Heatmap

![Heatmap](figures/heatmap.png)

*The heatmap visualizes the pairwise divergences. Darker red indicates higher divergence (more disagreement).*

## Related Files

- [01_hypothesis.md](01_hypothesis.md)
- [02_threshold.md](02_threshold.md)
- [03_outputs/](03_outputs/)
- [05_synthesis.md](05_synthesis.md)
- [06_validation.md](06_validation.md)
