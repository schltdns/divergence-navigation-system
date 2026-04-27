# frAIme
## Argumentation Drift Monitor

🟢 Topic consistency • 🟡 Idea emergence • 🔴 Verifiability • 🔵 Understandability

https://doi.org/10.5281/zenodo.19793185

**frAIme makes uncertainty visible — it creates the frame for reliable AI use.**
frAIme is governance by design, not ethics by declaration.

For classrooms: four questions, traffic light, done.
For research: measurable divergence (Δdiv), auditable.

**Version:** V1.0.0 (2026-04-26) – Stable release

---

## Start here — 2 minutes
**The Four Questions Method**
Check every LLM answer:

1. On topic? 🟢 / 🔴
2. New idea? 🟢 / 🟡 / 🔴
3. Verifiable? (number, date, place, if-then) 🟢 / 🔴
4. Understandable? 👍 / 👎

Good answer = 🟢 + 👍

No account. No API. Works on paper.

## 🚀 Live Demo
👉 https://divergence-navigation-system.streamlit.app

## What's new in V1.0.0
1. **Rebranding:** formerly DNS – now frAIme
2. **Tested with Copilot Crash:** Δdiv = 0.742 exposed invented narrative
3. **Live Δdiv tracking**
4. **Traction:** 3,270 clones / 1,126 unique cloners in 14 days

## New Case Study: AI Learning vs Frontal Teaching
**Replaces EU AI Act section – real-world education use**

- **6 models, same question:** "Is AI learning more efficient?"
- **Four Questions:** all 🟢 on topic, all 👍 understandable – apparent consensus
- **Δdiv matrix:** 0.584–0.759 – high divergence despite agreement
- **Triangulation:**
    - Harvard RCT 2025 (n=194): median 4.5 vs 3.5, time 49 vs 60 min – CONFIRMED
    - Turkey UPenn 2024 (n=1,000): +48% drills / −17% test – CONFIRMED
    - Kulik & Fletcher 2016: +0.66 SD – CONFIRMED
- **Insight:** High Δdiv signaled not "wrong" but "source-poor". Only Meta cluster provided primary data.

**frAIme lesson:** Plausibility ≠ evidence. Δdiv locates verification need.

## Technical
Δdiv = 0.5·(1−Jaccard) + 0.5·(1−Cosine)

Thresholds:
- <0.3 = convergence
- 0.3–0.5 = drift
- 0.5–0.7 = high risk
- >0.7 = contested

Two layers: Frontend (Four Questions) + Backend (Safety Layer, hash anchors, multi-agent log)
