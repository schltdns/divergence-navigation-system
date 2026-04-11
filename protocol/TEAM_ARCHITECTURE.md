# DNS Team Architecture v1.5

**Role‑based multi‑model architecture for epistemic divergence analysis**

DNS uses a fixed, reproducible role matrix (S1–Ω + Human Operator).  
Each role contributes a distinct epistemic function.  
The goal is not consensus, but **structured divergence**.

DNS is model‑agnostic: any LLM can fill any role, as long as the epistemic function is preserved.

---

## 🧩 Role Matrix (S1–Ω)

| Role | Agent Type | Epistemic Function |
|------|------------|--------------------|
| **S1 — Signal Layer** | Fast, high‑variance model (e.g., Grok) | Generates kinetic first‑pass signals; maximizes breadth and variation |
| **S2 — Structure Layer** | Stable, structured model (e.g., ChatGPT) | Produces logical scaffolding, documentation, and normalization |
| **S3 — Synthesis Layer** | Strategic, high‑context model (e.g., Gemini) | Integrates perspectives, frames long‑term structure, identifies conceptual gaps |
| **S4a — Precision Layer** | Tool‑oriented model (e.g., Copilot) | Ensures technical clarity, metric precision, reproducibility |
| **S4b — Boundary Layer** | Normative‑sensitive model (e.g., Claude) | Detects underspecification, overclaiming, normative drift |
| **Ω — Falsification Layer** | Adversarial model (e.g., DeepSeek) | Stress‑tests assumptions, challenges claims, exposes contradictions |
| **S4 (Human Operator)** | Human | Final synthesis, justification, reflection, responsibility |

---

## 🧠 Design Principles

### 1. **Heterogeneity over consensus**
DNS requires epistemic diversity.  
Roles must differ in:

- training distribution  
- reasoning style  
- normative tendencies  
- error profiles  

Homogeneous models reduce Δdiv and weaken the signal.

---

### 2. **Role fidelity**
A model must behave according to its epistemic function, not its brand identity.

Example:  
A model in S2 must prioritize structure — even if it is capable of S3‑style synthesis.

---

### 3. **Human‑in‑the‑loop sovereignty**
The operator:

- integrates signals  
- documents reasoning  
- performs bias reflection  
- carries epistemic responsibility  

DNS is not an autopilot.

---

### 4. **Reproducibility**
The architecture must be:

- fixed  
- documented  
- versioned  
- auditable  

This ensures Δdiv comparisons remain meaningful across runs.

---

## 🔄 Interaction Flow (High‑Level)

1. **S1** generates broad, high‑variance signals  
2. **S2** structures and normalizes  
3. **S3** synthesizes and reframes  
4. **S4a** ensures technical precision  
5. **S4b** checks boundaries and normative drift  
6. **Ω** falsifies and stress‑tests  
7. **Human Operator** performs final synthesis (P5–P7)

Full protocol:  
👉 [`protocol/P1_P6_protocol.md`](P1_P6_protocol.md)

---

## 🖼 Architecture Diagram

The visual overview of the role matrix:  
👉 `dns_architecture.png`

---

## 📌 Notes

- DNS does not require specific vendors — only epistemic functions.  
- Roles can be reassigned as models evolve.  
- The architecture is stable across domains (logic, economics, geopolitics, safety).  
- GNS/TNS use the same architecture but apply it to domain‑specific pipelines.

---

## 📜 License

This file is part of the DNS project and is released under the **Apache‑2.0 license**.  
See `LICENSE` for details.
