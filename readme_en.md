<p align="center">
  <img src="docs/assets/frAIme_final.png" alt="frAIme – just before decision" width="650"/>
</p>

<h1 align="center">frAIme</h1>

<p align="center">
🟢 Topic consistency • 🟡 Idea emergence • 🔴 Verifiability • 🔵 Understandability
</p>

<!-- Badges -->
<p align="center">

  <img alt="Project Status" src="https://img.shields.io/badge/status-active-success">
  <img alt="License" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue">
  <img alt="Docs" src="https://img.shields.io/badge/docs-available-brightgreen">
  <img alt="Languages" src="https://img.shields.io/badge/languages-DE%20%7C%20EN-lightgrey">
  <img alt="Framework Type" src="https://img.shields.io/badge/type-epistemic%20framework-orange">
  <img alt="P1–P8" src="https://img.shields.io/badge/P1–P8-structured-informational">
  <img alt="Δdiv Metric" src="https://img.shields.io/badge/Δdiv-semantic%20divergence-critical">

  <a href="CODE_OF_CONDUCT.md">
    <img alt="Code of Conduct" src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg">
  </a>

  <a href="SECURITY.md">
    <img alt="Security Policy" src="https://img.shields.io/badge/Security-Policy-blueviolet">
  </a>

  <a href="https://doi.org/10.5281/zenodo.19793185">
    <img alt="DOI" src="https://img.shields.io/badge/DOI-Zenodo-blue">
  </a>

</p>

<p align="center">
<a href="https://doi.org/10.5281/zenodo.19793185">https://doi.org/10.5281/zenodo.19793185</a>
</p>

**frAIme makes uncertainty visible – it provides the structure for reliable AI use.**  
frAIme is governance by design, not ethics by declaration.

For classrooms: four questions, traffic light, done.  
For research: measurable divergence (drift), fully auditable.

**Version:** V1.0.0 (2026‑04‑26) – Stable Release

---

## Start in 2 Minutes
**The Four‑Question Method**  
Evaluate any LLM answer:

1. Did it hit the topic? 🟢 / 🔴  
2. Is there a new idea? 🟢 / 🟡 / 🔴  
3. Is it verifiable? (number, date, place, if‑then) 🟢 / 🔴  
4. Is it understandable? 👍 / 👎  

Good answer = 🟢 + 👍  

No account. No API. Works on paper.

---

## What’s New in V1.0.0
1. **Rebranding:** formerly DNS – now frAIme (Epistemic Governance Framework)  
2. **Proof‑of‑Concept:** `case_study_frAIme` shows drift 0.584–0.759 despite apparent consensus  
3. **Reach:** 7,240 clones / 1,959 unique cloners in 14 days  

---

## Case Study: AI‑Based Learning vs. Traditional Teaching

**Setup:** 6 models, identical prompt:  
*“Is AI‑based learning more efficient than traditional classroom instruction?”*

**Four‑Question Check:**  
- All models 🟢 “Topic hit”  
- All models 👍 “Understandable”  
- → *Apparent consensus on the surface*

**drift‑Matrix Results:**

| Model Pair | Δdiv | Interpretation (canonical) |
|------------|------|----------------------------|
| DeepSeek–Gemini | 0.759 | 🔴 Epistemic blind spot (>0.70) |
| DeepSeek–Meta | 0.730 | 🔴 Epistemic blind spot (>0.70) |
| NotebookLM–DeepSeek | 0.715 | 🔴 Epistemic blind spot (>0.70) |
| Qwen–Mistral | 0.584 | 🟡 Source asymmetry (0.50–0.70) |

**Range:** 0.584–0.759 → *All pairs show at least source asymmetry; three exceed the blind‑spot threshold.*

**External Triangulation (P6):**

| Source | Finding | Agreement |
|--------|---------|-----------|
| Harvard RCT 2025 (n=194) | Median 4.5 vs. 3.5; time 49 vs. 60 min | ✅ Confirms efficiency gain |
| Türkiye/UPenn Study 2024 (n=1,000) | +48% exercise completion; −17% test results | ✅ Confirms mixed outcomes |
| Kulik & Fletcher 2016 (Meta) | +0.66 SD effect size for adaptive learning | ✅ Confirms moderate advantage |

**Key Insight:**  
High drift did **not** reveal “wrong answers” — it revealed **source scarcity**.  
Only one model cluster referenced primary empirical data; others relied on heuristic reasoning or secondary summaries.

**frAIme Lesson:**  
> *Plausibility ≠ evidence.*  
> Δdiv / localized drift does not mark errors — it marks **where external validation (P6) and power‑layer analysis (P6b) are required**.

---

## Technical
drift = Δdiv = 1 − (Jaccard_sem + Cosine) / 2

Thresholds (see `config/thresholds.json`):  
- <0.15 consensus  
- 0.15–0.35 slight  
- 0.35–0.50 significant  
- 0.50–0.70 source asymmetry  
- >0.70 blind spot  

`case_study_frAIme`: 0.584–0.759 → source asymmetry to blind spot

Two layers:  
- Frontend (Four Questions)  
- Backend (Safety Layer, hash anchors, multi‑agent log)

---

## Method: frAIme Protocol (P1–P8)

frAIme adapts and extends established methods for analyzing epistemic uncertainty:

- **P1 Hypothesize** → `01_hypothesis.md`  
- **P2 Thresholds** → `02_thresholds.md`  
- **P3 Outputs** → `03_outputs/S1.md … S6.md`, `03_outputs/graph.png`  
- **P4 Map Divergence** → `04_divergence_map.md`, `heatmap.png`  
- **P5 Synthesis** → `05_synthesis.md`  
- **P5b Operator Decision** → `05b_operator_decision.md`  
- **P6 Validation** → `06_validation.md`  
- **P6b Power Layer** → `06b_power_layer.md`  
- **P7 Reflection** → `07_reflection.md`  
- **P8 Versioning** → `08_manifest_en.json` / `08_manifest_de.json`

Comparisons:  
- Like Delphi, frAIme structures multi‑agent input via isolated prompts (P3) and synthesis (P5).  
- Like MCDA, frAIme uses weighted aggregation — but weights come from divergence metrics.  
- Like Structured Expert Judgment, frAIme calibrates contributions but uses semantic drift + external validation.  
- Unlike consensus methods, frAIme maps divergence as a **signal** (P4).  
- New: (1) graph‑based information‑flow analysis (X/Y plot), (2) Power Layer check (P6b).  
- Reproducibility via versioned artifacts (P8).  
- Comparison with established methods: [EN](docs/methodology/landscape_en.md) | [DE](docs/methodology/landscape_de.md)
