DNS Operationalization Report – 15 April 2026 (Final Version)
Background
The Divergence Navigation System (DNS) provides a theoretical framework for epistemic robustness. However, earlier test runs (Runde 1–3) revealed a critical flaw: when agents (LLMs) are exposed to protocol details (Δdiv, smoothing, drift), they abandon the content and enter meta-discussions about DNS itself. This frame drift made the method unusable for learners and practitioners.
Objective
Operationalize DNS into a practical, EU AI Act-compliant method that can be used by students, teachers, and administrators – without any knowledge of the underlying protocol.
Solution: Two-Layer Architecture
Frontend – Four Questions Method (for learners)
A simple traffic-light checklist:
Thema getroffen? 🟢 / 🔴
Neue Idee? 🟢 / 🟡 / 🔴
Überprüfbar? (Zahl, Datum, Ort, Wenn-Dann) 🟢 / 🔴
Verständlich? 👍 / 👎
Good answer = 🟢 + 🟢 + 🟢 + 👍
Backend – Safety Layer (EU AI Act compliant)
Component	Function	AI Act Article
Bias detection (SHAP alerts)	Shows feature importance, marks yellow when protected feature contributes >25%	Art. 13 (Transparency)
Formal dissent	Mandatory justification (≥140 characters) for any deviation from AI recommendation	Art. 14 (Human Oversight)
Audit trail	Hash-anchored logs (Merkle root + IPFS), session-based daily rotating salts	Art. 9, 15, 19
All logs use no personal profiles – only session hashes, fully DSGVO-compliant (Art. 89).
Interventions-Trigger (for Teachers / Operators)
The Four Questions Method remains deliberately simple. The teacher intervenes only at three clear signals – with graded intensity.
1. Question 3 (Verifiability) → 🔴
Stop signal for the entire learning process.  
An answer without verifiable information (number, date, place, or clear condition) cannot be assessed.
The teacher stops and asks:  
"Add a concrete detail – otherwise we cannot evaluate the answer."
→ No further work until 🔴 turns 🟢.
2. Question 1 (Topic relevance) → 🔴
Abort and redirect.  
If the answer drifts away from the original topic (frame drift), it is not evaluated further.
The teacher resets:  
"Back to the original question."
→ Factual restart without judgment.
3. Question 2 (New idea) → 🔴 (only agreement)
Activate own thinking.  
If the answer merely agrees, the teacher asks for elaboration:
"Can you specify, give an example, or formulate a counter-point?"
→ Continuation only when an independent contribution is recognisable.
What the teacher does NOT do:
No judgment (right/wrong)
No grades
No meta-discussion about DNS
The interventions are purely procedural – they secure the structure without steering the learning process.
Implementation Artifacts (v2.1)
All files are published on Zenodo and IPFS:
`vier_fragen_methode.pdf` – learner's flyer (German)
`mapping_ai_act.pdf` – legal mapping (German)
`safety_layer_schema_v2.json` – JSON schema for logs
`minimal_safety_layer.py` – Python reference implementation
`dns_open_data_proof.json` – IPFS CID + SHA256 hash
`LICENSE-DOCS.txt` – CC BY-NC-SA 4.0 (documentation & teaching)
`LICENSE-CODE.txt` – Apache-2.0 (code components)
Links:
Zenodo v2.1: 10.5281/zenodo.19597808
GitHub: schltdns/divergence-navigation-system
IPFS CID: `bafkreiblue2cs6e4xmpbpklkswimpzgnoumszgkvcm5csukdiqhqkf7wyy` (see proof file)
Key Lessons Learned
Agents must never see the protocol. Frame drift disappears when operators only receive the question and the previous answer.
The human operator is irreplaceable. Only a human can decide when to cut, forward, or restart.
Legal protection requires dual licensing. CC BY-NC-SA for methods, Apache-2.0 for code.
Open-Data proof works without blockchain. IPFS + SHA256 + daily Merkle root is sufficient, cheap, and legally sound.
Next Steps
Pilot at a Montessori school in NRW (planned, start after Easter)
Legal validation by IT law expert (Inge Seher) – scheduled
IHK Bonn integration – present Safety Layer as best-practice example for EU AI Act implementation
Case study – document pilot results, refine method, publish as supplement
License of this report: CC BY-NC-SA 4.0  
Copyright: Denis Schult, 2026
