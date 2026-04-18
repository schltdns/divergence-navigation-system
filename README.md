DNS — Divergence Navigation System
DNS macht Unsicherheit sichtbar – nicht kleiner.
> Für Schule, Ausbildung, Praxis: vier Fragen, Ampel, fertig.  
> Für Forschung: messbare Divergenz (Δdiv), auditierbar nach EU AI Act.
Version: v2.1 (2025-04-15) • DOI: 10.5281/zenodo.19597808 • IPFS: `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy`
---
Start here – 2 Minuten
Die Vier-Fragen-Methode (Frontend)
Jede KI-Antwort wird mit vier Kreuzen geprüft:
On topic? 🟢 / 🔴
New idea? 🟢 / 🟡 / 🔴
Verifiable? (Zahl, Datum, Ort, wenn-dann) 🟢 / 🔴
Understandable? 👍 / 👎
Gute Antwort = 🟢 + 🟢 + 👍
Kein Account. Keine API. Funktioniert auf Folie.  
→ PDF: `teaching/vier_fragen_methode.pdf` (DE) | `teaching/four_questions_method.pdf` (EN)
Warum das reicht
Lehrer behalten Deutungshoheit (Art. 14 AI Act – Human Oversight)
Schüler lernen, Halluzinationen zu filtern, nicht zu fürchten
Entscheider sehen, wo Modelle aufhören, sich einig zu sein
---
Was DNS technisch ist
DNS nutzt strukturierte Divergenz zwischen Modellen als Navigationssignal.
Kernmetrik Δdiv
```
Δdiv = 0.5 × (1 - Jaccard) + 0.5 × (1 - Cosine)
```
0.05 = Konvergenz (formale Logik)
0.62 = strukturierte Divergenz (Labour 2030)
0.78 = contested (Cognitive Safety)
Zwei Schichten
Frontend: Vier Fragen (jeder kann es)
Backend: Safety Layer (JSON-Schema, Hash-Anker, SHAP-Monitoring) – für EU-Konformität
→ Details: `docs/HOW_IT_WORKS.md`
---
EU AI Act Mapping
Anforderung	DNS Umsetzung
Art. 13 Transparenz	Vier Fragen dokumentieren Bewertung
Art. 14 Menschliche Aufsicht	Operator muss Synthese begründen (P7)
Art. 15 Robustheit	Δdiv + Falsifikationsregeln 1–4
→ Mapping: `teaching/mapping_ai_act.pdf`
---
Quick Start für Entwickler
Lies `docs/HOW_IT_WORKS.md` (10 Min Beispiel)
Nutze `safety_layer_schema_v2.json` für Logging
Teste mit `minimal_safety_layer.py`
---
Case Studies (v2.1)
Cognitive Safety – Δdiv 0.787, Low-Social-Risk-Hypothese validiert
Labour Market 2030 – Δdiv 0.6256, erste vollständige P1-P8
Archiv: `/archive/` (alte GNS-Modelle, KRI etc.)
---
Lizenz
Code: Apache-2.0
Methode & Docs: CC BY-NC-SA 4.0
> DNS ist Struktur, keine Garantie. Nutzung auf eigene Verantwortung.
---
Zitieren
> Schult, D. (2026). *DNS — Divergence Navigation System (v2.1)*. Zenodo. https://doi.org/10.5281/zenodo.19597808
