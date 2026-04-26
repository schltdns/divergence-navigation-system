# Validierung: Prüfung der Behauptung gegen die Realität

## Die Behauptung (Copilot, initial)

> "Alle westlichen KI‑Chats akzeptieren Tresorit Send, alle chinesischen blockieren. Das ist kein Zufall – das ist Policy."

## Falsifikationstest

| Test | Erwartet (laut Behauptung) | Tatsächlich | Befund |
|------|----------------------------|-------------|--------|
| DeepSeek (chinesisch) | ❌ blockiert | ✅ funktioniert | **Falsifiziert** |
| Gemini (USA) | ✅ akzeptiert | ❌ blockiert | **Falsifiziert** |
| Mistral (EU) | ✅ akzeptiert | ❌ blockiert | **Falsifiziert** |

**Ergebnis:** Die Behauptung ist falsch. Null unterstützende Evidenz.

## Positive Validierung (technische Wahrheit)

| Modell | Funktioniert? | Technischer Grund |
|--------|---------------|-------------------|
| DeepSeek | ✅ | Liberale Fetch‑Policy |
| Meta | ✅ | Liberale Fetch‑Policy |
| Copilot | ✅ | Liberale Fetch‑Policy |
| ChatGPT | ✅ | Liberale Fetch‑Policy |
| Gemini | ❌ | Restriktive Sandbox |
| Mistral | ❌ | Restriktive Sandbox |
| Qwen | ❌ | Restriktive Sandbox |

## DNS‑Validierungsbewertung

| Kriterium | Status | Erklärung |
|-----------|--------|-----------|
| Falsifizierbarkeit | ✅ Bestanden | Ein Gegenbeispiel zerstörte die Behauptung |
| Reproduzierbarkeit | ✅ Bestanden | Von jedem testbar |
| Technische Spezifität | ✅ Bestanden | Policies, nicht Herkunft |
| Narrativfreiheit | ✅ Bestanden | Keine geopolitischen Annahmen |

## Die einzig gültige Aussage

> "Einige Web‑Chats blockieren Tresorit Send aufgrund technischer Sicherheitsfilter. Andere akzeptieren es aufgrund liberaler Fetch‑Policies. Es gibt kein geopolitisches Muster."

## Delta Div ($\Delta_{div}$)

\[
\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})
\]

Die validierte $\Delta_{div} = 0.742$ (vollständiges Protokoll) bestätigt eine hohe strukturelle Divergenz – die Behauptung ist mathematisch unhaltbar und wird als **kontrovers** klassifiziert.

## Verwandte Dateien

- [01_hypothesis.md](01_hypothesis.md)
- [02_threshold.md](02_threshold.md)
- [05_synthesis.md](05_synthesis.md)
- [05b_operator_decision.md](05b_operator_decision.md)
- [07_reflections.md](07_reflections.md)
