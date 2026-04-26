# Operator‑Entscheidung: Welcher Datei‑Dienst soll genutzt werden?

## Das Problem

Nutzer Denis hat einen 140 MB Ordner, den er mit mehreren KI‑Web‑Chats teilen möchte.  
Einige akzeptieren Tresorit Send (Zero‑Knowledge), andere blockieren ihn.

## Zwei stabile Achsen (kein Narrativ, nur Funktion)

| Achse | Dienst | Datenschutz | Kompatibilität |
|-------|--------|-------------|----------------|
| A – Datenschutz zuerst | Tresorit Send | ✅ Zero‑Knowledge | ❌ Nur 4/7 Modelle |
| B – Kompatibilität zuerst | WeTransfer (mit Passwort) | ❌ Serverseitig sichtbar | ✅ Alle 7 Modelle |

## Entscheidungsmatrix

| Wenn du priorisierst... | Dann nutze... | Weil... |
|-------------------------|---------------|---------|
| Maximaler Datenschutz + du brauchst Gemini/Mistral/Qwen nicht | Tresorit Send | DeepSeek, Meta, Copilot, ChatGPT funktionieren |
| Maximale Kompatibilität + du brauchst alle Modelle | WeTransfer (mit Passwort) | Alle Web‑Chats akzeptieren einfache HTTP‑Downloads |
| Beides (Hybrid) | Kern‑Spezifikation auf HTTP + schwere Daten auf Tresorit | Alle Modelle sehen die Spezifikation; nur kompatible laden Details |

## Angewandte DNS‑Operatoren

**Operator: `FALSIFICATION` (Falsifikation)**
> Vor der Verallgemeinerung: Teste ein Gegenbeispiel.

Denis testete DeepSeek. Es funktionierte. Copilots Behauptung scheiterte sofort.

**Operator: `LIVE_TRACKING` (Live‑Verfolgung)**
> Überwache $\Delta_{total}$ während des Gesprächs.

Nach Antwort 1: $\Delta_{total}=0.68$ → Das System hätte „Narrativ‑Risiko“ markiert, bevor sich die Behauptung verbreiten konnte.

## Delta Div ($\Delta_{div}$)

\[
\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})
\]

Die hohe Divergenz ($\Delta_{div} = 0.742$ im vollständigen Protokoll) bestätigt, dass keine universelle Verallgemeinerung möglich ist.

## Endgültige Entscheidung (für Denis’ Workflow)

> Bleibe bei Tresorit Send. Der Verlust von Gemini/Mistral/Qwen ist für deinen aktuellen Workflow kein funktionaler Verlust.  
> Wenn du später Gemini als Hauptmodell benötigst, wechsle zu WeTransfer – nicht wegen Ideologie, sondern weil Google den Link blockiert.

Die Entscheidung basiert auf technischer Kompatibilität, nicht auf Copilots geopolitischen Narrativ.

## Verwandte Dateien

- [01_hypothesis.md](01_hypothesis.md)
- [05_synthesis.md](05_synthesis.md)
- [06_validation.md](06_validation.md)
- [07_reflections.md](07_reflections.md)
