# 02 – Schwellenwerte & Falsifikation

| Kriterium | Schwelle | Bedeutung |
|---|---|---|
| Δdiv < 0,30 | Konvergenz | Modelle teilen Kernkonzepte und Schlussfolgerungen |
| 0,30 ≤ Δdiv ≤ 0,50 | Produktive Reibung | Unterschiedliche Schwerpunkte, Aussagen kompatibel |
| 0,50 < Δdiv ≤ 0,70 | Hohe Divergenz | Perspektiven möglicherweise unvereinbar |
| Δdiv > 0,70 | Epistemischer blinder Fleck | Fundamentale Divergenz, F1-Trigger |

## Zusatz-Flags (DNS P4.2)

**Widerspruchs-Flag**
- Auslösung: ≥2 Modelle treffen explizit gegenteilige Aussagen zur selben Frage

**Quellenasymmetrie-Flag**
- Auslösung: Ein Modell ist zu allen anderen isoliert (min Δdiv > 0,5) UND die Analyse der Referenzen zeigt eine einseitig beschränkte Quellenbasis
- In diesem Lauf: NotebookLM = nur frAIme/DNS, andere = KMK, UNESCO, OECD, Schulbarometer, AKTIV, PAIR

**Falsifikations-Check**
- Hypothese H1 gilt als falsifiziert, wenn das Quellenasymmetrie-Flag nicht auslöst
