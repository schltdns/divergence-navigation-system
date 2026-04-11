# DNS — Divergence Navigation System

**A divergence‑based evaluation layer for epistemic uncertainty in multi‑model systems.**

> **DNS does not reduce uncertainty — it makes it visible.**

DNS transforms **model disagreement** into **structured epistemic insight**.  
It is a domain‑agnostic evaluation layer that detects friction, reveals blind spots,  
and supports transparent human‑in‑the‑loop synthesis.

DNS is not a truth machine — it is a **systemic weakness detector** for AI safety, governance, and research.

---

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

Reproducible workflow (Hypothese → Triangulation → Divergenz‑Mapping → Synthese → Validierung → Reflexion → Versionierung):  
👉 [protocol.md](protocol/protocol.md)


---

## 🧮 Mathematical Foundations

Formal definitions and glossary:  
👉 [MATH_AND_GLOSSARY.md](docs/MATH_AND_GLOSSARY.md)

Beispielhafter vollständiger Lauf (P1–P6):  
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

Ausführliche Einordnung im Kontext anderer Frameworks:  
👉 [related_works.md](related_works.md)

Kurzfassung:

| Framework | Focus | DNS adds… |
|----------|--------|-----------|
| AutoGen / CrewAI | orchestration | epistemic logic |
| Delphi method | consensus | divergence as signal |
| Semantic Triangulation | consistency | role‑based divergence |
| Red Teaming | adversarial probing | multi‑model disagreement |

DNS ist ein **Evaluation Layer**, kein Ersatz.

---

## 📂 Repository Structure

divergence-navigation-system/
├── README.md
├── BENCHMARK.md
├── docs/
│   ├── EXAMPLE_RUN.md
│   ├── HOW_IT_WORKS.md
│   └── MATH_AND_GLOSSARY.md
├── protocol/
│   └── P1_P6_protocol.md
├── case_studies/
│   ├── case_study_cognitive_safety.md
│   ├── case_study_labour_market_2030.md
│   └── case_study_energy.md
├── teaching/
├── related_works.md
├── dns_architecture.png
├── LICENSE
└── whitepaper.tex

Code

---

## 🚀 Quick Start

1. [BENCHMARK.md](BENCHMARK.md) lesen (Δdiv‑Logik)  
2. [HOW_IT_WORKS.md](docs/HOW_IT_WORKS.md) für den Ablauf  
3. [P1_P6_protocol.md](protocol/P1_P6_protocol.md) für den operativen Run  
4. Eigene Mini‑Benchmarks mit deinen Modellen fahren

DNS erfordert **keine Installation** — es ist ein human‑centered Protocol.

---

## ⚖️ License

**Apache‑2.0** — siehe [LICENSE](LICENSE).

---

## ✍️ Author & Citation

**Denis Schult**  
Independent Researcher, Germany  
GitHub: https://github.com/schltdns

> Schult, D. (2026). *DNS — Divergence Navigation System: A divergence‑based evaluation layer for epistemic uncertainty in multi‑model systems.*  
> GitHub: https://github.com/schltdns/divergence-navigation-system
