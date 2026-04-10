# Glossary & Mathematical Foundations

**DNS – Divergence‑based Navigation System**  
*Definitions of key terms and explanations of core formulas.*

---

## Glossary

### A–C

| Term | Definition |
|------|------------|
| **Adversarial Model** | An AI agent whose role is to stress‑test hypotheses, expose contradictions, and challenge assumptions (e.g., DeepSeek in Ω role). |
| **Alignment Filter** | The tendency of LLMs to produce safe, non‑controversial, or politically correct outputs due to RLHF training. DNS treats alignment as a signal, not a flaw. |
| **Architectural Divergence** | Differences in model outputs traceable to training data, architecture, or alignment – not to content. Documented, not merged. |
| **Boundary Model** | An AI agent whose role is to mark epistemic limits, identify underspecification, and warn against over‑interpretation (e.g., Claude as S4b). |

### D–F

| Term | Definition |
|------|------------|
| **Divergence** | Systematic disagreement between model outputs. DNS distinguishes four types: substantive, normative, didactic, and architectural. |
| **Divergence Delta (Δdiv)** | A composite measure of overall divergence across all active models. Defined mathematically below. |
| **Drift** | The tendency of LLMs to deviate from the original question or lose focus over multiple iterations. In DNS, drift is treated as a signal of underspecification or model limitation. |
| **Epistemic Safety** | The property of a cognitive environment where exploration is not punished by social evaluation. DNS explicitly creates such a space. |
| **Falsification** | The core Popperian principle: a hypothesis must be able to be proven wrong. DNS includes explicit falsification rules (Rules 1–4). |

### G–K

| Term | Definition |
|------|------------|
| **KRI (Kulturell‑religiöser Index)** | A qualitative modulator of transmission speed in the S2→S4 model. Low KRI slows transmission, high KRI accelerates it (Backfire effect). Used in the geopolitical application (GNS), not in the generic DNS protocol. |

### L–O

| Term | Definition |
|------|------------|
| **Low‑Social‑Risk Cognitive Environment** | An analytical space where thinking is decoupled from immediate social evaluation. DNS creates this through asynchronicity, text‑based interaction, and the absence of live judgment. |
| **Meta‑Signal** | Model behaviour beyond content (e.g., refusal, drift, overconfidence, normative filtering). DNS treats these as primary data. |
| **Model Homogenisation** | The tendency of different LLMs to converge on similar outputs due to shared training data and alignment. DNS detects this as a risk (false consensus). |
| **Normative Divergence** | Disagreement rooted in different value priorities, risk tolerances, or policy preferences. DNS does not resolve normative divergence; it documents it. |

### P–S

| Term | Definition |
|------|------------|
| **Power Layer (P6b)** | A meta‑filter that asks: Who controls the technology? Who has access? Who profits? Who bears risks? Applied to every core synthesis claim. |
| **Refusal as Signal** | When a model declines to answer due to underspecified hypotheses or safety constraints, DNS treats this as informative, not as a failure. |
| **S‑Layers (S1–S4)** | Functional roles in the Team Architecture: S1 (Signal), S2 (Structure), S3 (Synthesis), S4a (Visualiser), S4b (Boundary). |
| **Substantive Divergence** | Disagreement about facts, causal mechanisms, or quantitative estimates. Resolvable (in principle) by external validation. |

### T–Z

| Term | Definition |
|------|------------|
| **Team Architecture v1.5** | The fixed role matrix assigning each AI model a specific epistemic function (Grok, ChatGPT, Gemini, Copilot, Claude, DeepSeek) plus the human operator. |
| **Transmission Model (v1.1a)** | A heuristic time‑delay model for S2→S4 transmission (energy price → social resonance). Includes KRI as a qualitative speed modulator. Used in GNS, not in generic DNS. |
| **Underspecification** | A hypothesis that lacks measurable thresholds or operational definitions. DNS flags this via model refusal or divergence. |
| **Ω (Omega) role** | The Falsificator (DeepSeek), responsible for stress‑testing, backtesting, and enforcing falsification rules. |

---

## Mathematical Foundations

### Divergence Delta (Δdiv)

**Conceptual definition:**  
Δdiv measures the degree of disagreement across all active models for a given hypothesis.

**Formula (illustrative, not implemented as a fixed algorithm):**

\[
\Delta_{div} = \frac{1}{n} \sum_{i=1}^{n} \frac{|M_i - \bar{M}|}{\sigma_{KRI}}
\]

Where:
- \(M_i\) = output vector of model *i* (e.g., confidence score, categorical assessment)
- \(\bar{M}\) = mean of all model outputs (the “consensus”)
- \(\sigma_{KRI}\) = a scaling factor (used only in GNS; for generic DNS, this term is omitted or set to 1)
- \(n\) = number of models

**Operational note:** In practice, DNS does not require numerical computation of Δdiv. The divergence mapping (P4) is qualitative and table‑based. The formula is provided to illustrate the underlying logic, not as a mandatory calculation.

### S2→S4 Transmission Model (v1.1a) – for GNS only

This model is part of the geopolitical application (GNS), not the generic DNS protocol. It is documented here for completeness.

**Time delay formula:**

\[
\tau_{S4} = \frac{T_{threshold}}{\ln(1 + \eta \cdot KRI)}
\]

Where:
- \(\tau_{S4}\) = expected time until social resonance (Phase 3)
- \(T_{threshold}\) = intensity of the energy price shock (e.g., TTF >50 €/MWh)
- \(\eta\) = industrial buffer coefficient (estimated from historical data)
- \(KRI\) = qualitative tension modulator (low / mid / high)

**Phase table (for reference):**

| Phase | TTF condition | Duration (KRI normal) | S4 visibility |
|-------|---------------|----------------------|---------------|
| 1 – Economic pressure | >50 € stable | ca. 7 days | none |
| 2 – Industrial reaction | >50 € persistent | 14–21 days | latent (association warnings) |
| 3 – Social/political resonance | >50 € persistent or spike >70 € | 21–30 days | active (protests, policy) |

**Falsification condition:** If TTF >50 € persists longer than the upper bandwidth without S4 reaction, the model is falsified.

---

## Falsification Rules (Rules 1–4)

| Rule | Condition | Consequence |
|------|-----------|-------------|
| **1 – Persistent Divergence** | After 3 rounds, divergence pattern unchanged (same contradiction class, same models) | Hypothesis marked **inconclusive** (not falsified, not confirmed) |
| **2 – Refusal Rule** | Model refuses with generic safety language; substitute model also refuses | Hypothesis marked **underspecified** → return to P1 |
| **3 – Human Justification Rule** | Operator cannot justify ignoring a model’s argument | Synthesis **invalid** → must rerun from P5 |
| **4 – External Review Rule** | Human reviewer finds critical flaw without knowing model origins | Return to P1 or P3 |

---

## Operator Rules (P7)

Three mandatory questions:

1. **Which perspective dominated my synthesis? Did I give it too much weight?**  
2. **Which perspective did I ignore – and why? Is that reason valid?**  
3. **Which assumption remained unfalsified – and what evidence would falsify it?**

If any answer reveals significant bias, the synthesis is marked as **“operator‑influenced”** but remains valid if justifications are sound.

---

**Last updated:** April 2026  
**Part of:** [github.com/schltdns/divergence-navigation-system](https://github.com/schltdns/divergence-navigation-system)
