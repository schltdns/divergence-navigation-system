# DNS Divergence-based Navigation System
graph TD
    User((Mensch / Operator)) -- P5 Synthese --> Master[Divergence-based Navigation System]
    
    subgraph "Analytischer Kern (S1-S3)"
        DS[DeepSeek: Falsifikator]
        GK[Grok: Signal-Agent]
        CL[Claude: Grenzmarkierer]
    end
    
    subgraph "Synthese & Struktur"
        GPT[ChatGPT: System-Architekt]
        GEM[Gemini: Strategie-Erotik/Vision]
        CP[Copilot: Quellen-Matrix]
    end
    
    DS -.-> Master
    GK -.-> Master
    CL -.-> Master
    GPT -.-> Master
    GEM -.-> Master
    CP -.-> Master

    style User fill:#f9f,stroke:#333,stroke-width:4px
    style Master fill:#bbf,stroke:#333,stroke-width:2px

**A structured, falsifiable, multi‑model analysis method for complex uncertainty.**

> *“This repository does not show what AI says – it reveals where and why AI models disagree, and how reasoned decisions are derived from that divergence.”*

---

## What is TNS?

TNS is a hybrid method combining:
- **Classical triangulation** (Denzin 1978; Patton 1999)
- **Constructivist didactics** (Reich 2008)
- **Critical rationalism** (Popper)
- **Multi‑model AI divergence** as an epistemic resource

It uses divergent LLMs as “resonating bodies” to surface blind spots, biases, and causal disagreements – then synthesises them into falsifiable, transparent, and critique‑ready conclusions.

---

## Repository Structure
tns/
├── protocol/ # Operational guide for TNS phases (P1–P8)
├── related works/ # Academic references (Denzin, Patton, Reich, etc.)
├── case_study_energy/ # First case: European gas market dynamics
├── case_study_labour_market_2030/ # Second case: AI & skills shortage (full TNS cycle)
├── teaching/ # 90‑minute workshop for IHK / vocational schools
├── whitepaper.tex # Draft whitepaper on multi‑agent orchestration
├── Schult_2026_Triangulation_Protocol_v1_2.pdf # Formal protocol description
├── CHANGELOG.md # Version history
├── LICENSE # CC BY‑NC 4.0
└── README.md # This file

text

---

## Key Case Study: Labour Market 2030

**Question:** How will AI automation transform the German labour market by 2030, given a persistent skills shortage?

**Method:** Six models (ChatGPT, Claude, DeepSeek, Gemini, Grok, Copilot) – identical prompts – divergence extraction – external validation (IAB, WEF, IW, McKinsey, BAuA) – operator synthesis.

**Core findings (consensus):**
- Job change > job loss; 20–40% of tasks transformed
- Productivity potential 0.3–1.2% p.a. – conditional on adaptation
- Skill shift inevitable: routine analysis ↓, problem solving & AI literacy ↑
- Dual training is an advantage **if modernised quickly**
- Real risks: inequality, regional divergence, age (50+), mental health

**Open questions (divergences):** Speed of automation, regulation as brake vs. protection, social mobility trend.

**Falsification matrix:** Testable criteria with thresholds (e.g., productivity <0.1% by 2028 would falsify the optimistic productivity thesis).

**Power layer:** Added as fourth filter – who controls AI, who has access, who profits, who bears risks.

📁 **[Go to case study](case_study_labour_market_2030/)**

---

## How to Use This Repository

- **For researchers:** Replicate the TNS protocol with your own models or updated data. Compare divergence patterns.
- **For practitioners (IHK, vocational schools):** Use the `teaching/` workshop to introduce the three filters and power layer.
- **For method developers:** Build upon the divergence types, falsification matrix, and operator reflection.

---

## License

**CC BY‑NC 4.0** – Attribution required, non‑commercial. You are free to share and adapt, but not for commercial purposes.

---

## Citation

Schult, D. (2026). *Triangulation nach Schult (TNS): A multi‑model divergence analysis method*. GitHub. [https://github.com/schltdns/tns](https://github.com/schltdns/tns)

---

## Version

**Current release: v1.2-Open** (see [CHANGELOG](CHANGELOG.md))

---

## Contact & Contributing

Issues and pull requests welcome. For questions, open an issue or contact the maintainer.
2. CITATION.cff (for GitHub’s citation feature)
yaml
cff-version: 1.2.0
message: "If you use this method or case studies in your work, please cite as follows."
title: "Triangulation nach Schult (TNS): A multi‑model divergence analysis method"
version: 1.2-Open
date-released: 2026-04-06
authors:
  - family-names: "Schult"
    given-names: "Denis"
    orcid: "https://orcid.org/..." # optional
repository-code: "https://github.com/schltdns/tns"
license: "CC-BY-NC-4.0"
keywords:
  - triangulation
  - AI
  - divergence
  - labour market
  - methodology
type: software
3. Release Notes (for GitHub Releases)
markdown
# Release v1.2-Open – Labour Market 2030 Case Study

## What’s new

- **Full case study: Labour Market 2030** (AI automation & skills shortage)
  - Raw outputs from 6 models (ChatGPT, Claude, DeepSeek, Gemini, Grok, Copilot)
  - Divergence matrix with 4 types (substantive, normative, didactic, architectural)
  - Master Frame 3.3 (tasks, 3 filters, power layer, master question)
  - Falsification matrix with testable criteria (e.g., productivity <0.1% by 2028)
  - External validation (IAB, WEF, IW, McKinsey, BAuA)
  - Operator reflection (bias self‑assessment, falsification of operator decisions)

- **Power layer** introduced as fourth, meta‑filter (access, control, profit, risk)

- **Teaching module** (90‑minute workshop) for IHK / vocational schools

- **CHANGELOG.md** for version tracking

- **CITATION.cff** for easy referencing

## Changed

- Main README restructured with golden sentence and clearer navigation

## Fixed

- Divergence now explicitly treated as primary signal (not consensus‑first)

## How to use

- Browse `case_study_labour_market_2030/` for the full analysis
- Run the workshop from `teaching/`
- Cite using `CITATION.cff`

**Next planned:** Update falsification matrix with 2027/2028 data when available.
