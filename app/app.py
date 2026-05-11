import streamlit as st
import spacy
import numpy as np
import pandas as pd
import os
os.system("python -m spacy download de_core_news_sm")
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# ── 🧠 Modelle cachen (lädt nur einmal) ─────────────────────────────────────
@st.cache_resource
def load_nlp():
    return spacy.load("de_core_news_sm")

@st.cache_resource
def load_embed_model():
    return SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

nlp = load_nlp()
embed_model = load_embed_model()

# ── 📐 Δdiv-Backend ─────────────────────────────────────────────────────────
def extract_concepts(text):
    """Extrahiert Noun-Phrases + Lemmatisierte Nomen"""
    doc = nlp(text)
    concepts = set()
    for chunk in doc.noun_chunks:
        concepts.add(chunk.text.lower().strip())
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            concepts.add(token.lemma_.lower())
    return concepts

def jaccard_sim(set_a, set_b):
    if not set_a and not set_b: return 1.0
    return len(set_a & set_b) / len(set_a | set_b)

def cosine_sim(t1, t2):
    e1, e2 = embed_model.encode([t1, t2])
    return cosine_similarity([e1], [e2])[0][0]

def calculate_drift(t1, t2):
    j = jaccard_sim(extract_concepts(t1), extract_concepts(t2))
    c = cosine_sim(t1, t2)
    return max(0.0, min(1.0, 1 - (j + c) / 2))

# ── 🎨 Design & CSS ─────────────────────────────────────────────────────────
st.set_page_config(page_title="frAIme", page_icon="🎯", layout="wide", initial_sidebar_state="collapsed")

SVG_LOGO = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 170" style="background:transparent; max-width:360px; margin:0 auto; display:block;">
<style>.mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; } .sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, sans-serif; }</style>
<g transform="translate(10,10)">
 <rect x="0" y="0" width="148" height="148" rx="8" fill="none" stroke="#185FA5" stroke-width="2"/>
 <g transform="translate(16,20)">
  <text x="0" y="14" font-size="10" fill="#C2C0B6" class="mono">topic?</text>
  <circle cx="100" cy="10" r="5" fill="#1D9E75"/>
  <line x1="0" y1="24" x2="116" y2="24" stroke="#DEDCD1" stroke-opacity="0.15" stroke-width="0.5"/>
  <text x="0" y="44" font-size="10" fill="#C2C0B6" class="mono">new idea?</text>
  <circle cx="88" cy="40" r="5" fill="#EF9F27"/>
  <circle cx="100" cy="40" r="5" fill="#EF9F27" opacity="0.35"/>
  <circle cx="112" cy="40" r="5" fill="#E24B4A" opacity="0.2"/>
  <line x1="0" y1="54" x2="116" y2="54" stroke="#DEDCD1" stroke-opacity="0.15" stroke-width="0.5"/>
  <text x="0" y="74" font-size="10" fill="#C2C0B6" class="mono">verifiable?</text>
  <circle cx="100" cy="70" r="5" fill="#E24B4A"/>
  <line x1="0" y1="84" x2="116" y2="84" stroke="#DEDCD1" stroke-opacity="0.15" stroke-width="0.5"/>
  <text x="0" y="104" font-size="10" fill="#C2C0B6" class="mono">understandable?</text>
  <rect x="96" y="92" width="10" height="7" rx="1" fill="#185FA5"/>
  <rect x="109" y="92" width="7" height="7" rx="1" fill="#DEDCD1" fill-opacity="0.15"/>
 </g>
 <text x="170" y="78" font-size="36" font-weight="500" fill="#FAF9F5" class="mono">fr<tspan fill="#185FA5">AI</tspan>me</text>
 <text x="170" y="102" font-size="11" fill="#C2C0B6" letter-spacing="1.5" class="sans">ARGUMENTATION</text>
 <text x="170" y="118" font-size="11" fill="#C2C0B6" letter-spacing="1.5" class="sans">DRIFT MONITOR</text>
</g>
</svg>"""

st.markdown(f'<div style="padding:16px 0; text-align:center;">{SVG_LOGO}</div>', unsafe_allow_html=True)

FRAIME_CSS = """
:root { --fraime-blue:#185FA5; --fraime-green:#1D9E75; --fraime-amber:#EF9F27; --fraime-red:#E24B4A; --fraime-bg:#0F1419; --fraime-surface:#1A1F26; --fraime-text:#FAF9F5; --fraime-muted:#C2C0B6; --fraime-line:rgba(222,220,209,0.15); --radius-lg:8px; }
body { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background: var(--fraime-bg); color: var(--fraime-text); }
h1, h2, h3 { font-family: ui-monospace, monospace; font-weight: 500; letter-spacing: 0.5px; }
.subtitle { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Inter, sans-serif; color: var(--fraime-muted); letter-spacing: 1.5px; font-size: 0.85rem; text-transform: uppercase; }
.ampel-row { display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid var(--fraime-line); }
.ampel-label { color: var(--fraime-muted); font-size: 0.9rem; }
.ampel-status { display: flex; gap: 4px; }
.ampel-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--fraime-muted); opacity: 0.2; }
.ampel-dot.active { opacity: 1; }
.ampel-dot.green { background: var(--fraime-green); }
.ampel-dot.amber { background: var(--fraime-amber); }
.ampel-dot.red { background: var(--fraime-red); }
.fraime-card { background: var(--fraime-surface); border: 2px solid var(--fraime-blue); border-radius: var(--radius-lg); padding: 16px; margin: 12px 0; }
.drift-badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: var(--fraime-surface); border: 1px solid var(--fraime-line); border-radius: 4px; font-size: 0.85rem; font-family: monospace; }
.drift-badge.low { border-left: 3px solid var(--fraime-green); }
.drift-badge.medium { border-left: 3px solid var(--fraime-amber); }
.drift-badge.high { border-left: 3px solid var(--fraime-red); }
"""
st.markdown(f"<style>{FRAIME_CSS}</style>", unsafe_allow_html=True)

def drift_badge(val):
    if val < 0.15: lvl, lbl = "low", "Konsens"
    elif val < 0.35: lvl, lbl = "low", "Leichte Abweichung"
    elif val < 0.50: lvl, lbl = "medium", "Signifikante Divergenz"
    elif val < 0.70: lvl, lbl = "medium", "Quellenasymmetrie"
    else: lvl, lbl = "high", "Blinder Fleck"
    st.markdown(f'<span class="drift-badge {lvl}">Δdiv: {val:.3f} • {lbl}</span>', unsafe_allow_html=True)

# ── 🖥️ UI ───────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🧭 Vier-Fragen & Δdiv", "🧪 P3: Triangulation & Matrix"])

with tab1:
    st.markdown("### 🧭 Vier-Fragen-Check")
    topic = st.checkbox("✓ topic?", value=True)
    new_idea = st.selectbox("🟡 new idea?", ["yes", "partial", "no"], index=1)
    verifiable = st.checkbox("✓ verifiable?", value=False)
    understandable = st.checkbox("👍 understandable?", value=True)
    
    # Ampel-Preview
    t_d = '<div class="ampel-dot active green"></div>' if topic else '<div class="ampel-dot active red"></div>'
    i_d = '<div class="ampel-dot active amber"></div><div class="ampel-dot"></div><div class="ampel-dot"></div>' if new_idea=="yes" else \
          '<div class="ampel-dot active amber"></div><div class="ampel-dot amber" style="opacity:0.35"></div><div class="ampel-dot"></div>' if new_idea=="partial" else \
          '<div class="ampel-dot active amber"></div><div class="ampel-dot amber" style="opacity:0.35"></div><div class="ampel-dot red" style="opacity:0.2"></div>'
    v_d = '<div class="ampel-dot active red"></div>' if not verifiable else '<div class="ampel-dot active green"></div>'
    u_d = '<div style="display:flex;gap:2px"><div style="width:10px;height:7px;background:#185FA5;border-radius:1px"></div><div style="width:7px;height:7px;background:rgba(222,220,209,0.15);border-radius:1px"></div></div>' if understandable else '<div style="width:20px;height:7px;background:#E24B4A;border-radius:1px"></div>'
    
    st.markdown(f"""<div class="fraime-card">
      <div class="ampel-row"><span class="ampel-label">topic?</span><div class="ampel-status">{t_d}</div></div>
      <div class="ampel-row"><span class="ampel-label">new idea?</span><div class="ampel-status">{i_d}</div></div>
      <div class="ampel-row"><span class="ampel-label">verifiable?</span><div class="ampel-status">{v_d}</div></div>
      <div class="ampel-row"><span class="ampel-label">understandable?</span><div class="ampel-status">{u_d}</div></div>
    </div>""", unsafe_allow_html=True)

    st.markdown("### 📊 Δdiv berechnen (zwei Texte)")
    c1, c2 = st.columns(2)
    with c1: txt_a = st.text_area("Text A", height=100, placeholder="Modell-Output 1...")
    with c2: txt_b = st.text_area("Text B", height=100, placeholder="Modell-Output 2...")
    if txt_a and txt_b:
        with st.spinner("Berechne Δdiv..."):
            drift_badge(calculate_drift(txt_a, txt_b))

with tab2:
    st.markdown("### 🧪 P3 — Triangulate")
    st.text_area("Prompt", value="Ist KI-Lernen effizienter als Frontalunterricht?", height=60, disabled=True)
    n_models = st.number_input("Anzahl Modell-Outputs", 2, 6, 3)
    outputs = {}
    for i in range(n_models):
        outputs[f"Modell {i+1}"] = st.text_area(f"Output {i+1}", height=80, key=f"out_{i}")
        
    if st.button("▶️ Drift-Matrix berechnen", type="primary"):
        if all(v.strip() for v in outputs.values()):
            models = list(outputs.keys())
            n = len(models)
            mat = np.zeros((n, n))
            for i in range(n):
                for j in range(i+1, n):
                    d = calculate_drift(outputs[models[i]], outputs[models[j]])
                    mat[i,j] = mat[j,i] = round(d, 3)
            df = pd.DataFrame(mat, index=models, columns=models)
            st.markdown("### 📉 Divergenz-Matrix")
            st.dataframe(df.style.background_gradient(cmap="RdYlGn_r", vmin=0, vmax=0.8), use_container_width=True)
            st.success("✅ Matrix generiert. Werte >0.50 → P6/P6b erforderlich.")
        else:
            st.warning("⚠️ Bitte fülle alle Modell-Outputs aus.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""<div style="border-top:1px solid var(--fraime-line);padding-top:12px;color:var(--fraime-muted);font-size:0.8rem;text-align:center">
  fr<span style="color:var(--fraime-blue)">AI</span>me v1.0 • 
  <a href="https://github.com/schltdns/divergence-navigation-system" style="color:var(--fraime-blue);text-decoration:none">github.com/schltdns/divergence-navigation-system</a>
</div>""", unsafe_allow_html=True)
