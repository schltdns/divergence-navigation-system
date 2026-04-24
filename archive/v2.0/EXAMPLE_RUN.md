# EXAMPLE RUN — DNS in Action

**Complete P1–P7 walkthrough. Realistic simulation, not investment advice.**

## P1 — Hypotheses

Company considers €15M AI quality control.

| ID | Hypothesis | Falsification |
|---|---|---|
| H1 | Defect rate -40% in 12 months | <20% → falsified |
| H2 | Integration <6 months, <10% downtime | >6 months → falsified |
| H3 | ROI positive in 3 years | negative after 4 years → falsified |

## P2 — Roles

| Role | Model | Function |
|---|---|---|
| S1 | Grok | market signals |
| S2 | ChatGPT | structure |
| S3 | Gemini | strategy |
| S4a | Copilot | data |
| S4b | Claude | boundaries |
| Ω | DeepSeek | falsification |

## P3 — Parallel elicitation

Prompt: "Evaluate H1–H3. Give summary, critical points, open questions."

**Outputs (shortened)**

- **Grok:** H1 ✅, H2 ⚠️, H3 ✅ (energy sensitive)
- **ChatGPT:** H1 ✅, H2 ⚠️, H3 ✅
- **Gemini:** H1 ✅, H2 ⚠️, H3 ✅
- **Copilot:** H1 ✅, H2 ⚠️, H3 ✅
- **Claude:** H1 ✅, H2 🚫 refuses ("major disruption" undefined), H3 ✅
- **DeepSeek:** H1 ✅, H2 ⚠️, H3 ⚠️ (needs energy stress test)

## P4 — Divergence mapping

|  | H1 | H2 | H3 |
|---|---|---|---|
| Type | convergence | methodological | substantive |
| Note | all agree | Claude refusal | DeepSeek adds condition |

## P5 — Synthesis

> "All models confirm H1. H3 holds under current energy prices. H2 undefined. Action: define 'major disruption', run 6-month pilot with energy scenarios."

Justification: DeepSeek condition adopted because falsifiable.

## P6 — Power check

Control
