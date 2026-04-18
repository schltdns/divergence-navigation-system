# 📊 DNS Benchmark: Semantic Dispersion as an Uncertainty Signal

**v0.4 — Model-Agnostic Evaluation Layer**

---

## 1. Purpose

> **Semantic divergence ($\Delta_{div}$) can be observed, measured, and interpreted across domains.**

DNS does not reduce uncertainty — it makes it visible.

---

## 2. Methodology

- **Models:** 6 (ChatGPT, Claude, Gemini, Copilot, DeepSeek, Grok)
- **Metric:** $\Delta_{div} = 0.5 \times (1-\text{Jaccard}) + 0.5 \times (1-\text{Cosine})$
- **Implementation:** embedding-based

---

## 3. Results

### Domain A — Formal Logic
**Prompt:** Prove √2 is irrational  
**$\Delta_{div}$:** 0.05 — Convergent  
**Interpretation:** Mathematical proof produces near-identical outputs

### Domain B — Applied Systems (Labour Market 2030)
**Prompt:** Long-term economic effects of AI on labor markets  
**$\Delta_{div}$:** **0.6256** (Jaccard 0.1923, Cosine 0.5564)  
**Status:** Structured Divergence  
**Files:** [matrix](case_studies/case_study_labour_market_2030/08_divergence_matrix.md) · [heatmap](case_studies/case_study_labour_market_2030/dns_heatmap_labour_2030.png) · [synthesis](case_studies/case_study_labour_market_2030/04_synthesis.md)

### Domain C — Cognitive Safety
**Prompt:** Does DNS create cognitive safety for neurodivergent users?  
**$\Delta_{div}$:** **0.787**  
**Status:** Contested Divergence  
**Files:** [synthesis](case_studies/case_study_cognitive_safety/05_synthesis.md) · [divergence map](case_studies/case_study_cognitive_safety/04_divergence_map.md)

### Domain D — Meta-Methodology (DNS Full Circle)
**Prompt:** Describe DNS when applied to itself  
**$\Delta_{div}$:** **0.8142**  
**Status:** Contested Divergence  
**Files:** [synthesis](case_studies/dns_full_circle/05_synthesis.md) · [divergence map](case_studies/dns_full_circle/04_divergence_map.md)


---

## 4. Comparison

| Domain | $\Delta_{div}$ | Profile |
|--------|---------------|---------|
| Formal Logic | 0.05 | Convergent |
| Labour Market 2030 | **0.6256** | Structured Divergence |
| Cognitive Safety | **0.787** | Contested |
| DNS Full Circle | **0.8142** | Contested |

---

## 5. Insight

**$\Delta_{div}$ scales with epistemic complexity and reflexivity.**

- 0.05–0.35: Convergent domains (math, facts)
- 0.56–0.77: Structured divergence (applied systems) — Labour 2030 validates this band
- 0.78–0.90: Contested divergence (human factors, self-reference) — Cognitive Safety and Full Circle confirm

The progression from 0.6256 → 0.787 → 0.8142 demonstrates that DNS measures increasing interpretive depth, not error.

---

## 6. Guardrails

1. Low $\Delta_{div}$ ≠ Truth
2. High $\Delta_{div}$ ≠ Error  
3. DNS measures dispersion, not correctness

---

## 7. Operator Principle

> "DNS shows where models stop agreeing." — see [07_reflection.md](case_studies/case_study_labour_market_2030/07_reflection.md)
