# 06b_power_layer.md – Power Layer Analysis (P6b)

**Run:** dns_v2.1_cognitive_safety  
**Date:** 2026-04-18  

## Purpose

The Power Layer (P6b) is a meta‑filter that asks: Who controls the technology? Who has access? Who profits? Who bears the risks? It is applied to every core synthesis claim to surface structural asymmetries that might otherwise remain invisible.

This analysis follows the same structure as the Labour Market 2030 case study.

---

## 1. Who controls the technology?

| Aspect | Assessment |
|--------|------------|
| **Code** | Open source (Apache‑2.0). No vendor lock‑in. |
| **Method** | CC BY‑NC‑SA 4.0 – free for education and research, non‑commercial. |
| **Model dependencies** | DNS uses freely accessible LLMs (ChatGPT free tier, Claude, Gemini, DeepSeek, Grok, Copilot). No API keys required for basic use. |
| **Data** | No data is stored centrally. Audit trails are local (IPFS hashes optional). |

**Conclusion:** The technology is controlled by the user (operator). No central authority can revoke access or change the rules without a fork.

---

## 2. Who has access?

| Group | Access level | Barrier |
|-------|--------------|---------|
| **Schools (Germany)** | Full access via browser + laminated posters | None (free, no registration) |
| **International users** | Full access | None |
| **Neurodivergent individuals** | Full access | Requires basic literacy and ability to use a browser |
| **Commercial entities** | May use the code (Apache‑2.0) but may not commercialise the method itself (CC BY‑NC‑SA) | Legal barrier to enclosure |

**Conclusion:** Access is as low‑threshold as possible. The method is designed for universal access.

---

## 3. Who profits?

| Stakeholder | Type of profit | Notes |
|-------------|----------------|-------|
| **End users (students, researchers)** | Cognitive profit (better thinking, lower anxiety) | Primary intended beneficiary |
| **Operator (Denis Schult)** | No financial profit; reputational / academic credit | Method is open, not monetised |
| **Commercial AI providers (OpenAI, Google, etc.)** | Indirect – DNS drives usage of their free tiers | No revenue from DNS itself |
| **TÜV / IHK / ETH** | Methodological validation, potential service offerings | May adapt DNS into paid audits/training – permitted by Apache‑2.0 for code, but method remains non‑commercial |

**Conclusion:** The primary profit is epistemic and social. Financial profit is intentionally limited by the CC BY‑NC‑SA license on the method.

---

## 4. Who bears the risks?

| Risk | Who bears it? | Mitigation |
|------|---------------|------------|
| **Operator error (false synthesis)** | End user (student, researcher) | Training materials, operator checklist, falsification rules |
| **Model bias (e.g., Western alignment)** | End user | DNS documents bias explicitly (divergence map) |
| **Over‑reliance on DNS** | End user | DNS is positioned as a tool, not an autopilot |
| **Data privacy** | End user (local storage) | No data collection by design |
| **Misinterpretation of Δdiv** | End user | Clear documentation in `04_divergence_map.md` |

**Conclusion:** Risks are borne by the user, but DNS provides structural safeguards (documentation, falsification rules, operator reflection). The system itself does not collect data or impose external risks.

---

## 5. Structural asymmetries (explicitly documented)

| Asymmetry | Direction | Why it matters |
|-----------|-----------|----------------|
| **Literacy requirement** | Higher for operator | Not everyone can be an effective operator; some training is needed |
| **Language** | English / German only | Currently not localised; limits accessibility |
| **Model access** | Requires internet connection | Offline use not possible for model queries (though the method itself works offline) |
| **CC BY‑NC‑SA** | Restricts commercial use | Prevents enclosure, but may limit adoption by commercial training providers |

---

## 6. Power layer conclusion for the cognitive safety hypothesis

The hypothesis – *DNS reduces social evaluation anxiety for neurodivergent and introverted individuals* – is not neutral with respect to power:

- It empowers a group that is often structurally disadvantaged in traditional learning environments.
- It shifts control from the social evaluator (teacher, peer group) to the individual learner.
- It does not eliminate the need for social evaluation but postpones it, giving the learner time to prepare.

**This is a feature, not a bug.** The power layer makes explicit that DNS is a tool for epistemic self‑defence, not a neutral technology.

---

**Next:** [07_reflection.md](./07_reflection.md)
