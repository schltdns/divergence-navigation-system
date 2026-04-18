# 04_divergence_map.md – Divergence Map: Cognitive Safety Hypothesis

**Run:** dns_v2.1_cognitive_safety  
**Date:** 2026-04-18  

## Overview

All six models confirm the core hypothesis. Divergence occurs in **framing, emphasis, and operational details**, not in the fundamental mechanism.

## Divergence Types

### 1. Substantive Divergence (factual disagreements)

| Issue | Model A | Model B | Resolution |
|-------|---------|---------|------------|
| **Immunisation risk** | ChatGPT: "DNS scheitert nicht" is non-falsifiable | DeepSeek, Gemini, Grok: Statement is acceptable as tool property | Operator decided to keep statement but add caveat (see [05b_operator_decision.md](./05b_operator_decision.md)) |
| **Operator failure vs. design failure** | ChatGPT: Design can amplify/dampen operator failure | Others: Failure is exclusively operator error | Synthesised as: "DNS is robust; primary failure mode is operator, but design matters" |

### 2. Normative Divergence (value-based differences)

| Issue | Model A | Model B | Type |
|-------|---------|---------|------|
| **Universality** | ChatGPT: Not universal | Gemini: Broadly applicable | Risk tolerance |
| **Neurodivergence as origin** | Claude: Origin is geopolitics, son is application | Grok: Son is emotionally central | Emphasis |
| **Target group definition** | DeepSeek: "People with high evaluation anxiety" | Gemini: "Neurodivergent and introverted" | Scope |

### 3. Architectural Divergence (bias due to training)

- **ChatGPT** → reviewer mode, precision-focused  
- **Claude** → philosophical, depth-oriented  
- **DeepSeek** → falsification, strictness  
- **Gemini** → visionary, manifesto-like  
- **Grok** → direct, unvarnished  
- **Copilot** → synthesising, bridging  

No resolution needed – these are documented as epistemic diversity.

## Divergence Matrix

| Dimension | ChatGPT | Claude | DeepSeek | Gemini | Grok | Copilot | Consensus |
|-----------|---------|--------|----------|--------|------|---------|-----------|
| Core mechanism confirmed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **High** |
| Social decoupling works | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **High** |
| Neurodivergence relevance | ✅ (conditional) | ✅ | ✅ | ✅ | ✅ | ✅ | **High** |
| Universal applicability | ⚠️ (limited) | ✅ | ⚠️ | ✅ | ✅ | ✅ | **Medium** |
| Operator failure only | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | **Medium** |
| Empirical proof needed | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **High** |

## Δdiv Calculation (based on actual model outputs)

**Measured Δdiv (average over all model pairs):** `0.787`

**Divergence matrix (Δdiv for each pair):**

|         | chatgpt | claude | copilot | deepseek | gemini | grok |
|---------|---------|--------|---------|----------|--------|------|
| chatgpt | 0.0000  | 0.8068 | 0.7808  | 0.7536   | 0.7380 | 0.8274 |
| claude  | 0.8068  | 0.0000 | 0.8914  | 0.8079   | 0.7683 | 0.7850 |
| copilot | 0.7808  | 0.8914 | 0.0000  | 0.5716   | 0.8561 | 0.8570 |
| deepseek| 0.7536  | 0.8079 | 0.5716  | 0.0000   | 0.7638 | 0.8184 |
| gemini  | 0.7380  | 0.7683 | 0.8561  | 0.7638   | 0.0000 | 0.7803 |
| grok    | 0.8274  | 0.7850 | 0.8570  | 0.8184   | 0.7803 | 0.0000 |

**Interpretation:**  
Δdiv > 0.6 indicates **high structural divergence**. However, this divergence is primarily due to differences in **response length, detail level, terminology, and formatting** – not due to disagreement on the core hypothesis. All models verbally confirmed the hypothesis. This demonstrates that DNS captures formal/stylistic divergence as a signal, which is a feature, not a bug.

**Lowest pairwise divergence:** Copilot vs. DeepSeek (0.5716) – these two models share the most similar response structure.

## Implications for Synthesis

- Despite high Δdiv, a **consensus synthesis** is possible because the *content* agrees (see [05_synthesis.md](./05_synthesis.md)).
- The operator must explicitly note that the high divergence is structural, not substantive.
- Contradictions documented in the divergence matrix are resolved in [05b_operator_decision.md](./05b_operator_decision.md).

---

**Next:** [05_synthesis.md](./05_synthesis.md)
