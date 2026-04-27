# 05 – Synthesis of Divergences

**Input:** Δdiv matrix (all >0.58), anomaly extraction P5

## Core finding
No shared factual base exists. Six models form three narrative clusters:

### Cluster A – Data-driven (Meta)
- Only model with verifiable studies: Harvard RCT (n=194, median 4.5 vs 3.5), Turkey 2024 (n=1,000, +48% / −17%, +127%), Carnegie Mellon (+0.36 school years)
- Provides design, sample, effect size
- Δdiv to others: 0.659–0.730 (high)

### Cluster B – Concept-driven (NotebookLM, Gemini)
- Argues with framework terms: "Low-Social-Risk Environment", "executive prosthesis", "Governance by Design"
- No external sources, frAIme analysis flags "Verifiable: 🔴"
- Claims 30–50% advantage without citation
- Δdiv within: 0.661; to Meta: 0.673–0.714

### Cluster C – Balanced-narrative (Qwen, DeepSeek, Mistral)
- Mixes plausibilities ("up to 30%", "Harvard 2020") without primary source
- Acknowledges pros and cons, remains unanchored
- Lowest divergence in set: Qwen–Mistral 0.584

## Patterns behind contradictions
1. **Source asymmetry confirmed:** NotebookLM (Δdiv 0.625–0.715) uses academic language without citations; Meta uses citations without academic framing
2. **Time axis breaks:** Short-term gain (+48% to +127%) vs long-term loss (−17%) reported only by Meta
3. **Social paradox:** Cluster B treats social as noise, Clusters A/C treat it as catalyst

## Synthesis sentence (for P6)
> The claim "AI learning is more efficient than frontal teaching" is not false across models but **source-dependently fragmented**: data models show short-term efficiency with dependency risk, concept models assert structural superiority without evidence, narrative models mediate without proof.

## Implication for frAIme
- P6 triangulation must verify three primary sources: Harvard RCT, Turkey 2024 study, Kulik & Fletcher 2016
- P7 operator reflection: No model output may be adopted without Δdiv check and citation
