import streamlit as st

# Page Config
st.set_page_config(
    page_title="frAIme",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS laden
with open("assets/fraime_theme.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Header (Logo-Stil) ─────────────────────────────
def fraime_header():
    st.markdown("""
    <div style="display:flex;align-items:center;gap:16px;padding:12px 0">
      <div style="border:2px solid #185FA5;border-radius:8px;padding:8px 12px">
        <span style="font-family:monospace;font-size:1.5rem;font-weight:500">
          fr<span style="color:#185FA5">AI</span>me
        </span>
      </div>
      <div>
        <div class="subtitle">ARGUMENTATION</div>
        <div class="subtitle">DRIFT MONITOR</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

fraime_header()

# ── Vier-Fragen-Ampel Component ───────────────────
def vier_fragen_ampel(topic=True, new_idea="partial", verifiable=False, understandable=True):
    topic_dot = '<div class="ampel-dot active green"></div>' if topic else '<div class="ampel-dot active red"></div>'
    
    if new_idea == "yes":
        idea_dots = '<div class="ampel-dot active amber"></div><div class="ampel-dot"></div><div class="ampel-dot"></div>'
    elif new_idea == "partial":
        idea_dots = '<div class="ampel-dot active amber"></div><div class="ampel-dot amber" style="opacity:0.35"></div><div class="ampel-dot"></div>'
    else:
        idea_dots = '<div class="ampel-dot active amber"></div><div class="ampel-dot amber" style="opacity:0.35"></div><div class="ampel-dot red" style="opacity:0.2"></div>'
    
    verif_dot = '<div class="ampel-dot active red"></div>' if not verifiable else '<div class="ampel-dot active green"></div>'
    
    understand_box = (
        '<div style="display:flex;gap:2px">'
        '<div style="width:10px;height:7px;background:#185FA5;border-radius:1px"></div>'
        '<div style="width:7px;height:7px;background:rgba(222,220,209,0.15);border-radius:1px"></div>'
        '</div>'
    ) if understandable else '<div style="width:20px;height:7px;background:#E24B4A;border-radius:1px"></div>'

    st.markdown(f"""
    <div class="fraime-card">
      <div class="ampel-row"><span class="ampel-label">topic?</span><div class="ampel-status">{topic_dot}</div></div>
      <div class="ampel-row"><span class="ampel-label">new idea?</span><div class="ampel-status">{idea_dots}</div></div>
      <div class="ampel-row"><span class="ampel-label">verifiable?</span><div class="ampel-status">{verif_dot}</div></div>
      <div class="ampel-row"><span class="ampel-label">understandable?</span><div class="ampel-status">{understand_box}</div></div>
    </div>
    """, unsafe_allow_html=True)

# ── Δdiv Badge ────────────────────────────────────
def drift_badge(value: float):
    if value < 0.15:
        level, label = "low", "Konsens"
    elif value < 0.35:
        level, label = "low", "Leichte Abweichung"
    elif value < 0.50:
        level, label = "medium", "Signifikante Divergenz"
    elif value < 0.70:
        level, label = "medium", "Quellenasymmetrie"
    else:
        level, label = "high", "Blinder Fleck"
    st.markdown(f'<span class="drift-badge {level}">Δdiv: {value:.3f} • {label}</span>', unsafe_allow_html=True)

# ── Main Content ──────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🧭 Vier-Fragen-Check")
    topic = st.checkbox("✓ topic?", value=True)
    new_idea = st.selectbox("🟡 new idea?", ["yes", "partial", "no"], index=1)
    verifiable = st.checkbox("✓ verifiable?", value=False)
    understandable = st.checkbox("👍 understandable?", value=True)
    
    vier_fragen_ampel(topic, new_idea, verifiable, understandable)
    
    st.markdown("### 📊 Δdiv / drift")
    drift_val = st.slider("Δdiv-Wert", 0.0, 1.0, 0.584, 0.001)
    drift_badge(drift_val)

with col2:
    st.markdown("### 🧪 P3 — Triangulate")
    prompt_input = st.text_area("Prompt", height=100, placeholder="Gib deinen Prompt hier ein...")
    
    if st.button("▶️ Modelle befragen", type="primary"):
        st.info("🔧 Backend-Integration folgt – hier würdest du S1–Ω aufrufen.")
        # Placeholder für spätere Δdiv-Berechnung
    
    st.markdown("### 🗂️ P1–P8 Workflow")
    step = st.radio(
        "Schritt auswählen",
        ["P1 Hypothesize", "P2 Thresholds", "P3 Triangulate", "P4 Map Divergence", 
         "P5 Synthesis", "P5b Operator Decision", "P6 Validation", "P6b Power Layer", 
         "P7 Reflection", "P8 Versioning"],
        index=3
    )
    st.markdown(f"*Output für `{step.lower().replace(' ', '_')}.md` wird hier generiert...*")

# ── Footer ────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style="border-top:1px solid var(--fraime-line);padding-top:12px;color:var(--fraime-muted);font-size:0.8rem">
  fr<span style="color:var(--fraime-blue)">AI</span>me v1.0 • 
  <a href="https://github.com/schltdns/divergence-navigation-system" style="color:var(--fraime-blue);text-decoration:none">github.com/schltdns/divergence-navigation-system</a>
</div>
""", unsafe_allow_html=True)
