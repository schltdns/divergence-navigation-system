# 05 – External Validation

This file documents the **empirical grounding** of the TNS synthesis. Model outputs were systematically checked against independent, publicly available sources. Any claim that contradicted these sources was **discarded or marked as uncertain**.

---

## 1. Sources Used

| Source | Full Name / Report | Focus Areas | Access |
|--------|-------------------|-------------|--------|
| **IAB** | Institut für Arbeitsmarkt- und Berufsforschung – Forschungsbericht 23|2025 | Task shift, net employment effects, productivity potential (Germany) | Free |
| **WEF** | World Economic Forum – Future of Jobs Report 2025 | Global job creation/destruction, skill shifts, AI adoption | Free |
| **IW Köln** | Institut der deutschen Wirtschaft – 2025 Prognosen | Productivity growth, skills shortage (Germany) | Free summary |
| **McKinsey** | McKinsey Global Institute – 2025 Europe reports | Automation potential (% of hours), job changes | Free summary |
| **BAuA** | Bundesanstalt für Arbeitsschutz und Arbeitsmedizin – 2025 study | Mental health, work intensity, gender effects | Free |

---

## 2. Validation Protocol (Three Levels)

For each core claim, we applied a three‑level check:

| Level | Question | Method | Example |
|-------|----------|--------|---------|
| **1 – Fact** | Do the numbers / trends match aggregated statistics? | Compare model output to source tables | "30% of hours automatable" → McKinsey 2025: 27–30% → **confirmed** |
| **2 – Causality** | Is the causal mechanism supported by research? | Compare model explanation to meta‑studies | "AI shifts income from labour to capital" → IAB/IW: consistent with factor share trends → **plausible** |
| **3 – Robustness** | Does the claim hold under alternative assumptions? | Sensitivity analysis (slow vs. fast adoption scenarios) | "Net job balance positive" → holds in IAB baseline, but not in pessimistic scenario → **conditional** |

---

## 3. Key Validated Claims (with Sources)

| Claim | Model Support | Source | Level 1 (Fact) | Level 2 (Causality) | Level 3 (Robustness) | Verdict |
|-------|---------------|--------|----------------|---------------------|----------------------|---------|
| 20–40% of tasks transformed by 2030 | All models | IAB, McKinsey | ✅ (IAB: 1.6M jobs affected; McKinsey: 27–30% hours) | ✅ (task‑based approach confirmed) | ✅ (bandwidth covers slow/fast) | **Validated** |
| Net employment stable, but up to 3M job changes in DE | Claude, Grok, Copilot | IAB, WEF | ✅ (IAB: net ±0 over 15 years) | ✅ (reallocation not net loss) | ✅ (holds under most scenarios) | **Validated** |
| Wage dispersion increases | All models | IW, OECD | ✅ (trend data) | ✅ (skill‑biased technical change) | ⚠️ (could be offset by policy) | **Validated with caveat** |
| 59–63% need reskilling by 2030 | DeepSeek, Grok | WEF, IAB | ✅ (WEF: 59% core skills change) | ✅ (task shift drives demand) | ✅ (range accounts for uncertainty) | **Validated** |
| AI adds 0.3–1.2% to GDP growth | ChatGPT, DeepSeek, Copilot | IAB, IW | ✅ (IAB: up to +0.8pp; IW: 0.9–1.2%) | ✅ (productivity channel) | ⚠️ (depends on adoption) | **Validated as potential** |
| Dual training is an advantage if modernised | All models | IW, OECD | ✅ (lower youth unemployment in DACH) | ✅ (practice‑theory link) | ✅ (conditional statement) | **Validated conditional** |
| Mental health risks from acceleration | Claude, DeepSeek, Grok | BAuA 2025 | ✅ (higher work intensity reported) | ⚠️ (causality not fully isolated) | ⚠️ (other factors like pandemic) | **Plausible, not proven** |

✅ = confirmed / ⚠️ = partial or conditional / ❌ = contradicted (none in this case study)

---

## 4. Claims That Were Discarded or Marked Uncertain

| Claim | Model(s) | Contradicting Source | Reason for Discarding |
|-------|----------|----------------------|----------------------|
| "Massive net job loss due to AI" | None explicitly, but a pessimistic scenario | IAB, WEF (both show net stability) | Direct contradiction of empirical forecasts |
| "AI fully solves skills shortage" | None explicitly, but some optimistic tones | IW (still 3.1M shortage by 2030) | Demographics dominate; AI only alleviates |
| "Basic income will be implemented by 2030" | Mentioned as possibility | No empirical source; political consensus absent | Speculative, not falsifiable within horizon |

---

## 5. How to Use This Validation in Your Own Work

- **For researchers:** Replicate the three‑level check with updated data (2027, 2028, 2030) to see which claims hold.
- **For practitioners:** Use the “Validated” claims as robust grounding for strategy or policy decisions. Treat “Validated with caveat” as likely but conditional. Treat “Plausible, not proven” as needing local assessment.
- **For method developers:** The validation protocol (Levels 1–3) is part of the TNS standard. It can be applied to any case study.

---

## 6. Limitations of This Validation

- **Temporal:** Data as of 2025/2026. Future revisions may change verdicts.
- **Geographic:** Mostly Germany/EU. Some claims (e.g., WEF global) may not fully apply locally.
- **Selection bias:** Only claims that could be checked against available sources are included. Some nuanced model statements remain unvalidated.
- **Causality:** Level 2 checks are often based on meta‑consensus, not randomised controlled trials.

---

**Next file:** `06_power_layer.md` (Access, control, profit, and risk distribution)
