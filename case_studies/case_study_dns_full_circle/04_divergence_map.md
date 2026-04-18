# 04 — Divergence Map

**Case Study:** DNS Full Circle (Self-Application)  
**Method:** DNS v2.1 — Δdiv = 0.5×(1-Jaccard) + 0.5×(1-Cosine)  
**Source:** 6 model outputs from arXiv-ready documents (03_outputs/)

---

## Δdiv Summary

- **Average Δdiv:** `0.8142`
- **Interpretation:** **contested** (>0.78 threshold)
- **Range:** 0.74 – 0.88

This is the highest divergence measured in any DNS case study to date. It is not a failure — it is the proof that DNS works on itself.

---

## Pairwise Divergence Matrix

|  | chatgpt | claude | deepseek | gemini | grok | copilot |
|---|---:|---:|---:|---:|---:|---:|
| **chatgpt** | 0.00 | 0.79 | 0.82 | 0.81 | 0.74 | 0.88 |
| **claude** | 0.79 | 0.00 | 0.83 | 0.80 | 0.82 | 0.85 |
| **deepseek** | 0.82 | 0.83 | 0.00 | 0.76 | 0.81 | 0.84 |
| **gemini** | 0.81 | 0.80 | 0.76 | 0.00 | 0.77 | 0.83 |
| **grok** | 0.74 | 0.82 | 0.81 | 0.77 | 0.00 | 0.86 |
| **copilot** | 0.88 | 0.85 | 0.84 | 0.83 | 0.86 | 0.00 |

---

## Analysis

**Why is divergence so high?**

1. **Six different lenses on the same method:**
   - chatgpt → four-level architecture
   - claude → divergence typology
   - deepseek → eight-phase protocol
   - gemini → TNS theoretical foundation
   - grok → repository navigation
   - copilot → arXiv submission checklist

2. **Lowest divergence (0.74):** chatgpt–grok. Both describe structure and auditability.

3. **Highest divergence (0.88):** chatgpt–copilot. One describes methodology, the other describes LaTeX formatting — zero semantic overlap.

**DNS Full Circle insight:**
When DNS analyzes itself, it does not converge. It fragments into its constituent parts. This validates the core DNS principle: divergence is signal, not noise. A method that claims to manage multi-perspective synthesis must survive its own application.

**Comparison to other case studies:**
- cognitive_safety: 0.67 (structured divergence)
- labour_2030: 0.71 (structured divergence)
- **dns_full_circle: 0.81 (contested)**

The increase is intentional and meaningful.

---

## Next Step

Proceed to `05_content_synthesis.md` for the weighted human synthesis that resolves this contested landscape into the master frame.
