# 📊 DNS Benchmark: Semantic Dispersion as an Uncertainty Signal

**v0.3 — Model-Agnostic Evaluation Layer**

---

## 1. Purpose

> **Semantic divergence (Δdiv) can be observed, measured, and interpreted across domains.**

DNS does not reduce uncertainty — it makes it visible.

---

## 2. Methodology

- **Models:** 6 (ChatGPT, Claude, Gemini, Copilot, DeepSeek, Grok)
- **Metric:** Δdiv = 0.5×(1-Jaccard) + 0.5×(1-Cosine)
- **Implementation:** embedding-based

Reference: [`08_divergence_matrix.md`](./case_studies/case_study_labour_market_2030/08_divergence_matrix.md)

---

## 3. Results

### Domain A — Formal Logic
**Prompt:** Prove √2 is irrational  
**Δdiv:** 0.05 — Convergent

### Domain B — Applied Systems (Labour Market 2030)
**Prompt:** Long-term economic effects of AI on labor markets  
**Δdiv:** **0.6256** (Jaccard 0.1923, Cosine 0.5564)  
**Status:** Structured Divergence  
**Files:** [matrix](./case_studies/case_study_labour_market_2030/08_divergence_matrix.md) · [heatmap](./case_studies/case_study_labour_market_2030/dns_heatmap_labour_2030.png) · [synthesis](./case_studies/case_study_labour_market_2030/04_synthesis.md)

### Domain C — Complex Systems
**Prompt:** Inflationary effects of energy supply disruption  
**Δdiv:** 0.70–0.80 (pilot) — Contested

---

## 4. Comparison

| Domain | Δdiv | Profile |
|--------|------|---------|
| Formal Logic | 0.05 | Convergent |
| Applied Systems | **0.63** | Structured Divergence |
| Complex Systems | 0.75 | Contested |

---

## 5. Insight

**Δdiv scales with epistemic complexity.** The measured 0.63 validates DNS in the productive middle.

---

## 6. Guardrails

1. Low Δdiv ≠ Truth
2. High Δdiv ≠ Error
3. DNS measures dispersion, not correctness

---

## 7. Operator Principle

> "DNS shows where models stop agreeing." — see [`07_reflection.md`](./case_studies/case_study_labour_market_2030/07_reflection.md)
