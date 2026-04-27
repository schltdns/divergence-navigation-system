<p align="center">
  <img src="04_archive_legacy/docs/assets/frAIme_logo_wordmark.png" alt="frAIme – Argumentation Drift Monitor" width="650"/>
</p>

<h1 align="center">frAIme</h1>

<p align="center">
  <strong>Argumentation Drift Monitor</strong>
</p>

# frAIme
## Argumentation Drift Monitor

🟢 Topic consistency • 🟡 Idea emergence • 🔴 Verifiability • 🔵 Understandability

https://doi.org/10.5281/zenodo.19793185

**frAIme macht Unsicherheit sichtbar – es schafft den Rahmen für verlässliche KI-Nutzung.**
frAIme ist Governance by Design, nicht Ethik per Deklaration.

Für Klassenzimmer: vier Fragen, Ampel, fertig.
Für Forschung: messbare Divergenz (Δdiv), auditierbar.

**Version:** V1.0.0 (2026-04-26) – Stable Release

---

## Start in 2 Minuten
**Die Vier-Fragen-Methode**
Prüfe jede LLM-Antwort:

1. On topic? 🟢 / 🔴
2. Neue Idee? 🟢 / 🟡 / 🔴
3. Verifizierbar? (Zahl, Datum, Ort, wenn-dann) 🟢 / 🔴
4. Verständlich? 👍 / 👎

Gute Antwort = 🟢 + 👍

Kein Account. Keine API. Funktioniert auf Papier.

## 🚀 Live Demo
👉 https://divergence-navigation-system.streamlit.app

Teste mit eingebauten Beispielen („The Copilot Crash“) oder eigenen Texten.

## Was ist neu in V1.0.0
1. **Rebranding:** früher DNS – jetzt frAIme (Epistemic Governance Framework)
2. **Getestet mit Copilot Crash:** Δdiv = 0,742 deckte erfundene „West vs. China“-Narrative auf
3. **Live Δdiv-Tracking:** Frontend berechnet Δtotal während des Gesprächs
4. **Reichweite:** 3.270 Clones / 1.126 Unique Cloner in 14 Tagen

## Neue Case Study: KI-Lernen vs Frontalunterricht
**Ersetzt den EU-AI-Act-Teil – realer Einsatz in Bildung**

- **6 Modelle, gleiche Frage:** „Ist KI-Lernen effizienter?“
- **Vier Fragen:** alle 🟢 bei „On topic“, alle 👍 bei „Verständlich“ – scheinbarer Konsens
- **Δdiv-Matrix:** 0,584–0,759 – hohe Divergenz trotz Einigkeit
- **Triangulation:**
    - Harvard RCT 2025 (n=194): Median 4,5 vs 3,5, Zeit 49 vs 60 Min – BESTÄTIGT
    - Türkei UPenn 2024 (n=1.000): +48 % Übungen / −17 % Test – BESTÄTIGT
    - Kulik & Fletcher 2016: +0,66 SD – BESTÄTIGT
- **Erkenntnis:** Hohe Δdiv zeigte nicht „falsch“, sondern „quellenarm“. Nur Meta-Cluster lieferte Primärdaten.

**frAIme-Lektion:** Plausibilität ≠ Evidenz. Δdiv lokalisiert Prüfbedarf.

## Technik
Δdiv = 0.5·(1−Jaccard) + 0.5·(1−Cosine)

Grenzwerte:
- <0,3 = Konvergenz
- 0,3–0,5 = Drift
- 0,5–0,7 = hohes Risiko
- >0,7 = contested

Zwei Ebenen: Frontend (Vier Fragen) + Backend (Safety Layer, Hash-Anker, Multi-Agent-Log)
