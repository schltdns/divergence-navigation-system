DNS – Protocol P1–P6 (Divergence-based Navigation System)
Operational guide to the six-phase DNS protocol

This document provides a detailed, operational guide to the six phases of the DNS (Divergence-based Navigation System) protocol.

P1 – Hypothesis & Falsification Setup
Goal: Define what you want to test and under which conditions you would consider it falsified.

Steps:

Write down 3–5 hypotheses (e.g., “TTF prices are driven by speculation, not supply shortage”).

For each hypothesis, define a measurable falsification threshold (e.g., “H1 is falsified if TTF average >50€/MWh for 10 consecutive days”).

Decide which falsification rules (Rule 1–4) apply.

Output: A document with hypotheses and thresholds.

P2 – Role-Based Model Configuration (Team Architecture v1.5)
Goal: Select LLMs and assign them functional roles according to the DNS team matrix.

Standard DNS configuration:

Role	Instance	Function
S1: Kinetic-Agent	Grok	Raw data, market signals, real-time OSINT
S2: Structural-Architect	ChatGPT	Framework integrity, documentation, logic
S3: Synthesis-Bridge	Gemini	Strategic vision, context expansion, scenarios
S4a: Visualizer	Copilot	Source matrix, data synthesis, operational tools
S4b: Boundary-Marker	Claude	Epistemic precision, safety, risk boundaries
Ω: Falsificator	DeepSeek	Logical stress testing, falsification, backtesting
P5/6: Operator	Human	Final synthesis, judgment, meta‑reflection
Roles are illustrative, not fixed – they can be reassigned to other models with similar epistemic profiles.

Output: List of models and their assigned roles.

P3 – Parallel Elicitation
Goal: Obtain raw, comparable outputs from all models.

Steps:

Write an identical prompt for all models. Include the hypotheses and ask for structured answers (summary, critical points, open questions).

Send the prompt to each model independently (no cross‑feeding).

Copy the raw responses verbatim.

Output: A folder with raw model responses (timestamped).

P4 – Divergence Mapping
Goal: Systematically compare the responses.

Steps:

Create a table with rows for each hypothesis/question and columns for each model.

Mark each cell as:

✅ Confirmed

❌ Rejected

⚠️ Partial/ambiguous

🚫 Refused (with reason)

Categorize divergences:

Content divergence (different factual claims)

Methodological divergence (different approaches to uncertainty)

Bias signals (moralizing, one-sided framing)

Blind spots (missing aspects)

Output: Divergence map table.

P5 – Weighted Synthesis (Human Operator)
Goal: Integrate the perspectives into a coherent conclusion.

Steps:

Identify convergences (points where ≥2 models agree on content).

For divergences, decide which perspective to follow or whether to mark the point as unresolved.

Justify every deviation from the majority/weighting rule in writing.

If more than three unjustified deviations occur, the synthesis is invalid (Rule 3).

Output: A written synthesis (2–5 paragraphs).

P6 – Operator Self-Reflection
Goal: Detect and document human bias.

Mandatory three questions (answer in writing):

Which perspective dominated my synthesis? Did I give it too much weight?

Which perspective did I ignore – and why? Is that reason valid?

Which assumption remained unfalsified – and do I secretly hope it stays that way?

Output: A short self-reflection statement. If any answer reveals significant bias, the synthesis is marked as “operator‑influenced” but can still be valid if justifications are sound.

Falsification Rules (Quick Reference)
Rule	Condition	Consequence
1	After 3 rounds, divergence pattern unchanged	Hypothesis inconclusive
2	Model refusal persists with substitute models	Hypothesis underspecified
3	Operator cannot justify ignoring a model	Synthesis invalid
4	External reviewer finds critical flaw	Return to P1/P3
Template Files
See /TEMPLATES/ for:

prompt_template.md

divergence_map_template.csv

operator_reflection_template.md

Last update: April 8, 2026
Version: 3.8.2‑DNS (Open)
Part of: DNS – Divergence-based Navigation System
