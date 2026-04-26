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

````24 Zeilen verborgen
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
└── readme.md````


## Delta Div (Δdiv) – The DNS Metric
Δdiv = 0.5 * (1 - Jaccard) + 0.5 * (1 - Cosine)

- 0.742 indicates contested territory – no generalization allowed
- Copilot shares <26% semantic basis with any other model

## Implications for MSB NRW

The MSB NRW partners with Microsoft for "KI-Skilling.NRW" – training 200,000 teachers on Copilot. Copilot produces unverified geopolitical narratives. Without DNS as epistemic filter, schools learn tool usage, not critical thinking.

## License

**DNS Framework – Governance by Design, not Ethics by Declaration**

Copyright © 2026 Denis / DNS Project

Permission is granted to use, copy, and adapt this case study for research, education, and governance purposes, provided that:

1. Attribution to the DNS Framework is preserved
2. Modifications are documented
3. No unverified claims are presented as fact without falsification

## Licensing

This repository uses **dual licensing** to protect the method from commercial appropriation while keeping code open:

**Code and implementations** (`calc_delta_div.py`, `/heatmap`, scripts)  
- **License:** Apache-2.0  
- **File:** [LICENSE-CODE](./LICENSE-CODE)  
- Allows use, modification, and commercial use with attribution

**Documentation, method, and teaching materials** (`/01-07_*.md`, `/04_divergence_map.md`, `/05_synthesis.md`, this case study)  
- **License:** Creative Commons BY-NC-SA 4.0  
- **File:** [LICENSE-DOCS](./LICENSE-DOCS)  
- Allows: sharing and adaptation for non-commercial purposes (education, research)  
- Requires: attribution, share-alike, no commercial use

**Why dual?**  
Code should remain forkable. The method itself should stay free for education and not be enclosed by commercial providers.

**Open-Data Proof**  
Version v1.2 will be anchored with SHA256 hash and IPFS CID. See `dns_open_data_proof.json` (coming).

