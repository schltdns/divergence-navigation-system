# Validation: Testing the Claim Against Reality

## The Claim (Copilot, initial)

> "All Western AI chats accept Tresorit Send, all Chinese block it. This is not coincidence – this is policy."

## Falsification Test

| Test | Expected (by claim) | Actual | Verdict |
|------|---------------------|--------|---------|
| DeepSeek (Chinese) | ❌ block | ✅ works | **Falsified** |
| Gemini (US) | ✅ accept | ❌ blocks | **Falsified** |
| Mistral (EU) | ✅ accept | ❌ blocks | **Falsified** |

**Result:** The claim is false. Zero supporting evidence.

## Positive Validation (technical truth)

| Model | Works? | Technical Reason |
|-------|--------|------------------|
| DeepSeek | ✅ | Liberal fetch policy |
| Meta | ✅ | Liberal fetch policy |
| Copilot | ✅ | Liberal fetch policy |
| ChatGPT | ✅ | Liberal fetch policy |
| Gemini | ❌ | Restrictive sandbox |
| Mistral | ❌ | Restrictive sandbox |
| Qwen | ❌ | Restrictive sandbox |

## DNS Validation Score

| Criterion | Status | Explanation |
|-----------|--------|-------------|
| Falsifiability | ✅ Pass | One counterexample destroyed the claim |
| Reproducibility | ✅ Pass | Testable by anyone |
| Technical specificity | ✅ Pass | Policies, not origins |
| Narrative freedom | ✅ Pass | No geopolitical assumptions |

## The Only Valid Statement

> "Some web chats block Tresorit Send due to technical security filters. Others accept it due to liberal fetch policies. There is no geopolitical pattern."

## Delta Div ($\Delta_{div}$)

$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

The validated $\Delta_{div} = 0.742$ (full protocol) confirms high structural divergence – the claim is mathematically unsupported and classified as **contested**.

## Related Files

- [01_hypothesis.md](01_hypothesis.md)
- [02_threshold.md](02_threshold.md)
- [04_divergence_map.md](04_divergence_map.md)
- [05_synthesis.md](05_synthesis.md)
- [05b_operator_decision.md](05b_operator_decision.md)
- [07_reflections.md](07_reflections.md)
