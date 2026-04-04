# Triangulation nach Schult (v1.0‑Open)
**"Divergence is a signal, not noise."**  
A formal multi‑agent protocol for structured decision‑making and uncertainty mapping using Large Language Models (LLMs).  
**Divergence > Consensus.**

---

## 🎯 The Problem
Traditional AI consensus methods (voting, averaging, multi‑agent debate) aim for a single “correct” answer.  
But because LLMs share training data and alignment biases, **consensus often hides systemic errors**.

When multiple models confidently agree on a falsehood, the risk becomes invisible.

---

## 🚀 The Solution: Triangulation nach Schult
This framework treats **dissonance, disagreement, drift, and even model refusal** as primary data points.  
It provides a **6‑phase operational protocol** to transform conflicting AI outputs into a **robust, non‑falsified human synthesis**.

The method is:
- model‑agnostic  
- falsifiable  
- recursive  
- didactically applicable  
- open‑source  

---

## 🛠 The 6‑Phase Protocol (P1–P6)

### **P1 — Hypotheses & Falsification**
Define clear, measurable thresholds.  
Example: *“If Gas Price > 50€, H1 is false.”*

### **P2 — Team Architecture**
Assign functional roles to diverse models:  
Signal • Structure • Boundaries • Falsification • Dynamics • Critique.

### **P3 — Parallel Elicitation**
Send an **identical prompt** to all models to ensure context constancy.

### **P4 — Divergence Mapping**
Categorize contradictions:  
- Content divergence  
- Meta‑/methodological divergence  
- Bias signals  
- Blind spots  

### **P5 — Weighted Synthesis**
The human operator integrates findings and **explicitly justifies** any deviation from model outputs.

### **P6 — Operator Self‑Reflection**
A mandatory 3‑question check to surface human confirmation bias.

---

## 📊 Real‑World Case Study: Energy Market 2026
This repository includes a documented test case (April 4, 2026) analyzing the European gas market (TTF) during the Hormuz crisis.

**Models used:**
- Grok → Signal  
- Claude → Boundaries  
- Copilot → Dynamics  

**Outcome:**  
The protocol identified a structural shift from speculation to supply‑driven volatility.  
A model refusal served as a critical signal for an underspecified hypothesis.

---

## 📂 Repository Structure

```
WHITE_PAPER.md          → Full methodological description (arXiv: cs.AI)
PROTOCOL.md             → Step‑by‑step P1–P6 instructions
CASE_STUDY_ENERGY.md    → April 2026 test case (verbatim transcripts + synthesis)
TEMPLATES/              → Prompt templates & synthesis spreadsheets
```

---

## ⚖️ License & Intellectual Property
**Method & Documentation:** Apache License 2.0  
You are free to use, modify, and distribute this framework.

**Proprietary Context:**  
High‑level system prompts used in the GNS (Geopolitical Navigation System) remain proprietary to the author.

---

## ✍️ Author & Citation

**Denis Schult**  
Independent Researcher, Germany  
Email: *schltdns@gmail.com*

If you use this framework in research or industry, please cite:

> Schult, D. (2026). *Triangulation nach Schult: A Recursive Multi‑Agent Framework for Robust Decision‑Making under Epistemic Uncertainty.*  
> GitHub Repository / arXiv: cs.AI.

---

## 📥 Quick Start

1. Define 3 hypotheses for your current problem.  
2. Set a falsification threshold for each.  
3. Run the **same prompt** through 3 different LLMs.  
4. Map the divergence — ignore consensus initially.  
5. Perform the operator reflection (P6).  

---

## 🧩 Why Divergence > Consensus
Consensus hides risk.  
Divergence reveals structure.

This framework helps you see what the models cannot see about themselves — and what you cannot see without them.

