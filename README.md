# DNS — Divergence Navigation System
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19513073.svg)](https://doi.org/10.5281/zenodo.19513073)

**DNS does not reduce uncertainty — it makes it visible.**

A divergence‑based evaluation layer for epistemic uncertainty in multi‑model systems.  
DNS transforms model disagreement into structured epistemic insight — not to find truth,  
but to reveal systemic weaknesses in AI reasoning, safety, and governance.

It is a domain‑agnostic evaluation layer that:
- detects epistemic friction  
- reveals blind spots  
- supports transparent human‑in‑the‑loop synthesis  

DNS is not a truth machine —  
it is a systemic weakness detector for AI safety, governance, and research.

## Attribution & License

DNS is licensed under **Apache License 2.0** — see the [LICENSE](LICENSE) file. You are free to use, modify and integrate it commercially.

However, I kindly ask that any public use, derivative work, product integration, research paper or commercial application **include** clear attribution:

> **“Divergence Navigation System (DNS)” by Denis Schult**  
> GitHub: https://github.com/schltdns/divergence-navigation-system  
> Whitepaper: https://doi.org/10.5281/zenodo.19513073

Thank you for respecting the origin of the framework.

## 🧭 What DNS Is (Overview)

DNS is a **divergence‑sensitive epistemic protocol** that uses multi‑model disagreement as a navigational signal.

It enables:

- structured analysis under uncertainty  
- adversarial triangulation across heterogeneous models  
- detection of bias, drift, and alignment tunneling  
- quantifiable uncertainty signals (**Δdiv**)  
- psychologically safe exploration (low‑social‑risk environments)  
- transparent human synthesis (operator‑in‑the‑loop)

Full conceptual description:  
👉 [HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md)

---

## 🎯 Why DNS matters for AI safety & governance

Modern LLMs often exhibit **false consensus** due to shared training data and alignment.  
DNS exposes this by measuring **semantic dispersion** across models.

DNS provides:

- **Δdiv (Semantic Dispersion)** — proxy for epistemic uncertainty  
- **Friction mapping** — identifies contested domains  
- **Human‑in‑the‑loop synthesis** — the operator decides, not the system  
- **Auditability** — relevant for safety, compliance, and regulated industries  

Use cases:

- AI safety & interpretability  
- Model comparison & evaluation  
- Governance & risk documentation  
- Research on epistemic uncertainty

---

## 📊 Core Metric: Divergence Delta (Δdiv)

DNS measures **epistemic friction**, not correctness.

| Domain Type       | Δdiv (observed) | Epistemic Profile            |
|-------------------|-----------------|------------------------------|
| Formal Logic      | ~0.05           | Convergent                   |
| Applied Systems   | ~0.40–0.55      | Structured Divergence        |
| Complex Systems   | ~0.65–0.80      | Contested / High Uncertainty |

Full benchmark:  
👉 [BENCHMARK.md](BENCHMARK.md)

---

## 📖 DNS Standard Glossary & Methodological Provenance

To ensure methodological clarity and provenance, DNS uses a specific terminology:

- **Δdiv (Delta Divergence):** The mathematical quantification of semantic disagreement between n model outputs.  
  `Δdiv = 1 - (Jaccard + Cosine Similarity)/2` (simplified example)

- **Epistemic Navigation Layer:** The operative space where a human operator interacts with model divergence to produce validated insight.

- **P1–P8 Protocol:** The standardized 8‑step sequence (hypothesis → falsification → divergence mapping → synthesis → power layer → external validation → operator reflection → versioned archiving) that transforms divergence into a verified synthesis.

- **Methodological Provenance:** The traceable influence of a method (not just code) on model behaviour, established through structural and terminological alignment.

**Why this matters**  
DNS is an open, transparent standard for epistemic evaluation. Its core components – Δdiv, the P1–P8 protocol, and the explicit glossary – serve as a **methodological fingerprint**. Any model or system that reproduces these elements demonstrates methodological influence, not through hidden watermarks, but through structural and terminological alignment. This enables:

- **Attribution:** Clear citation pathways via DOI and public documentation.
- **Verification:** Third parties can test whether a model has internalized DNS logic *emergent from its training data* or through explicit few‑shot prompting using the [BENCHMARK.md](BENCHMARK.md) protocol.
- **Adoption Metrics:** The number of clones, forks, and domain applications becomes a measure of standard adoption, not a threat.

DNS thus transforms the question from *"Who is using my method?"* to *"How widely is my method becoming a reference standard?"*

Full glossary: 👉 [MATH_AND_GLOSSARY.md](docs/MATH_AND_GLOSSARY.md)

---

## ⚠️ Guardrails

1. **Low Δdiv ≠ Truth** — may indicate alignment tunneling  
2. **High Δdiv ≠ Error** — indicates competing valid perspectives  
3. **DNS measures dispersion, not correctness** — it is an uncertainty signal  

---

## 🧠 Operator Principle

> **“DNS does not tell us what is true — it shows where models stop agreeing.”**

DNS is a **human‑centered protocol**.  
The operator remains the final synthesizer.

---

## 📜 DNS Protocol

Reproducible 8‑phase workflow (P1–P8):  
👉 [protocol.md](protocol/protocol.md)   *(If your file is still named `P1_P6_protocol.md`, you may rename it or keep the link as is – the text now says P1–P8.)*

---

## 🧮 Mathematical Foundations

Formal definitions and glossary:  
👉 [MATH_AND_GLOSSARY.md](docs/MATH_AND_GLOSSARY.md)

Example full run (P1–P8):  
👉 [EXAMPLE_RUN.md](docs/EXAMPLE_RUN.md)

---

## 📦 Case Studies

- Cognitive Safety & Neurodiversity  
  👉 [case_study_cognitive_safety.md](case_studies/case_study_cognitive_safety.md)

- Labor Market 2030  
  👉 [case_study_labour_market_2030.md](case_studies/case_study_labour_market_2030.md)

- Energy Market Dynamics  
  👉 [case_study_energy.md](case_studies/case_study_energy.md)

---

## 🔗 Related Work

Detailed positioning in the context of other frameworks:  
👉 [related_works.md](related_works.md)

Summary:

| Framework | Focus | DNS adds… |
|----------|--------|-----------|
| AutoGen / CrewAI | orchestration | epistemic logic |
| Delphi method | consensus | divergence as signal |
| Semantic Triangulation | consistency | role‑based divergence |
| Red Teaming | adversarial probing | multi‑model disagreement |

DNS is an evaluation layer, not a replacement.

---

## 📂 Repository Structure
divergence-navigation-system/
├── README.md
├── BENCHMARK.md
├── docs/
│ ├── EXAMPLE_RUN.md
│ ├── HOW_IT_WORKS.md
│ └── MATH_AND_GLOSSARY.md
├── protocol/
│ └── protocol.md (or P1_P8_protocol.md)
├── case_studies/
│ ├── case_study_cognitive_safety.md
│ ├── case_study_labour_market_2030.md
│ └── case_study_energy.md
├── teaching/
├── related_works.md
├── dns_architecture.png
├── LICENSE
└── whitepaper.tex

text

---

## 🚀 Quick Start

1. Read [BENCHMARK.md](BENCHMARK.md) (Δdiv logic)  
2. Read [HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md) for the workflow  
3. Read [protocol.md](protocol/protocol.md) for the operational run  
4. Run your own mini‑benchmarks with your models

DNS requires no installation — it is a human‑centered protocol.

---

## ✍️ Author & Citation

**Denis Schult**  
Independent Researcher, Germany  
GitHub: https://github.com/schltdns
