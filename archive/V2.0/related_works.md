## Related Work and Distinction

DNS – originally developed under the working title *Triangulation nach Schult* – sits at the intersection of multi‑agent LLM systems and epistemic uncertainty. Its contribution becomes clear when contrasted with adjacent approaches:

### SCOUT (Uncertainty Triangulation)
SCOUT uses model heterogeneity and critique signals for automated error detection in clinical settings.  
**DNS differs:** it includes **P6 – Meta‑Reflection** and does not aim to "fix" the AI. DNS informs the human operator through structured dissonance.

### AI Council Framework
Council‑based systems orchestrate multiple LLMs to reach **consensus**.  
**DNS differs:** DNS treats **divergence** as the primary epistemic signal. Consensus can hide risk; DNS exposes it.

### Semantic Triangulation
Semantic Triangulation evaluates consistency across linguistic transformations of a single model.  
**DNS differs:** DNS leverages **architectural diversity** (e.g., Grok vs. Claude) to reveal structural blind spots, not just paraphrase stability.

### DiscoUQ (Disentangled Uncertainty Quantification)
DiscoUQ decomposes uncertainty into aleatoric and epistemic components within a single model using latent-space disentanglement.  
**DNS differs:** DiscoUQ quantifies uncertainty *inside* one model; DNS measures **semantic dispersion (Δdiv) *between* heterogeneous models** and makes it operationally visible for human synthesis. DiscoUQ is a statistical estimator – DNS is a governance protocol.

### DelphiAgent / LLM Council‑Double Delphi
Delphi‑style systems aim for iterative convergence.  
**DNS differs:** DNS is designed for **falsification (P1)** and the analysis of **unresolved gaps**, not for agreement or averaging.

---

DNS is not a consensus‑machine.  
It is a **diagnostic framework for uncertainty**, placing the human operator in the role of an active **Synthesizer**.
