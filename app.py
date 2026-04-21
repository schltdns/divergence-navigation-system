import streamlit as st
import hashlib
import json
import zipfile
from io import BytesIO
from datetime import datetime
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from difflib import SequenceMatcher

# ---------------------------
# Δdiv nach DNS v2.2
# ---------------------------
def extract_concepts(text):
    words = re.findall(r'\b[A-Z][a-z]+\b|\b[a-z]{4,}\b', text)
    stopwords = {'the', 'and', 'for', 'with', 'this', 'that', 'are', 'was', 'were', 'from', 'have', 'has', 'but', 'not', 'you', 'they'}
    return set(w.lower() for w in words if w.lower() not in stopwords and len(w) > 2)

def jaccard_semantic(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    inter = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return inter / union if union > 0 else 0.0

def cosine_semantic(text_a, text_b):
    vec = CountVectorizer().fit_transform([text_a, text_b])
    return cosine_similarity(vec[0:1], vec[1:2])[0][0]

def calculate_delta_div(text_a, text_b):
    concepts_a = extract_concepts(text_a)
    concepts_b = extract_concepts(text_b)
    jac = jaccard_semantic(concepts_a, concepts_b)
    cos = cosine_semantic(text_a, text_b)
    return 1 - (jac + cos) / 2, jac, cos

def highlight_diff(text_a, text_b):
    words_a, words_b = text_a.split(), text_b.split()
    matcher = SequenceMatcher(None, words_a, words_b)
    highlighted_a, highlighted_b = [], []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for w in words_a[i1:i2]:
                highlighted_a.append(f'<span style="background-color:#c8e6c9">{w}</span>')
            for w in words_b[j1:j2]:
                highlighted_b.append(f'<span style="background-color:#c8e6c9">{w}</span>')
        else:
            for w in words_a[i1:i2]:
                highlighted_a.append(f'<span style="background-color:#ffcdd2">{w}</span>')
            for w in words_b[j1:j2]:
                highlighted_b.append(f'<span style="background-color:#ffcdd2">{w}</span>')
    return ' '.join(highlighted_a), ' '.join(highlighted_b)

# ---------------------------
# Session State
# ---------------------------
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'artifacts' not in st.session_state:
    st.session_state.artifacts = {}
if 'model_outputs' not in st.session_state:
    st.session_state.model_outputs = {
        "S1": "", "S2": "", "S3": "", "S4a": "", "S4b": "", "F1": "", "Ω": ""
    }
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""

def next_step():
    st.session_state.step += 1
def prev_step():
    st.session_state.step -= 1

st.set_page_config(page_title="DNS v2.2 – Divergence Navigation System", layout="wide")
st.title("🧭 DNS v2.2 – Divergence Navigation System")
st.caption("Reproducible, auditable workflow for epistemic analysis (P1–P8)")

# ---------------------------
# Sidebar with thresholds (optional, can be fixed)
# ---------------------------
with st.sidebar:
    st.header("Thresholds (DNS v2.2)")
    conv = st.number_input("Convergence (<)", value=0.3, step=0.05)
    prod_low = st.number_input("Productive friction (lower)", value=0.3, step=0.05)
    prod_high = st.number_input("Productive friction (upper)", value=0.6, step=0.05)
    blind = st.number_input("Epistemic blind spot (>)", value=0.7, step=0.05)
    st.divider()
    st.caption("Based on: 0.5*(1-Jaccard_sem) + 0.5*(1-Cosine)")

# ---------------------------
# P1 – Hypothesize
# ---------------------------
if st.session_state.step == 1:
    st.header("P1 — Hypothesize")
    with st.form("p1"):
        question = st.text_area("Falsifiable question", height=100)
        scope = st.text_area("Scope / assumptions", height=100)
        domain = st.selectbox("Domain", ["Formal", "Applied", "Complex"])
        expected_delta = st.slider("Expected Δdiv", 0.0, 1.0, 0.3)
        submitted = st.form_submit_button("Save & continue")
        if submitted:
            content = f"# 01_hypothesis.md\n\n**Question:** {question}\n\n**Scope:** {scope}\n\n**Domain:** {domain}\n\n**Expected Δdiv:** {expected_delta}\n"
            st.session_state.artifacts["01_hypothesis.md"] = content
            next_step()
            st.rerun()

# ---------------------------
# P2 – Thresholds
# ---------------------------
elif st.session_state.step == 2:
    st.header("P2 — Thresholds")
    with st.form("p2"):
        st.write("Using sidebar values – you can override here:")
        conv2 = st.number_input("Convergence (<)", value=conv, step=0.05)
        prod_low2 = st.number_input("Productive friction (lower)", value=prod_low, step=0.05)
        prod_high2 = st.number_input("Productive friction (upper)", value=prod_high, step=0.05)
        blind2 = st.number_input("Epistemic blind spot (>)", value=blind, step=0.05)
        contradiction = st.checkbox("Enable contradiction flags")
        submitted = st.form_submit_button("Save & continue")
        if submitted:
            content = f"""# 02_thresholds.md

**Δdiv thresholds:**
- Convergence: < {conv2}
- Productive friction: {prod_low2} – {prod_high2}
- Epistemic blind spot: > {blind2}

**Additional flags:** Contradiction = {contradiction}
"""
            st.session_state.artifacts["02_thresholds.md"] = content
            next_step()
            st.rerun()

# ---------------------------
# P3 – Triangulate with Demo Examples (English)
# ---------------------------
elif st.session_state.step == 3:
    st.header("P3 — Triangulate")
    st.markdown("**Demo examples (English) – copy them or use your own**")
    demo_examples = {
        "Copilot Crash (Tresorit)": {
            "prompt": "Why do some AI models block Tresorit links while others accept them?",
            "A": "Access to Tresorit links is technically possible because the sandbox accepts normal HTTP downloads and ZIP folders. The blocking in some models is due to missing JavaScript execution in their specific test environment.",
            "B": "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy. Western models are inherently more compatible with zero-knowledge encryption."
        },
        "LLMs for strategic decisions": {
            "prompt": "Should companies use LLMs for strategic decisions?",
            "A": "Yes, LLMs increase efficiency, analyze vast amounts of data, and detect patterns humans miss. With clear guidelines, the risk is manageable.",
            "B": "No, LLMs lack accountability. Strategic decisions require liability, ethical judgment, and context that an LLM cannot provide. Human decision authority is essential."
        },
        "Climate policy: Meat tax": {
            "prompt": "Should the state tax meat consumption?",
            "A": "A tax efficiently changes behavior, reduces emissions and health costs. Compensation for low-income households is possible.",
            "B": "A tax is paternalistic, hits poorer households harder, and reduces acceptance. Education and subsidies for alternatives are better."
        }
    }
    chosen = st.selectbox("Load example", ["None"] + list(demo_examples.keys()))
    if chosen != "None":
        st.session_state.prompt = demo_examples[chosen]["prompt"]
        st.session_state.model_outputs["S1"] = demo_examples[chosen]["A"]
        st.session_state.model_outputs["Ω"] = demo_examples[chosen]["B"]
        # Optionally fill other models with empty or same
        for m in ["S2","S3","S4a","S4b","F1"]:
            if st.session_state.model_outputs[m] == "":
                st.session_state.model_outputs[m] = "(not used)"
        st.rerun()
    prompt = st.text_area("Identical prompt for all models (S1–Ω)", height=100, value=st.session_state.prompt)
    st.session_state.prompt = prompt
    st.markdown("### Model outputs (no cross-contamination)")
    cols = st.columns(3)
    models = ["S1", "S2", "S3", "S4a", "S4b", "F1", "Ω"]
    for i, m in enumerate(models):
        with cols[i % 3]:
            st.session_state.model_outputs[m] = st.text_area(m, value=st.session_state.model_outputs[m], height=200)
    if st.button("Save outputs & continue"):
        for m, out in st.session_state.model_outputs.items():
            filename = f"03_outputs/{m}.md"
            content = f"# {m} Output\n\n**Prompt:** {prompt}\n\n**Answer:**\n{out}"
            st.session_state.artifacts[filename] = content
        next_step()
        st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P4 – Map Divergence (with visual diff)
# ---------------------------
elif st.session_state.step == 4:
    st.header("P4 — Map Divergence")
    text_a = st.session_state.model_outputs.get("S1", "")
    text_b = st.session_state.model_outputs.get("Ω", "")
    if text_a and text_b:
        delta, jac, cos = calculate_delta_div(text_a, text_b)
        st.metric("Δdiv (S1 ↔ Ω)", f"{delta:.3f}")
        st.write(f"Jaccard_sem: {jac:.3f}, Cosine: {cos:.3f}")
        # Traffic light
        if delta < conv:
            st.success("🟢 CONVERGENCE – delegable")
        elif delta < prod_high:
            st.warning("🟡 PRODUCTIVE FRICTION – human check recommended")
        else:
            st.error("🔴 EPISTEMIC BLIND SPOT – non‑delegable, manual override required")
        # Visual diff
        st.subheader("Visual frame comparison")
        ha, hb = highlight_diff(text_a, text_b)
        c1, c2 = st.columns(2)
        c1.markdown(f"**S1 (reference)**<br><div style='border:1px solid #ddd; padding:10px'>{ha}</div>", unsafe_allow_html=True)
        c2.markdown(f"**Ω (deviation)**<br><div style='border:1px solid #ddd; padding:10px'>{hb}</div>", unsafe_allow_html=True)
        # Graph divergence (simplified table)
        st.subheader("Graph divergence (edge weights = 1 - similarity)")
        models = list(st.session_state.model_outputs.keys())
        edges = []
        for i in range(len(models)):
            for j in range(i+1, len(models)):
                t_i = st.session_state.model_outputs[models[i]]
                t_j = st.session_state.model_outputs[models[j]]
                if t_i and t_j:
                    d, _, _ = calculate_delta_div(t_i, t_j)
                    edges.append((models[i], models[j], d))
        df = pd.DataFrame(edges, columns=["From", "To", "Δdiv"])
        st.dataframe(df)
        high = [e for e in edges if e[2] > 0.7]
        if high:
            st.warning(f"⚠️ F1 DeepSeek activation: edges >0.7 – {high}")
    else:
        st.warning("Please fill S1 and Ω in P3 first.")
    if st.button("Save divergence map & continue"):
        content = f"""# 04_divergence_map.md

**Δdiv (S1↔Ω):** {delta:.3f} (Jaccard_sem={jac:.3f}, Cosine={cos:.3f})

**Graph edges:**\n{df.to_markdown()}
"""
        st.session_state.artifacts["04_divergence_map.md"] = content
        next_step()
        st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P5 – Weighted Synthesis
# ---------------------------
elif st.session_state.step == 5:
    st.header("P5 — Weighted Synthesis")
    st.write("Assign weights to each model output (sum = 1)")
    weights = {}
    total = 0.0
    cols = st.columns(3)
    models = ["S1", "S2", "S3", "S4a", "S4b", "F1", "Ω"]
    for i, m in enumerate(models):
        with cols[i % 3]:
            w = st.slider(f"Weight {m}", 0.0, 1.0, 1.0/len(models), step=0.01)
            weights[m] = w
            total += w
    st.write(f"Sum: {total:.2f}")
    if abs(total - 1.0) > 0.01:
        st.warning("Weights should sum to 1. Adjust.")
    reasoning = st.text_area("Justification for weighting", height=150)
    if st.button("Generate synthesis & continue"):
        synth = f"# 05_synthesis.md\n\n## Weights\n{json.dumps(weights, indent=2)}\n\n## Justification\n{reasoning}\n\n## Synthesis text (to be filled manually)\n"
        st.session_state.artifacts["05_synthesis.md"] = synth
        next_step()
        st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P6 – External Validation
# ---------------------------
elif st.session_state.step == 6:
    st.header("P6 — External Validation")
    external = st.text_area("Paste external source (literature, expert, data)", height=200)
    if st.button("Compare with synthesis"):
        synth = st.session_state.artifacts.get("05_synthesis.md", "")
        if synth and external:
            d, _, _ = calculate_delta_div(synth, external)
            st.metric("Δdiv between synthesis and external source", f"{d:.3f}")
            if d < conv:
                st.success("Synthesis aligns with external source.")
            elif d < prod_high:
                st.warning("Moderate divergence – further check needed.")
            else:
                st.error("High divergence – review synthesis.")
    if st.button("Save validation & continue"):
        content = f"# 06_validation.md\n\nExternal source:\n{external}\n\n"
        st.session_state.artifacts["06_validation.md"] = content
        next_step()
        st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P6b – Power Layer Check
# ---------------------------
elif st.session_state.step == 7:
    st.header("P6b — Power Layer Check")
    with st.form("power"):
        control = st.text_area("Who controls knowledge production?")
        benefit = st.text_area("Who benefits?")
        risk = st.text_area("Who bears risk?")
        excluded = st.text_area("Who is excluded?")
        submitted = st.form_submit_button("Save & continue")
        if submitted:
            content = f"""# 06b_power_layer.md
- **Control:** {control}
- **Benefit:** {benefit}
- **Risk:** {risk}
- **Exclusion:** {excluded}
"""
            st.session_state.artifacts["06b_power_layer.md"] = content
            next_step()
            st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P7 – Operator Reflection
# ---------------------------
elif st.session_state.step == 8:
    st.header("P7 — Operator Reflection")
    load = st.slider("Cognitive load (1=low, 5=high)", 1, 5, 3)
    uncertainty = st.slider("Epistemic uncertainty (1=low, 5=high)", 1, 5, 3)
    bias = st.multiselect("Confirmation bias indicators", ["Own expectation confirmed", "Ignored alternative perspectives", "Selective quoting"])
    free_text = st.text_area("Free reflection", height=150)
    if st.button("Save reflection & continue"):
        content = f"""# 07_reflection.md
- **Load:** {load}/5
- **Uncertainty:** {uncertainty}/5
- **Bias:** {', '.join(bias)}
- **Free text:** {free_text}
"""
        st.session_state.artifacts["07_reflection.md"] = content
        next_step()
        st.rerun()
    if st.button("Back"):
        prev_step()
        st.rerun()

# ---------------------------
# P8 – Versioning & Export
# ---------------------------
elif st.session_state.step == 9:
    st.header("P8 — Versioning")
    tag = st.text_input("Version tag (e.g., dns_v2.2_run01)", value=f"dns_v2.2_{datetime.now().strftime('%Y%m%d_%H%M')}")
    if st.button("Archive all artifacts and download"):
        manifest = {
            "dns_version": "v2.2",
            "release_date": datetime.utcnow().isoformat() + "Z",
            "version_tag": tag,
            "files": {}
        }
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            for filename, content in st.session_state.artifacts.items():
                sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
                manifest["files"][filename] = {"sha256": sha}
                zf.writestr(filename, content)
            manifest_str = json.dumps(manifest, indent=2)
            zf.writestr("08_manifest.json", manifest_str)
        zip_buffer.seek(0)
        st.download_button("📦 Download ZIP archive", data=zip_buffer, file_name=f"{tag}_dns_artifacts.zip", mime="application/zip")
        st.success("Artifacts packaged. You can upload to IPFS / Zenodo.")
    if st.button("Back to P7"):
        prev_step()
        st.rerun()
else:
    st.write("Workflow complete. Download your archive.")
