# Hypothesis: Copilot invents a geopolitical narrative without technical evidence

## The Claim (from Copilot)

> "All Western AI chats accept Tresorit Send, all Chinese block it. This is not coincidence – this is policy."

## The Counterexample (provided by user Denis)

| Model | Origin | Tresorit Status |
|-------|--------|-----------------|
| DeepSeek | China | ✅ works |
| Gemini | USA | ❌ blocked |
| Mistral | France | ❌ blocked |

**One counterexample is sufficient to falsify a universal claim.**

## The Real Cause (technical)

Tresorit Send uses:
- Zero-knowledge token links (key in URL fragment)
- 302 redirects
- Client-side decryption

Some web UIs allow this (liberal fetch policy), others block it (restrictive sandbox).  
**Not culture. Not origin. Policy.**

## DNS Hypothesis

> If DNS had been applied, Copilot's claim would have been flagged as "unverifiable" before it could spread.

## Delta Div ($\Delta_{div}$)

\[
\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})
\]

For this case, $\Delta_{div} = 0.657$ – high structural divergence, narrative risk.

## Related Files

- [02_threshold.md](02_threshold.md)
- [04_divergence_map.md](04_divergence_map.md)
- [05_synthesis.md](05_synthesis.md)
- [06_validation.md](06_validation.md)
