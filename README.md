# Triangulation nach Schult (TNS) — v1.0‑Open
**"Divergence is a signal, not noise."**  
A formal multi‑agent protocol for decision‑making, AI evaluation, and uncertainty mapping using Large Language Models (LLMs).  
**Divergence > Consensus.**

---

## 🎯 Why TNS Exists
Most AI evaluation frameworks try to *reduce* disagreement (e.g., voting, averaging, ensemble methods).  
But because modern LLMs share training data, alignment norms, and structural biases, **consensus often hides systemic error**.

When multiple models confidently agree on a falsehood, the error becomes invisible.

**TNS reverses the logic:**  
Disagreement, drift, refusal, and contradiction are treated as *primary analytical signals*.

---

## 🚀 What TNS Does
TNS provides a **6‑phase operational protocol** that transforms conflicting AI outputs into a structured, falsifiable, human‑led synthesis.

The method is:

- **model‑agnostic**  
- **falsifiable** (explicit thresholds)  
- **recursive**  
- **didactically applicable**  
- **open‑source**  
- **human‑in‑the‑loop by design**

TNS does **not** aim for consensus.  
It aims for **epistemic stability under divergence**.

---

## 🔬 Novelty Claim
TNS is distinct from:

- classical triangulation (Denzin, Patton)  
- Delphi methods  
- ensemble learning  
- multi‑agent debate systems  

Because TNS:

1. **Operationalizes divergence** as a structured data layer  
2. Uses **role‑based model decomposition** (Signal, Structure, Boundaries, Falsification, Dynamics, Critique)  
3. Applies **explicit falsification thresholds**  
4. Requires **mandatory human justification** for synthesis  
5. Includes **operator self‑reflection** to detect human bias  

This combination does not exist in current AI evaluation frameworks.

---

# 🛠 The 6‑Phase TNS Protocol (P1–P6)

### **P1 — Hypotheses & Falsification**
Define hypotheses and measurable falsification thresholds.  
Example:  
*“If Gas Price > 50€, H1 is false.”*

### **P2 — Team Architecture**
Assign functional roles to diverse models:  
**Signal • Structure • Boundaries • Falsification • Dynamics • Critique**

### **P3 — Parallel Elicitation**
Send the **same prompt** to all models.  
No cross‑contamination. No iterative debate.

### **P4 — Divergence Mapping**
Categorize contradictions:

- content divergence  
- methodological divergence  
- bias signals  
- blind spots  
- refusals / safety‑filter artifacts  

### **P5 — Weighted Human Synthesis**
The operator integrates findings and **must justify**:

- why certain model outputs were included  
- why others were excluded  
- how divergence informed the final position  

### **P6 — Operator Self‑Reflection**
A mandatory 3‑question check:

1. *Did I prefer the model that matched my prior belief?*  
2. *Did I ignore a divergence because it was inconvenient?*  
3. *Would another operator reach the same synthesis?*

---

# 📊 Workflow Diagram (Mermaid)

```mermaid
graph TD
    classDef stage fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef human fill:#e1f5fe,stroke:#01579b,stroke-width:2px,font-weight:bold;
    classDef models fill:#fff3e0,stroke:#ef6c00,stroke-width:2px;

    Start((Start)) --> S1[Stage 1: Initialization]
    S1 --> S2[Stage 2: Role Assignment]
    
    subgraph Parallel_Processing [Multi-Agent Layer]
        S3[Stage 3: Parallel Multi-Agent Prompting]
        M1(Model A: Falsifier) -.-> S3
        M2(Model B: Historicator) -.-> S3
        M3(Model C: Structuralist) -.-> S3
    end

    S3 --> S4[Stage 4: Divergence Mapping]
    S4 --> S5[Stage 5: Human-in-the-Loop Synthesis]
    S5 --> S6[Stage 6: Epistemic Reflection]
    S6 --> End((Validated Insight))

    class S1,S2,S4,S6 stage;
    class S5 human;
    class S3,M1,M2,M3 models;
📚 Real‑World Case Study (Included in Repository)
Energy Market 2026 — Hormuz Crisis (TTF Gas)  
Models used:

Grok → Signal

Claude → Boundaries

Copilot → Dynamics

Outcome:

Identified a structural shift from speculation → supply‑driven volatility

A model refusal revealed an underspecified hypothesis

Divergence mapping exposed hidden assumptions in the initial scenario

📂 Repository Structure
Code
README.md               → Overview (this file)
WHITE_PAPER.md          → Full methodological description (arXiv: cs.AI)
PROTOCOL.md             → Step-by-step P1–P6 instructions
CASE_STUDY_ENERGY.md    → April 2026 test case (verbatim transcripts + synthesis)
TEMPLATES/              → Prompt templates & synthesis spreadsheets
⚖️ License & Intellectual Property
Method & Documentation: Apache License 2.0
Free to use, modify, and distribute.

Proprietary Context:  
High‑level system prompts used in the GNS (Geopolitical Navigation System) remain proprietary to the author.

✍️ Author & Citation
Denis Schult  
Independent Researcher, Germany
Email: schltdns@gmail.com

If you use this framework in research or industry, please cite:

Schult, D. (2026). Triangulation nach Schult (TNS): A Recursive Multi‑Agent Framework for Robust Decision‑Making under Epistemic Uncertainty.  
GitHub Repository / arXiv: cs.AI.

📥 Quick Start
Define 3 hypotheses for your problem.

Set falsification thresholds.

Run the same prompt through 3+ LLMs.

Map divergence — ignore consensus initially.

Perform the operator reflection (P6).

🧩 Why Divergence > Consensus
Consensus can obscure systemic risk.
Divergence reveals structure.

TNS helps you see what the models cannot see about themselves —
and what you cannot see without them.
