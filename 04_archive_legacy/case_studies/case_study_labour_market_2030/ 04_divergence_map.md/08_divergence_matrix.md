# delta_div – Divergenz der sechs KI-Modell-Antworten (Labour Market 2030)

## Berechnungsmethode
- **Jaccard-Ähnlichkeit** (Token-basiert, Lowercase, Splits)
- **Cosine-Ähnlichkeit** (TF-IDF, `sklearn`)
- Mittelwert aus beiden
- `delta_div = 1 – Mittelwert` (Divergenzmaß, 0 = identisch, 1 = maximal verschieden)

## Gesamtergebnisse

| Kennzahl | Wert |
|----------|------|
| Jaccard-Ähnlichkeit (Mittelwert über 15 Paare) | 0.1923 |
| Cosine-Ähnlichkeit (Mittelwert über 15 Paare) | 0.5564 |
| Mittelwert aus Jaccard & Cosine | 0.3744 |
| **delta_div** | **0.6256** |

Interpretation: Die sechs Antworten weisen eine **moderat hohe Divergenz** auf. Die semantische Struktur (Cosine) ist ähnlicher als die reine Wortwahl (Jaccard).

## Paarweise Divergenzmatrix (6×6)
Reihenfolge der Modelle:  
1. ChatGPT, 2. Claude, 3. Copilot, 4. DeepSeek, 5. Gemini, 6. Grok

|           | ChatGPT | Claude | Copilot | DeepSeek | Gemini | Grok |
|-----------|---------|--------|---------|----------|--------|------|
| ChatGPT   | 0.0000  | 0.6217 | 0.6155  | 0.6152   | 0.7221 | 0.6142 |
| Claude    | 0.6217  | 0.0000 | 0.6074  | 0.5809   | 0.6815 | 0.5879 |
| Copilot   | 0.6155  | 0.6074 | 0.0000  | 0.5492   | 0.6627 | 0.5974 |
| DeepSeek  | 0.6152  | 0.5809 | 0.5492  | 0.0000   | 0.6572 | 0.5630 |
| Gemini    | 0.7221  | 0.6815 | 0.6627  | 0.6572   | 0.0000 | 0.7088 |
| Grok      | 0.6142  | 0.5879 | 0.5974  | 0.5630   | 0.7088 | 0.0000 |

## Auffälligkeiten
- **Höchste Divergenz** (0.7221): zwischen **ChatGPT und Gemini**
- **Niedrigste Divergenz** (0.5492): zwischen **Copilot und DeepSeek**
- Gemini ist zu allen anderen Modellen durchweg am stärksten divergent (alle Werte > 0.65).

## Ausgabe des Skripts (Original)
