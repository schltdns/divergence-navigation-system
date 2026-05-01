# frAIme Protokoll (P1–P8)

**Reproduzierbarer Workflow für Argumentations-Drift**

frAIme strukturiert, wie heterogene Modelle und der Mensch zusammenarbeiten, um epistemische Unsicherheit sichtbar zu machen. Es ist domänenunabhängig.

frAIme sucht keinen Konsens — es kartiert, **wo und warum Modelle auseinanderlaufen**.

---

## 🧭 Überblick

1. **P1 — Hypothese**
2. **P2 — Schwellenwerte**
3. **P3 — Sammeln**
4. **P4 — Divergenz-Karte**
5. **P5 — Synthese**
6. **P5b — Operator-Entscheidung**
7. **P6 — Validierung**
8. **P6b — Power Layer**
9. **P7 — Reflexion**
10. **P8 — Versionierung**

---

## P1 — Hypothese

Falsifizierbare Frage definieren.
- Scope, Annahmen, Domäne

**Output:** `01_hypothesis/`

## P2 — Schwellenwerte

Falsifikationskriterien festlegen.
- Drift-Schwellen, Widerspruchs-Flags

**Output:** `02_thresholds/`

## P3 — Sammeln

Identischen Prompt über verschiedene Modelle laufen lassen.
- keine Kreuzkontamination, single-turn

## P4 — Divergenz-Karte

frAIme berechnet Divergenz auf zwei Ebenen:

### 4.1 Semantischer Drift

Drift = 1 - (Jaccard_sem + Cosine) / 2

wobei:
- Jaccard_sem = |Konzepte(A) ∩ Konzepte(B)| / |Konzepte(A) ∪ Konzepte(B)|
  (Konzepte via Nomen-Phrasen, nicht Tokens)
- Cosine = Embedding-Ähnlichkeit (sentence-transformers)

Interpretation:
- Drift < 0,3 → Konvergenz
- 0,3–0,6 → produktive Reibung
- >0,7 → blinder Fleck

*Referenz: case_study_frAIme „KI-Lernen vs Frontalunterricht“ – Drift 0,584–0,759 trotz scheinbarem Konsens; nur ein Modell lieferte Primärquellen.*

### 4.2 Graph-Divergenz

Modelle sind Knoten in gerichtetem Graph G = (V,E). Kantengewicht w_ij = 1 - Ähnlichkeit(Output_i, Output_j). Hohe Gewichte = Reibungspunkte.

**Output:** `04_divergence_map/`

## P5 — Synthese

Integration mit den Vier Fragen (Thema, Idee, Belegbar, Verständlich).

**Output:** `05_synthesis/`

## P5b — Operator-Entscheidung

Mensch gewichtet, begründet, wählt.

**Output:** `05b_operator_decision/`

## P6 — Validierung

Abgleich mit Daten, Literatur, Experten.

**Output:** `06_validation/`

## P6b — Power Layer

Wer steuert, profitiert, trägt Risiko, wird ausgeschlossen.

**Output:** `06b_power_layer/`

## P7 — Reflexion

Bias, kognitive Last, Unsicherheit dokumentieren.

**Output:** `07_reflection/`

## P8 — Versionierung

Alle Artefakte mit Versionstag archivieren.

**Output:**
- `08_manifest_de.json` / `08_manifest_en.json`
- Zenodo DOI: 10.5281/zenodo.19793185
