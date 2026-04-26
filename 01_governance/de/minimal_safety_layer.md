# minimal_safety_layer.py – Erklärung

Dieses Skript implementiert die **DNS‑Safety‑Layer**‑Logik für frAIme V1.0.0.

## Kernfunktionen

- **`create_log_entry()`** – Erzeugt einen revisionssicheren Log‑Eintrag aus den Vier‑Fragen‑Antworten.  
  Mappt automatisch auf EU AI Act: Art. 13 (Transparenz), Art. 14 (Human Oversight), Art. 9 (Risikomanagement).
- **`hash_entry()`** – Berechnet einen SHA256‑Hash des gesamten Log‑Eintrags. Jede nachträgliche Änderung würde den Hash ungültig machen.
- **`build_merkle_root()`** – Verdichtet eine Liste von Hashes zu einer einzigen Merkle‑Root (z. B. für tägliche Integritätsnachweise).
- **Cross‑Language Integrity Check** – Prüft, ob die LaTeX‑Formeln in deutschen und englischen Markdown‑Dateien identisch sind.  
  Aufruf: `python minimal_safety_layer.py --all`

## Anwendung im frAIme‑Workflow

1. **KI generiert** eine Aussage / Prognose.
2. **Mensch** beantwortet die Vier‑Fragen (per Klick).
3. **Safety Layer** erstellt Log, Hash und ggf. Merkle‑Root.
4. **System** speichert Log und Hash in einer Datenbank.

Der Mensch schreibt kein langes Protokoll – er validiert nur. Der Rest entsteht automatisch.

## Beispielaufruf

```bash
python minimal_safety_layer.py --all                # Prüft alle Case‑Study‑Dateien
python minimal_safety_layer.py de/datei.md en/datei.md   # Prüft ein Paar
