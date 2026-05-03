# Landscape Comparison: frAIme vs. etablierte Methodiken

> **Dokumentzweck**: Vergleichende Einordnung von frAIme in die Landschaft von Decision-Support, Unsicherheitsquantifizierung und AI-Governance.  
> **QUELLENMATRIX-Konformität**: Kernquellen = Must; Ergänzende = Nice-to-have; Abweichungen explizit markiert.  
> **Version**: 1.0.0 | **Erstellt**: 2026-05-03

---

## 1. Scope & Methodik

### 1.1 Vergleichskriterien
| Kriterium | Definition | frAIme-Umsetzung |
|-----------|------------|------------------|
| **Multi-Source-Input** | Strukturierte Aggregation unabhängiger Bewertungen | P3: Isolierte Prompts an S1–Ω, keine Cross-Kontamination |
| **Divergenz-Handling** | Umgang mit Uneinigkeit | P4: Δdiv als Signal (nicht Fehler); explizite Kartierung |
| **Ethische Reflexion** | Integration von Macht/Risiko-Analyse | P6b: Power Layer Check (verpflichtend) |
| **Auditierbarkeit** | Reproduzierbarkeit und Versionskontrolle | P8: Versionierte Manifeste (`08_manifest_*.json`) |

### 1.2 Quellenklassifikation
| Typ | Beispiele | Rolle |
|-----|-----------|-------|
| **Kern (Must)** | Delphi-Literatur; MCDA-Standards; Jaccard/Cosine-Definitionen; NIST AI RMF; ISO/IEC 42001 | Basis für methodische Ansprüche |
| **Ergänzend** | Preprints zu Multi-Agent-Governance; UQ-Reviews | Kontext, nicht fundierend |
| **frAIme-spezifisch** | Δdiv-Formel; P1–P8; Power Layer | Innovationsansprüche |

---

## 2. Vergleichende Analyse

| Framework | Ähnlichkeit | Kritischer Unterschied | Quelle |
|-----------|-------------|------------------------|--------|
| **Delphi-Methode** | Strukturierter Multi-Experten-Input | Ziel: *iterativer Konsens*; frAIme: *Divergenz-Erhalt* | Kern |
| **MCDA** | Gewichtete Aggregation | Gewichte: *Experten-vergeben*; frAIme: *Δdiv-abgeleitet* | Kern |
| **Structured Expert Judgment** | Kalibrierung von Beiträgen | Kalibrierung: *historische Genauigkeit*; frAIme: *semantischer Drift + Validierung* | Kern |
| **AI Agent Governance** | Phase-Gating | Fokus: *operative Kontrolle*; keine Divergenz-Metrik | Ergänzend |
| **Governance-as-a-Service** | Multi-Agent-Runtime | Trust: *regelbasiert*; frAIme: *epistemisch* | Ergänzend |
| **Uncertainty Quantification** | Aleatorisch/epistemisch | Fokus: *statistisch*; frAIme: *semantisch* | Ergänzend |

### 2.1 Neue Beiträge von frAIme
1. **Hybride Δdiv-Metrik**: `Δdiv = 1 − (Jaccard_sem + Cosine) / 2`  
   – Kombiniert Konzept-Overlap mit Vektor-Ähnlichkeit

2. **Divergenz-als-Signal (P4)**:  
   – Klassisch: Optimierung *auf Konsens*; frAIme: Optimierung *auf sichtbare Unsicherheit*  
   – Schwellen: <0,15 Konsens; >0,70 blinder Fleck

3. **Power Layer Check (P6b)**:  
   – Verpflichtend: "Wer profitiert? Wer trägt Risiko?"

4. **Versionierte Audit-Artefakte (P8)**:  
   – Maschinenlesbare Manifeste für EU AI Act-Konformität

---

## 3. Abweichungen (explizit)
| Etablierte Norm | frAIme | Begründung |
|-----------------|--------|------------|
| Konsens als Ziel | Divergenz als Signal | Konsens kann geteilten Bias spiegeln |
| Statische Gewichte | Dynamische Δdiv-Gewichte | Objektiv, kontextsensitiv |
| Ethik als Add-on | Ethik eingebettet (P6b) | Machtanalyse ist entscheidungsrelevant |

---

## 4. Reproduzierbarkeit

### 4.1 Kernquellen
1. Dalkey & Helmer (1963). Delphi Method.  
2. Belton & Stewart (2002). MCDA.  
3. Cooke (1991). Experts in Uncertainty.  
4. NIST (2023). AI RMF.  
5. ISO/IEC 42001:2023.

### 4.2 frAIme-Artefakte
- DOI: `10.5281/zenodo.19793185`  
- Repo: `github.com/schltdns/divergence-navigation-system`

---

## 5. Fazit
frAIme ist kein Ersatz für statistische UQ oder operative Governance. Es ist eine **komplementäre epistemische Schicht**, die die *Qualität von Uneinigkeit* sichtbar macht.
