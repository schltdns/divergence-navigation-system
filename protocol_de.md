# frAIme Protokoll (P1–P8)

## P1 – Hypothese → `01_hypothesis/`
Falsifizierbare Frage definieren.

## P2 – Schwellenwerte → `02_thresholds/`
Falsifikationskriterien festlegen.

## P3 – Sammeln → `03_outputs/`
Identischen Prompt über S1–Ω laufen lassen.

## P4 – Divergenz-Karte → `04_divergence_map/`
**Δdiv = 1 - (Jaccard_sem + Cosine) / 2**  
*drift = vereinfachter Begriff*

wobei:
- Jaccard_sem = |Konzepte(A) ∩ Konzepte(B)| / |Konzepte(A) ∪ Konzepte(B)|
  (Konzepte via Nomen-Phrasen, nicht Tokens)
- Cosine = Embedding-Ähnlichkeit (sentence-transformers)

Interpretation:
- Δdiv < 0,3 → Konvergenz
- 0,3–0,6 → produktive Reibung
- >0,7 → blinder Fleck

*Referenz: case_study_frAIme – Δdiv 0,584–0,759 trotz scheinbarem Konsens*

## P5 – Synthese → `05_synthesis/`
Integration mit Vier Fragen.

## P5b – Operator-Entscheidung → `05b_operator_decision/`
Mensch gewichtet und begründet.

## P6 – Validierung → `06_validation/`
Abgleich mit Literatur.

## P6b – Power Layer → `06b_power_layer/`
Wer profitiert / trägt Risiko.

## P7 – Reflexion → `07_reflection/`
Bias dokumentieren.

## P8 – Versionierung → `08_manifest_de.json`
Version und DOI archivieren.
