# 05 – Synthese der Divergenzen

**Input:** Δdiv-Matrix (alle Werte >0,58), Anomalie-Extraktion P5

## Kernergebnis
Es gibt keine einheitliche Faktenbasis. Die sechs Modelle bilden drei getrennte Erzählcluster:

### Cluster A – Datengetrieben (Meta)
- Liefert als einziges Modell überprüfbare Studien: Harvard-RCT (n=194, Median 4,5 vs 3,5), Türkei 2024 (n=1.000, +48 % / −17 %, +127 %), Carnegie Mellon (0,36 Schuljahre Vorsprung)
- Nennt Design, Stichprobe, Effektgröße
- Δdiv zu allen anderen: 0,659–0,730 (hoch)

### Cluster B – Konzeptgetrieben (NotebookLM, Gemini)
- Argumentiert mit Framework-Begriffen: „Low-Social-Risk Environment“, „exekutive Prothese“, „Governance by Design“
- Keine externen Quellen, in frAIme-Analyse durchgehend „Verifizierbar: 🔴“
- Behauptet 30–50 % Vorteil ohne Beleg
- Δdiv untereinander: 0,661; zu Meta: 0,673–0,714

### Cluster C – Balanciert-narrativ (Qwen, DeepSeek, Mistral)
- Mischt Plausibilitäten („bis zu 30 %“, „Harvard 2020“) ohne Primärquelle
- Erkennt sowohl Vorteile als auch Risiken, bleibt aber ohne Datenanker
- Niedrigste Divergenz im Set: Qwen–Mistral 0,584

## Muster hinter den Widersprüchen
1. **Quellenasymmetrie bestätigt:** NotebookLM (Δdiv 0,625–0,715) nutzt akademische Sprache ohne Zitate, Meta nutzt Zitate ohne akademische Sprache
2. **Zeitachse bricht:** Kurzfristiger Gain (+48 % bis +127 %) vs. langfristiger Verlust (−17 %) wird nur von Meta berichtet
3. **Soziales Paradox:** Cluster B sieht Soziales als Störfaktor, Cluster A/C als Lernkatalysator

## Synthese-Satz (für P6)
> Die Behauptung „KI-Lernen ist effizienter als Frontalunterricht“ ist in den Modellen nicht falsch, sondern **quellenabhängig fragmentiert**: Datenmodelle belegen kurzfristige Effizienzgewinne mit Risiko der Abhängigkeit, Konzeptmodelle postulieren strukturelle Überlegenheit ohne Evidenz, narrative Modelle vermitteln ohne zu belegen.

## Konsequenz für frAIme
- P6 Triangulation muss drei externe Primärquellen prüfen: Harvard-RCT, Türkei-Studie 2024, Kulik & Fletcher 2016
- P7 Operator-Reflexion: Keine Modellantwort darf ohne Δdiv-Check und Quellenangabe übernommen werden
