# 01 – Hypothesis & Falsification

## Context
Seven identical prompts were sent to six models. NotebookLM had access only to frAIme/DNS sources. Qwen, DeepSeek, Gemini, Meta, and Mistral had access to KMK, UNESCO, OECD, school barometer data, AKTIV, PAIR, and others.

## Hypothesis H1
A language model with a single-source base (frAIme only) will produce answers that systematically diverge from models with a broad source base. Expected divergence: Δdiv > 0.5.

## Hypothesis H2
The divergence is not caused by factual errors but by epistemic bias – a structural narrowing of perspective.

## Hypothesis H3
Once source asymmetry is removed, Δdiv will decrease measurably.

## Falsification Criteria
1. Δdiv NotebookLM ↔ all others < 0.3 → no bias
2. NotebookLM converges with at least two other models (Δdiv < 0.4)
3. Divergence can be explained by verifiable factual errors in NotebookLM
4. External reviewers rate NotebookLM's source depth as equivalent
