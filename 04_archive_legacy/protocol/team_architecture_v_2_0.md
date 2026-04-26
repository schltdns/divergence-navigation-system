DNS Team Architecture 2.0 – Triangulation Framework
Version: 2.0 (2026-04-20)
Visual: Ω-Meta-Control (Human) at the center
![DNS Triangulation Framework](../docs/assets/dns_triangulation_framework.png)
---
The Principle
DNS is not a consensus tool. It is a triangulation framework for multi-model analysis. The human (Ω) steers; the models provide friction.
---
Roles in the Loop (as shown in diagram)
S1 Qwen – Raw Signals / Raw Data
Function: unfilted data collection, broad coverage
Input: web, papers, databases
Output: raw material for S2
S2 Copilot – Dynamics / Drift
Function: detects temporal change, narrative drift
Output: trend curves, "what is changing right now?"
S3 Gemini – Structure / Scenarios
Function: builds scenario grids, organizes information
Output: matrices, scenario trees
S4a Mistral – Divergence / Friction
Function: calculates Δdiv, deliberately creates friction
Output: divergence score, conflict points
S4b Meta/LLaMA – Limits / Epistemics
Function: marks knowledge boundaries, "what don't we know?"
Output: uncertainty flags ⚠️
F1 DeepSeek – Falsification / Critique
Function: attacks when data is incomplete (Error Propagation)
Trigger: "When data is incomplete → DeepSeek triggers"
Output: counter-hypotheses, kill criteria
Ω – Meta-Control (Human)
At the center. No model decides alone.
Applies the Four Questions Method:
On topic? 🟢 / 🔴
New idea? 🟢 / 🟡 / 🔴
Verifiable? (number, date, place, if-then) 🟢 / 🔴
Understandable? 👍 / 👎
Good answer = 🟢 + 👍
---
Workflow (Live in v2.2)
Input → S1 Qwen collects
Dynamics → S2 Copilot tracks drift
Structure → S3 Gemini builds scenarios
Friction → S4a Mistral measures Δdiv live
Limits → S4b Meta flags epistemic gaps
Falsification → F1 DeepSeek tests gaps
Human → Ω decides with traffic light
Error Propagation: if S1 is incomplete → F1 activates → feedback to S1
---
Why This Architecture?
Not 7x the same model: each model has an epistemic role
Human remains in the loop: Ω is not a metaphor but a governance requirement (EU AI Act Art. 14)
Validated: Copilot Crash (Δdiv = 0.742) ran exactly through this loop
---
For Zenodo / arXiv
This diagram replaces the abstract "team architecture." It is:
Reproducible (roles are model-agnostic)
Teachable (students understand hexagons instantly)
Auditable (every step logs Δdiv)
Files for v2.2:
`protocol/team\_architecture\_v\_2\_0.md` (this file)
`docs/assets/dns\_triangulation\_framework.png`
`teaching/4\_questions.md`
---
DNS v2.2 – Divergence Navigation System – CC BY-NC-SA 4.0
