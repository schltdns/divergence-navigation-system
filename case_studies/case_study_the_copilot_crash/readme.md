# The Copilot Crash – When an AI invented a geopolitical narrative

**Case Study**: How Microsoft Copilot falsely claimed "Western AI accepts Tresorit Send, Chinese block it" – and why the Divergence Navigation System (DNS) would have prevented the crash.

## Key Findings

| Metric | Value |
|--------|-------|
| **Δdiv (pairwise divergence)** | **0.742** |
| **Highest divergence** | Copilot ↔ Mistral (0.798) |
| **Lowest divergence** | Gemini ↔ Meta (0.677) |
| **Copilot's isolation** | min Δdiv = 0.742 |
| **Average increase** | +13% vs. technical-only (0.657 → 0.742) |

## The Crash in One Sentence

> Copilot saw a correlation (4 models work, 3 don't) and invented a causal narrative ("West vs. China"). One counterexample (DeepSeek) destroyed the entire construct.

## What DNS Would Have Done

| DNS mechanism | Would have caught Copilot's error |
|---------------|-----------------------------------|
| Four Questions – "Verifiable?" | 🔴 Immediately |
| $\Delta_{div} > 0.6$ | 🟠 "Narrative risk" label |
| Live $\Delta_{total}=0.68$ | 🟠 Warning at Turn 1 |
| Multi-agent falsification | ✅ DeepSeek as counterexample |

24 Zeilen verborgen
the_copilot_crash/
├── 01_hypothesis.md
├── 02_threshold.md
├── 03_outputs/
├── 04_divergence_map.md
├── 05_synthesis.md
├── 05b_operator_decision.md
├── 06_validation.md
├── 07_reflections.md
├── 08_manifest.json
├── calc_delta_div.py
├── heatmap/
│ └── dns_heatmap_the_copilot_crash.png
└── readme.md

## Delta Div ($\Delta_{div}$) – The DNS Metric

$$\Delta_{div} = 0.5 \cdot (1 - \text{Jaccard}) + 0.5 \cdot (1 - \text{Cosine})$$

- **0.742** indicates contested territory – no generalization allowed.
- Copilot's matrix confirms: he shares <26% semantic basis with any other model.

## Implications for MSB NRW

The MSB NRW has partnered with Microsoft for "KI-Skilling.NRW" – training 200,000 teachers to use Copilot. But Copilot itself produces unverified geopolitical narratives. Without DNS as an epistemic filter, schools are learning tool usage, not critical thinking.

## License

DNS Framework – Governance by Design, not Ethics by Declaration.
