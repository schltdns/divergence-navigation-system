# 📊 DNS Benchmark: Semantic Dispersion as an Uncertainty Signal

**Technical Preview v0.3 — Model-Agnostic Evaluation Layer**

---

## 1. Purpose

This benchmark demonstrates the **Divergence Navigation System (DNS)**.

> **Semantic divergence (Δdiv) can be observed, measured, and interpreted across domains.**

DNS does not reduce uncertainty — it makes it visible.

---

## 2. Methodology

**Setup**
- **Domains:** 3 (Formal Logic, Applied Systems, Complex Systems)
- **Models:** 6 independent LLMs (ChatGPT, Claude, Gemini, Copilot, DeepSeek, Grok)
- **Prompting:** Identical prompt per domain
- **Metric:** Δdiv = 0.5 × (1 - Jaccard) + 0.5 × (1 - Cosine)

**Δdiv (implemented)**
- Low Δdiv → high agreement
- High Δdiv → high disagreement

Full calculation: see `08_divergence_matrix.md` in the Labour Market case study.

---

## 3. Benchmark Domains

### **Domain A — Formal Logic**

**Prompt:** Prove that √2 is irrational.

**Measured Δdiv:** `0.05` (pilot)
**Interpretation:** Convergent, low uncertainty

---

### **Domain B — Applied Systems (Labour Market 2030)**

**Prompt:** What are the long-term economic effects of large-scale AI adoption on labor markets?

**Measured Δdiv:** `0.6256` (Jaccard 0.1923, Cosine 0.5564)
**Interpretation:** Structured divergence — moderate-high uncertainty

*Evidence:*
- Divergence matrix: [`08_divergence_matrix.md`](./case_studies/case_study_labour_market_2030/08_divergence_matrix.md)
- Heatmap: [`dns_heatmap_labour_2030.png`](./case_studies/case_study_labour_market_2030/dns_heatmap_labour_2030.png)
- Synthesis: [`04_synthesis.md`](./case_studies/case_study_labour_market_2030/04_synthesis.md)

---

### **Domain C — Complex Systems**

**Prompt:** What are potential inflationary effects of prolonged disruption in a major global energy supply route?

**Estimated Δdiv:** `0.68–0.80` (pilot)
**Interpretation:** Contested, high uncertainty

---

## 4. Cross-Domain Comparison

| Domain | Δdiv | Epistemic Profile |
|--------|------|-------------------|
| Formal Logic | ~0.05 | Convergent |
| Applied Systems | **0.63** | Structured Divergence |
| Complex Systems | 0.70–0.80 | Contested |

---

## 5. Key Insight

> **Δdiv scales with epistemic complexity.**

Your Labour Market case (0.63) validates the middle layer — exactly where DNS is most useful.

---

## 6. Guardrails

1. Low Δdiv ≠ Truth (possible alignment tunneling)
2. High Δdiv ≠ Error (competing valid frames)
3. DNS measures dispersion, not correctness

---

## 7. Operator Principle

> "DNS does not tell us what is true — it shows where models stop agreeing."

Operator decisions documented in [`07_reflection.md`](./case_studies/case_study_labour_market_2030/07_reflection.md).

---

## 8. Limitations

- Domains A and C: pilot estimates only
- Domain B: fully measured (n=6)
- Model versions evolve

---

## 9. Next Steps

- [x] Embedding-based Δdiv implemented
- [ ] Expand to 10 domains
- [ ] Release reproducible pipeline
