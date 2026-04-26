# Divergenzkarte – Paarweise $\Delta_{div}$ Matrix

## Validierte Baseline (Vollständiges Protokoll)

|       | DS   | CP   | GM   | MS   | MT   | QW   |
|-------|------|------|------|------|------|------|
| **DS** | 0.000 | 0.749 | 0.736 | 0.776 | 0.762 | 0.771 |
| **CP** | 0.749 | 0.000 | 0.742 | 0.798 | 0.783 | 0.777 |
| **GM** | 0.736 | 0.742 | 0.000 | 0.712 | 0.677 | 0.690 |
| **MS** | 0.776 | 0.798 | 0.712 | 0.000 | 0.707 | 0.730 |
| **MT** | 0.762 | 0.783 | 0.677 | 0.707 | 0.000 | 0.717 |
| **QW** | 0.771 | 0.777 | 0.690 | 0.730 | 0.717 | 0.000 |

**Legende:**  
- **DS** = DeepSeek  
- **CP** = Copilot  
- **GM** = Gemini  
- **MS** = Mistral  
- **MT** = Meta  
- **QW** = Qwen  

## Wichtige Beobachtungen

| Beobachtung | Wert | Interpretation |
|-------------|------|----------------|
| **Höchste Divergenz** | 0.798 (Copilot ↔ Mistral) | Narrativ vs. Compliance‑Framing |
| **Copilots minimale Divergenz** | 0.742 (zu Gemini) | Immer noch in der kontroversen Zone |
| **Niedrigste Divergenz** | 0.677 (Gemini ↔ Meta) | Beide fokussieren auf technische Filter |
| **Durchschnitt (paarweise)** | 0.742 | Höher als 0.657 – Nachfragen erhöhen die Divergenz |
| **Copilot ↔ DeepSeek** | 0.749 | Grundlegende Meinungsverschiedenheit über Expertise |

## Interpretation

> Der Anstieg von 0.657 (nur technische Antworten) auf 0.742 (vollständiges Protokoll) beweist: Das Narrativ‑Risiko liegt nicht in der ersten Behauptung, sondern in der Weigerung, sich unter kritischer Prüfung selbst zu korrigieren.

## Delta Div ($\Delta_{div}$)

\[
\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})
\]

## Visuelle Heatmap

![Heatmap](../../figures/heatmap.png)

## Verwandte Dateien

- [01_hypothesis.md](../../03_pedagogy/de/01_hypothesis.md)
- [02_threshold.md](../../03_pedagogy/de/02_threshold.md)
- [03_outputs/](../../03_pedagogy/de/03_outputs/)
- [05_synthesis.md](../../03_pedagogy/de/05_synthesis.md)
- [06_validation.md](../../03_pedagogy/de/06_validation.md)
