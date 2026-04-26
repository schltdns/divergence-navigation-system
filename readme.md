<p align="center">
  <img src="04_archive_legacy/docs/assets/frAIme_logo_wordmark.png" alt="frAIme – Argumentation Drift Monitor" width="650"/>
</p>

<h1 align="center">frAIme</h1>

<p align="center">
  <strong>Argumentation Drift Monitor</strong>
</p>

<p align="center">
  🟢 Topic consistency &nbsp;&nbsp;•&nbsp;&nbsp;
  🟡 Idea emergence &nbsp;&nbsp;•&nbsp;&nbsp;
  🔴 Verifiability &nbsp;&nbsp;•&nbsp;&nbsp;
  🔵 Understandability
</p>

---

**frAIme makes uncertainty visible — it creates the frame for reliable AI use.**  
**frAIme is governance by design, not ethics by declaration.**

> For classrooms: four questions, traffic light, done.  
> For research: measurable divergence (Δdiv), auditable under EU AI Act.  
> For ODiKS: validated as the epistemic governance layer for open digital school infrastructures.

**Version:** V1.0.0 (2026-04-26) – *Stable release for ODiKS pilot*

---

## Start here — 2 minutes

### The Four Questions Method
Check every LLM answer:

1. **On topic?** 🟢 / 🔴
2. **New idea?** 🟢 / 🟡 / 🔴
3. **Verifiable?** (number, date, place, if‑then) 🟢 / 🔴
4. **Understandable?** 👍 / 👎

**Good answer = 🟢 + 👍**

No account. No API. Works on paper.

## 🚀 Live Demo

The interactive web app (frAIme V1.0.0 / DNS v2.2) is available at:  
👉 [https://divergence-navigation-system.streamlit.app](https://divergence-navigation-system.streamlit.app)

> Test the app with the built‑in examples (e.g., 'The Copilot Crash') or your own texts.

---

## What’s new in frAIme V1.0.0

**1. Rebranding & Strategic Positioning**
- Formerly known as **DNS (Divergence Navigation System)** – now **frAIme (Epistemic Governance Framework)**
- **ODIkS** (Open Digital Infrastructures for school authorities) becomes the primary validation case
- frAIme is **not limited to ODiKS** – it fits any AI governance pipeline

**2. Validated with the Copilot Crash (Full Protocol)**
- Single‑model narrative fails at Δdiv > 0.6
- Microsoft Copilot invented "West vs. China" – Δdiv = **0.742** across 7 models exposed it
- Three follow‑up questions increased divergence by 13% → narrative risk, not technical error

**3. Live Δdiv Tracking (Operationalized)**
- Frontend calculates Δtotal during conversation, not post‑hoc
- Thresholds validated: 0.3 = convergent, 0.5 = drift, 0.7 = contested

**4. Real‑world traction (unchanged)**
- 3,270 clones / 1,126 unique cloners in 14 days (GitHub)
- Used in MSB NRW pilot "KI‑Skilling.NRW"

---

## What frAIme is technically

**Core metric (inherited from DNS)**
$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

Validated ranges (frAIme V1.0.0):
- **<0.3** = convergence
- **0.3–0.5** = structured divergence (drift)
- **0.5–0.7** = high divergence (narrative risk)
- **>0.7** = contested (Copilot ↔ Mistral: 0.798)

**Two layers**
- **Frontend:** Four Questions + Live Traffic Light
- **Backend:** Safety Layer (JSON schema, hash anchors, SHAP, multi‑agent log, cross‑language integrity check)

---

## EU AI Act mapping

| Article | frAIme V1.0.0 Implementation |
| :--- | :--- |
| Art. 13 Transparency | Four Questions documented per answer |
| Art. 14 Human oversight | Operator justifies synthesis, Δdiv logged |
| Art. 15 Robustness | Δdiv + falsification rules + live tracking |

---

## Implementation Artifacts (V1.0.0)

- [4_questions.md](04_archive_legacy/teaching/4_questions.md) – The Four Questions Method
- [Case Study "The Copilot Crash" (bilingual)](03_pedagogy/) – bereits im aktiven Ordner (nicht archiviert)
- [Safety Layer Schema](04_archive_legacy/src/safety_layer_schema_v2.json)
- [minimal_safety_layer.py](01_governance/minimal_safety_layer.py) – with cross‑language check
- [calc_delta_div.py](04_archive_legacy/case_studies/case_study_the_copilot_crash/calc_delta_div.py)
- [Open Data Proof](04_archive_legacy/proof/dns_open_data_proof.json)
- [LICENSE-DOCS](LICENSE-DOCS) (CC BY-NC-SA 4.0)
- [LICENSE-CODE](LICENSE-CODE) (Apache-2.0)
---

## Links

- **Zenodo:** https://doi.org/10.5281/zenodo.19597808
- **GitHub:** https://github.com/schltdns/divergence-navigation-system (frAIme V1.0.0)
- **IPFS CID V1.0.0:** `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy` (same as DNS v2.2 for now)
- **ODIkS validation case:** [03_pedagogy/](03_pedagogy/) (bilingual case study)

---

## Quick start

1. Read the architecture: [docs/team_architecture.md](docs/team_architecture.md)
2. Try the crash: [case_studies/case_study_the_copilot_crash/readme.md](case_studies/case_study_the_copilot_crash/readme.md)
3. Run the demo: `python src/minimal_safety_layer.py`

**frAIme provides structure, not guarantees.**
