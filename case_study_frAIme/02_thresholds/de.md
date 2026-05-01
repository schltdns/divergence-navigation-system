# 02 – Schwellenwerte & Falsifikation

## Δdiv / drift Interpretation (canonical)

| Wertebereich | Label | Handlungsempfehlung |
|-------------|-------|-------------------|
| < 0,15 | Konsens | Keine weitere Prüfung nötig |
| 0,15–0,35 | Leichte Abweichung | Kontext prüfen, dokumentieren |
| 0,35–0,50 | Signifikante Divergenz | Externe Validierung (P6) anstoßen |
| 0,50–0,70 | Quellenasymmetrie | Power Layer Check (P6b) aktivieren |
| > 0,70 | Epistemischer blinder Fleck | F1-Trigger: DeepSeek-Intervention + Operator-Eskalation |

## Zusatz-Flags (DNS P4.2)

**Widerspruchs-Flag**
- Auslösung: ≥2 Modelle treffen explizit gegenteilige Aussagen zur selben Frage

**Quellenasymmetrie-Flag**
- Auslösung: Ein Modell ist zu allen anderen isoliert (min Δdiv > 0,5) UND die Analyse der Referenzen zeigt eine einseitig beschränkte Quellenbasis
- In diesem Lauf: NotebookLM = nur frAIme/DNS, andere = KMK, UNESCO, OECD, Schulbarometer, AKTIV, PAIR

**Falsifikations-Check**
- Hypothese H1 gilt als falsifiziert, wenn das Quellenasymmetrie-Flag nicht auslöst
