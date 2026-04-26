# DNS Operationalization Report – 15 April 2026 (Final Version)

## Background
The Divergence Navigation System (DNS) provides a theoretical framework for epistemic robustness. However, earlier test runs (Runde 1–3) revealed a critical flaw: when agents (LLMs) are exposed to protocol details (Δdiv, smoothing, drift), they abandon the content and enter meta-discussions about DNS itself. This frame drift made the method unusable for learners and practitioners.

## Objective
Operationalize DNS into a practical, EU AI Act-compliant method that can be used by students, teachers, and administrators – without any knowledge of the underlying protocol.

## Solution: Two-Layer Architecture

### Frontend – Four Questions Method
1. **On topic?** 🟢 / 🔴
2. **New idea?** 🟢 / 🟡 / 🔴
3. **Verifiable?** (number, date, place, if-then) 🟢 / 🔴
4. **Understandable?** 👍 / 👎

**Good answer = 🟢 + 🟢 + 👍**

### Backend – Safety Layer (EU AI Act)
| Component | Function | AI Act Article |
|-----------|----------|----------------|
| Bias detection (SHAP alerts) | Shows feature importance, marks yellow when protected feature contributes >25% | Art. 13 Transparency |
| Formal dissent | Mandatory justification (≥140 characters) for any deviation from AI recommendation | Art. 14 Human Oversight |
| Audit trail | Hash-anchored logs (Merkle root + IPFS), session-based daily rotating salts | Art. 9, 15, 19 |

All logs use no personal profiles – only session hashes, fully DSGVO-compliant (Art. 89).

## Interventions-Trigger

**1. Q3 Verifiability → 🔴**  
Stop. *"Add a concrete detail – otherwise we cannot evaluate the answer."*

**2. Q1 Topic relevance → 🔴**  
Reset. *"Back to the original question."*

**3. Q2 New idea → 🔴**  
Elaborate. *"Can you specify, give an example, or formulate a counter-point?"*

**Teacher does NOT:** judge right/wrong, give grades, discuss DNS meta-level.

## Implementation Artifacts (v2.1)

- `vier_fragen_methode.pdf`
- `mapping_ai_act.pdf`
- `safety_layer_schema_v2.json`
- `minimal_safety_layer.py`
- `dns_open_data_proof.json`
- `LICENSE-DOCS.txt` (CC BY-NC-SA 4.0)
- `LICENSE-CODE.txt` (Apache-2.0)

**Links**
- Zenodo: https://doi.org/10.5281/zenodo.19597808
- GitHub: https://github.com/schltdns/divergence-navigation-system
- IPFS CID: `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy`
    - ipfs://bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy
    - https://ipfs.io/ipfs/bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy
    - https://dweb.link/ipfs/bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy

## Key Lessons Learned
1. Agents must never see the protocol
2. The human operator is irreplaceable
3. Legal protection requires dual licensing
4. Open-Data proof works without blockchain

## Next Steps
- Pilot at Montessori school
- Legal validation by lawyer
- Case study publication

---
**License:** CC BY-NC-SA 4.0  
**Copyright:** Denis Schult, 2026
