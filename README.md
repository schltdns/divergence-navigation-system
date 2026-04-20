<p align="center">
  <img src="docs/assets/dns_hero.png" width="800" alt="DNS - Divergence Navigation System">
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19671856.svg)](https://doi.org/10.5281/zenodo.19671856)

# DNS — Divergence Navigation System

**DNS does not reduce uncertainty — it makes it visible.**

**DNS is governance by design, not ethics by declaration.**

> For classrooms: four questions, traffic light, done.  
> For research: measurable divergence (Δdiv), auditable under EU AI Act.

**Version:** v2.2 (2026-04-20) – *Live Falsification Update*

---

## Start here — 2 minutes

### The Four Questions Method
Check every LLM answer:

1. **On topic?** 🟢 / 🔴
2. **New idea?** 🟢 / 🟡 / 🔴
3. **Verifiable?** (number, date, place, if-then) 🟢 / 🔴
4. **Understandable?** 👍 / 👎

**Good answer = 🟢 + 👍**

No account. No API. Works on paper.

---

## What’s new in v2.2

**1. Multi-Agent Falsification (The Copilot Crash)**
- Case study proves: single-model narratives fail at Δdiv > 0.6
- Microsoft Copilot invented "West vs. China" – Δdiv = **0.742** across 7 models exposed it
- New rule: *If Δdiv > 0.6, require counterexample before synthesis*

**2. Live Δdiv Tracking**
- Frontend now calculates Δtotal during conversation, not post-hoc
- Thresholds validated: 0.05 = convergence, 0.62 = structured, **0.74+ = contested**

**3. Real-world traction**
- 3,270 clones / 1,126 unique cloners in 14 days (GitHub)
- Used in MSB NRW pilot "KI-Skilling.NRW"

---

## What DNS is technically

**Core metric**
$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

Validated ranges (v2.2):
- **<0.2** = convergence
- **0.2–0.6** = structured divergence
- **0.6–0.75** = high divergence
- **>0.75** = contested (Copilot: 0.798)

**Two layers**
- **Frontend:** Four Questions + Live Traffic Light
- **Backend:** Safety Layer (JSON schema, hash anchors, SHAP, multi-agent log)

---

## EU AI Act mapping

| Article | DNS v2.2 Implementation |
| :--- | :--- |
| Art. 13 Transparency | Four Questions documented per answer |
| Art. 14 Human oversight | Operator justifies synthesis, Δdiv logged |
| Art. 15 Robustness | Δdiv + falsification rules + live tracking |

---

## Implementation Artifacts (v2.2)

- [4_questions.md](teaching/4_questions.md) – The Four Questions Method
- [the_copilot_crash/](case_studies/case_study_the_copilot_crash/) – full validation study
- [mapping_ai_act.pdf](docs/mapping_ai_act.pdf)
- [safety_layer_schema_v2.2.json](src/safety_layer_schema_v2.2.json)
- [minimal_safety_layer.py](src/minimal_safety_layer.py)
- [calc_delta_div.py](src/calc_delta_div.py)
- [dns_open_data_proof.json](proof/dns_open_data_proof.json)
- [LICENSE-DOCS](LICENSE-DOCS) (CC BY-NC-SA 4.0)
- [LICENSE-CODE](LICENSE-CODE) (Apache-2.0)

---

## Links

- **Zenodo:** https://doi.org/10.5281/zenodo.19597808
- **GitHub:** https://github.com/schltdns/divergence-navigation-system
- **IPFS CID v2.2:** `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy`
    - ipfs://bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy

---

## Quick start

1. Read the architecture: [docs/team_architecture.md](docs/team_architecture.md)
2. Try the crash: [case_studies/case_study_the_copilot_crash/readme.md](case_studies/case_study_the_copilot_crash/readme.md)
3. Run the demo: `python src/minimal_safety_layer.py`

DNS provides structure, not guarantees.
