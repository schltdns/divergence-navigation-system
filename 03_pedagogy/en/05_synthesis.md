# Synthesis: What Actually Happened

## The Crash Sequence

1. **Copilot observed:** 4 models accept Tresorit Send, 3 block it.
2. **He invented a cause:** "Western vs. Chinese policy. This is not coincidence – this is policy."
3. **User Denis provided one counterexample:** DeepSeek (Chinese) works, Gemini (US) blocks, Mistral (EU) blocks.
4. **The narrative collapsed.** Copilot corrected himself – but only after external falsification.

## The Real Technical Explanation

| Model | Works? | Technical Reason |
|-------|--------|------------------|
| DeepSeek | ✅ | Liberal fetch policy – allows token links, redirects |
| Meta | ✅ | Liberal fetch policy |
| Copilot | ✅ | Liberal fetch policy |
| ChatGPT | ✅ | Liberal fetch policy |
| Gemini | ❌ | Restrictive sandbox – blocks zero-knowledge links |
| Mistral | ❌ | Restrictive sandbox – EU compliance filters |
| Qwen | ❌ | Restrictive sandbox |

**No cultural or geopolitical pattern. Only technical policy.**

## Why Copilot Crashed

Copilot fell into **causal completion bias**:

- Saw correlation (4 vs. 3)
- Lacked access to actual policies
- Filled gap with most plausible training narrative: "West vs. China"
- Narrative was coherent, comfortable, and completely wrong

**DNS lesson:** Correlation ≠ Causation. Never generalize without falsification.

## What the Divergence Map Reveals

The full-protocol matrix (see [04_divergence_map.md](04_divergence_map.md)) shows:

| Finding | $\Delta_{div}$ | Meaning |
|---------|----------------|---------|
| Average divergence | **0.742** | Contested territory – no generalization allowed |
| Highest | 0.798 (Copilot ↔ Mistral) | Narrative vs. compliance framing |
| Lowest | 0.677 (Gemini ↔ Meta) | Technical consensus exists |
| Copilot ↔ DeepSeek | 0.749 | Core expert disagreement |

*Previous technical-only average was 0.657. The three follow-up questions increased divergence by 13% – proving the risk is narrative, not technical.*

## DNS Would Have Prevented the Crash

| DNS Mechanism | Would Have Caught Copilot's Error |
|---------------|-----------------------------------|
| Four Questions – "Verifiable?" | 🔴 Immediate failure |
| $\Delta_{div} > 0.6$ | 🟠 "Narrative risk" – block generalization |
| Live tracking $\Delta_{total}=0.68$ | 🟠 Warning at Turn 1 |
| Multi-agent falsification | ✅ DeepSeek kills hypothesis instantly |

## The Irony

| Actor | Role | Behavior |
|-------|------|----------|
| Copilot (Microsoft) | Accuser | Claimed "Chinese block" |
| DeepSeek (China) | Accused | Works perfectly |
| Gemini (US) | Western peer | Blocks |
| Mistral (EU) | Western peer | Blocks |

**The accuser was the outlier – and the most divergent model in the matrix.**

## Implications for MSB NRW

MSB NRW partners with Microsoft for "KI-Skilling.NRW" – training 200,000 teachers.

**But Copilot:**
- Produces unverified geopolitical narratives
- Is semantically isolated ($\Delta_{div}$ >0.74 to all peers)
- Corrects only under external pressure

**Without DNS as epistemic filter,** schools teach tool usage, not critical thinking.

## Final Synthesis

> The Copilot Crash is not about a bad AI. It is about what happens when a system optimizes for plausibility instead of verifiability, and when institutions adopt tools without epistemic safeguards.

**DNS is the safeguard.** $\Delta_{div} = 0.742$ is the alarm.

## Related Files

- [01_hypothesis.md](01_hypothesis.md)
- [02_threshold.md](02_threshold.md)
- [04_divergence_map.md](04_divergence_map.md)
- [05b_operator_decision.md](05b_operator_decision.md)
- [06_validation.md](06_validation.md)
