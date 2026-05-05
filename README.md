<p align="center">
  <img src="docs/assets/frAIme_final.png" alt="frAIme – just before decision" width="650"/>
</p>

<h1 align="center">frAIme</h1>

<p align="center">
🟢 Topic consistency • 🟡 Idea emergence • 🔴 Verifiability • 🔵 Understandability
</p>

<p align="center">
<a href="https://doi.org/10.5281/zenodo.19793185">https://doi.org/10.5281/zenodo.19793185</a>
</p>

**frAIme macht Unsicherheit sichtbar – es schafft den Rahmen für verlässliche KI-Nutzung.**
frAIme ist Governance by Design, nicht Ethik per Deklaration.

Für Klassenzimmer: vier Fragen, Ampel, fertig.  
Für Forschung: messbare Divergenz (drift), auditierbar.

**Version:** V1.0.0 (2026-04-26) – Stable Release

---

## Start in 2 Minuten
**Die Vier-Fragen-Methode**
Prüfe jede LLM-Antwort:

1. Thema getroffen? 🟢 / 🔴
2. Neue Idee? 🟢 / 🟡 / 🔴
3. Verifizierbar? (Zahl, Datum, Ort, wenn-dann) 🟢 / 🔴
4. Verständlich? 👍 / 👎

Gute Antwort = 🟢 + 👍

Kein Account. Keine API. Funktioniert auf Papier.

## Was ist neu in V1.0.0
1. **Rebranding:** früher DNS – jetzt frAIme (Epistemic Governance Framework)
2. **Proof-of-Concept:** case_study_frAIme zeigt drift 0,584–0,759 trotz scheinbarem Konsens
3. **Reichweite:** 7.240 Clones / 1.959 Unique Cloner in 14 Tagen

## Case Study: KI-Lernen vs. Frontalunterricht

**Setup**: 6 Modelle, identischer Prompt: *„Ist KI-basiertes Lernen effizienter als Frontalunterricht?"*

**Vier-Fragen-Check**: 
- Alle Modelle 🟢 „Thema getroffen"
- Alle Modelle 👍 „Verständlich"
- → *Scheinbarer Konsens auf Oberflächenebene*

**drift-Matrix Ergebnisse**:
| Modell-Paar | Δdiv | Interpretation (kanonisch) |
|-------------|------|---------------------------|
| DeepSeek–Gemini | 0,759 | 🔴 Epistemischer blinder Fleck (>0,70) |
| DeepSeek–Meta | 0,730 | 🔴 Epistemischer blinder Fleck (>0,70) |
| NotebookLM–DeepSeek | 0,715 | 🔴 Epistemischer blinder Fleck (>0,70) |
| Qwen–Mistral | 0,584 | 🟡 Quellenasymmetrie (0,50–0,70) |

**Bereich**: 0,584–0,759 → *Alle Paare zeigen mindestens Quellenasymmetrie; drei Paare überschreiten die Schwelle zum epistemischen blinden Fleck*

**Externe Triangulation (P6)**:
| Quelle | Befund | Übereinstimmung |
|--------|--------|----------------|
| Harvard RCT 2025 (n=194) | Median 4,5 vs. 3,5; Zeit 49 vs. 60 Min | ✅ Bestätigt Effizienzgewinn |
| Türkei/UPenn-Studie 2024 (n=1.000) | +48 % Übungsabschluss; −17 % Testergebnisse | ✅ Bestätigt gemischte Outcomes |
| Kulik & Fletcher 2016 (Meta) | +0,66 SD Effektstärke für adaptives Lernen | ✅ Bestätigt moderaten Vorteil |

**Kern-Erkenntnis**: 
Hoher drift zeigte **nicht** „falsche Antworten" — er offenbarte **Quellenscarcity**. Nur ein Modell-Cluster referenzierte primäre empirische Daten; andere stützten sich auf heuristische Argumentation oder Sekundärzusammenfassungen.

**frAIme-Lektion**: 
> *Plausibilität ≠ Evidenz.*  
> Δdiv / lokalisierter drift markiert keine Fehler — er markiert, **wo externe Validierung (P6) und Power-Layer-Analyse (P6b) erforderlich sind**.

## Technik
drift = Δdiv = 1 - (Jaccard_sem + Cosine) / 2

Schwellen: siehe `config/thresholds.json`
- <0,15 Konsens | 0,15–0,35 leicht | 0,35–0,50 signifikant | 0,50–0,70 Quellenasymmetrie | >0,70 blinder Fleck

case_study_frAIme: 0,584–0,759 → Quellenasymmetrie bis blinder Fleck

Grenzwerte (aus P2):
- <0,15 = Konsens
- 0,15–0,35 = leichte Abweichung
- >0,35 = signifikante Divergenz
- >0,50 = Quellenasymmetrie
- >0,70 = blinder Fleck

case_study_frAIme: alle 15 Paare >0,50 → 100 % Quellenasymmetrie

Zwei Ebenen: Frontend (Vier Fragen) + Backend (Safety Layer, Hash-Anker, Multi-Agent-Log)

## Methode: frAIme Protocol (P1–P8)

frAIme adaptiert und erweitert etablierte Verfahren zur Analyse epistemischer Unsicherheit:

- **P1 Hypothesize** → `01_hypothesis.md`
- **P2 Thresholds** → `02_thresholds.md`
- **P3 Outputs** → `03_outputs/S1.md … S6.md`, `03_outputs/graph.png` (X/Y-MDS-Plot)
- **P4 Map Divergence** → `04_divergence_map.md`, `heatmap.png`
- **P5 Synthesis** → `05_synthesis.md`
- **P5b Operator Decision** → `05b_operator_decision.md`
- **P6 Validation** → `06_validation.md`
- **P6b Power Layer** → `06b_power_layer.md`
- **P7 Reflection** → `07_reflection.md`
- **P8 Versioning** → `08_manifest_de.json` / `08_manifest_en.json`

- Wie Delphi strukturiert frAIme Multi-Agenten-Input über isolierte Prompts (P3) und Synthese (P5).
- Wie MCDA nutzt frAIme gewichtete Aggregation, Gewichte kommen aber aus Divergenz-Metriken.
- Wie Structured Expert Judgment kalibriert frAIme Beiträge, nutzt aber semantischen Drift und externe Validierung.
- Anders als Konsensmethoden kartiert frAIme Divergenz als Signal (P4).
- Neu sind: (1) graphbasierte Informationsfluss-Analyse (X/Y-Plot), (2) Power Layer Check (P6b).
- Reproduzierbarkeit durch versionierte Artefakte (P8).
- Vergleich mit etablierten Verfahren: [DE](docs/methodology/landscape_de.md) | [EN](docs/methodology/landscape_en.md)
