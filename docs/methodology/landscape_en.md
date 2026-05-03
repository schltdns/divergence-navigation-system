# Landscape Comparison: frAIme vs. Established Methodologies

> **Document Purpose**: Comparative analysis positioning frAIme within decision-support, uncertainty quantification, and AI governance.  
> **QUELLENMATRIX Compliance**: Core = Must; Supplemental = Nice-to-have; Deviations marked.  
> **Version**: 1.0.0 | **Generated**: 2026-05-03

---

## 1. Scope & Methodology

### 1.1 Criteria
| Criterion | Definition | frAIme Implementation |
|-----------|------------|---------------------|
| **Multi-Source Input** | Structured aggregation | P3: Isolated prompts S1–Ω |
| **Divergence Handling** | Treatment of disagreement | P4: Δdiv as signal |
| **Ethical Reflexion** | Power/risk analysis | P6b: Power Layer Check |
| **Auditability** | Reproducibility | P8: Versioned manifests |

---

## 2. Comparative Analysis

| Framework | Similarity | Critical Difference | Source |
|-----------|------------|---------------------|--------|
| **Delphi Method** | Multi-expert input | Goal: *consensus*; frAIme: *divergence preservation* | Core |
| **MCDA** | Weighted aggregation | Weights: *expert-assigned*; frAIme: *Δdiv-derived* | Core |
| **Structured Expert Judgment** | Calibration | Calibration: *historical*; frAIme: *semantic drift* | Core |
| **AI Agent Governance** | Phase-gating | No divergence metric | Supplement |
| **Governance-as-a-Service** | Multi-agent runtime | Trust: *rule-based*; frAIme: *epistemic* | Supplement |
| **Uncertainty Quantification** | Aleatoric/epistemic | Focus: *statistical*; frAIme: *semantic* | Supplement |

### 2.1 Novel Contributions
1. **Hybrid Δdiv**: `Δdiv = 1 − (Jaccard_sem + Cosine) / 2`
2. **Divergence-as-Signal**: Thresholds <0.15 consensus; >0.70 blind spot
3. **Power Layer (P6b)**: Mandatory "who benefits / who bears risk"
4. **Versioned Audit (P8)**: Machine-readable manifests

---

## 3. Deviations
| Norm | frAIme | Rationale |
|------|--------|-----------|
| Consensus goal | Divergence signal | Consensus may reflect shared bias |
| Static weights | Dynamic Δdiv | Objective, context-sensitive |
| Ethics separate | Ethics embedded | Power analysis is decision-relevant |

---

## 4. Reproducibility
**Core sources**: Delphi (1963), MCDA (2002), SEJ (1991), NIST AI RMF (2023), ISO/IEC 42001  
**frAIme**: DOI `10.5281/zenodo.19793185`

---

## 5. Conclusion
frAIme is a complementary epistemic layer that makes the quality of disagreement visible, actionable, and auditable.
