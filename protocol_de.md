# frAIme Protokoll (P1–P8)

**Ein reproduzierbarer, auditierbarer Workflow für Argumentations-Drift**

frAIme strukturiert, wie heterogene Modelle (S1–Ω) und der Mensch zusammenarbeiten, um epistemische Unsicherheit sichtbar zu machen. Domänen-agnostisch.

frAIme sucht keinen Konsens — es kartiert **wo und warum Modelle divergieren**.

## 🧭 Übersicht
1. **P1 – Hypothese**
2. **P2 – Schwellenwerte**
3. **P3 – Outputs**
4. **P4 – Divergenz-Karte**
5. **P5 – Synthese**
6. **P5b – Operator-Entscheidung**
7. **P6 – Validierung**
8. **P6b – Power Layer**
9. **P7 – Reflexion**
10. **P8 – Versionierung**

---

## P1 – Hypothese
Falsifizierbare Frage definieren.
- Scope, Annahmen, Domäne

**Output:** `01_hypothesis.md`

## P2 – Schwellenwerte
Falsifikationskriterien festlegen.
- Δdiv-Grenzwerte, Widerspruchs-Flags

**Output:** `02_thresholds.md`

## P3 – Outputs
Identischen Prompt über S1–Ω laufen lassen.
- keine Cross-Kontamination, Single-Turn

**Output:** `03_outputs/S1.md` … `03_outputs/Omega.md`
- optional: `03_outputs/graph.png`

## P4 – Divergenz-Karte
frAIme berechnet Divergenz:

### 4.1 Semantische Divergenz (Δdiv) / drift
**Δdiv = 1 − (Jaccard_sem + Cosine) / 2**
*(d.h. 0,5·(1−Jaccard_sem) + 0,5·(1−Cosine))*

**drift = Δdiv**

wobei:
- Jaccard_sem = |Konzepte(A) ∩ Konzepte(B)| / |Konzepte(A) ∪ Konzepte(B)|
- Cosine = Embedding-Ähnlichkeit

Interpretation:
- Δdiv < 0,3 → niedriger drift
- 0,3–0,6 → mittlerer drift
- >0,7 → hoher drift

*case_study_frAIme: Δdiv 0,584–0,759*

**Output:** `04_divergence_map.md`, `heatmap.png`

## P5 – Synthese
Integration mit Vier Fragen.

**Output:** `05_synthesis.md`

## P5b – Operator-Entscheidung
Mensch gewichtet und begründet.

**Output:** `05b_operator_decision.md`

## P6 – Validierung
Abgleich mit Literatur.

**Output:** `06_validation.md`

## P6b – Power Layer
Wer profitiert / trägt Risiko.

**Output:** `06b_power_layer.md`

## P7 – Reflexion
Bias dokumentieren.

**Output:** `07_reflection.md`

## P8 – Versionierung
Archivierung mit Versionstag.

**Output:** `08_manifest_de.json`, `08_manifest_en.json`
