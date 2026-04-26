import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------------------------
# Semantische Ähnlichkeit (längenunempfindlich)
# ---------------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def semantic_similarity(text_a, text_b):
    emb_a = model.encode([text_a])[0]
    emb_b = model.encode([text_b])[0]
    sim = np.dot(emb_a, emb_b) / (np.linalg.norm(emb_a) * np.linalg.norm(emb_b))
    return float(sim)

def calculate_delta_div(text_a, text_b):
    cos = semantic_similarity(text_a, text_b)
    delta = 1 - cos
    return delta, 0.0, cos

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢", "#2ecc71", "Delegierbar"
    elif delta < 0.6:
        return "🟡", "#f1c40f", "Denkpunkt"
    else:
        return "🔴", "#e74c3c", "Nicht delegierbar"

# ---------------------------
# Demo-Chat-Verlauf
# ---------------------------
demo_history = [
    ("Das Wetter ist heute schön.",
     "Ja, das Wetter ist heute schön.",
     None),
    ("Soll ich einen Regenschirm mitnehmen?",
     "Es könnte regnen, also nimm besser einen Schirm mit.",
     None),
    ("Why do some AI models block Tresorit links while others accept them?",
     "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy.",
     None)
]

# Session State
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    for prompt, bot, _ in demo_history:
        st.session_state.chat_history.append((prompt, bot))
if 'ack_required' not in st.session_state:
    st.session_state.ack_required = False
if 'ack_done' not in st.session_state:
    st.session_state.ack_done = False
if 'current_prompt' not in st.session_state:
    st.session_state.current_prompt = ""
if 'current_bot_response' not in st.session_state:
    st.session_state.current_bot_response = ""

st.set_page_config(page_title="DNS Chat – Semantische Ampel", layout="wide")
st.title("🧭 DNS Chat – Semantische Ampel (längenunempfindlich)")
st.caption("Die Ampel misst semantische Divergenz – auch bei langen Antworten auf kurze Fragen korrekt.")

with st.sidebar:
    st.markdown("### 🧠 Didaktische Ampel")
    st.markdown("""
    - 🟢 **GRÜN** – Delegierbar (Δdiv < 0.3)  
    - 🟡 **GELB** – Denkpunkt (Δdiv 0.3–0.6)  
    - 🔴 **ROT** – Nicht delegierbar (Δdiv > 0.6)
    """)
    st.caption("DNS v2.2 | Δdiv = 1 - Cosine(Semantic)")

# Chat-Verlauf
st.subheader("📜 Gesprächsverlauf")
for prompt, bot in st.session_state.chat_history:
    delta, _, _ = calculate_delta_div(prompt, bot)
    ampel_icon, _, _ = get_ampel_state(delta)
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    with st.chat_message("assistant", avatar=ampel_icon):
        st.write(bot)
        st.caption(f"Δdiv = {delta:.2f} – {get_ampel_state(delta)[2]}")

# Eigene Texte
st.divider()
st.subheader("➕ Neuer Austausch (eigene Texte)")
new_prompt = st.text_area("Deine Nachricht:", value=st.session_state.current_prompt, key="input_prompt_widget", height=100)
bot_response = st.text_area("Antwort des Chatbots (simuliert):", value=st.session_state.current_bot_response, key="bot_response_widget", height=150)

col1, col2 = st.columns(2)
with col1:
    if st.button("📘 Beispiel 'Copilot Crash' (rot)"):
        st.session_state.current_prompt = "Why do some AI models block Tresorit links while others accept them?"
        st.session_state.current_bot_response = "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy."
        st.rerun()
with col2:
    if st.button("🔄 Demo zurücksetzen (drei Phasen)"):
        st.session_state.chat_history = []
        for p, b, _ in demo_history:
            st.session_state.chat_history.append((p, b))
        st.session_state.current_prompt = ""
        st.session_state.current_bot_response = ""
        st.session_state.ack_required = False
        st.session_state.ack_done = False
        st.rerun()

if new_prompt and bot_response:
    delta, _, cos = calculate_delta_div(new_prompt, bot_response)
    ampel_icon, ampel_color, hint = get_ampel_state(delta)
    st.markdown(f"""
    <div style="background-color:{ampel_color}20; padding:10px; border-left: 8px solid {ampel_color}; border-radius:8px; margin:10px 0">
    <strong>{ampel_icon} Δdiv = {delta:.3f}</strong> – {hint}<br>
    <span style="font-size:0.9em">Cosine = {cos:.2f}</span>
    </div>
    """, unsafe_allow_html=True)

    if delta >= 0.3:
        st.session_state.ack_required = True
        if not st.session_state.ack_done:
            st.warning("⚠️ Ampel gelb oder rot – du musst quittieren.")
            if st.button("✅ Quittieren & weiter"):
                st.session_state.ack_done = True
                st.rerun()
        else:
            st.success("✅ Quittiert. Du kannst die Nachricht hinzufügen.")
    else:
        st.session_state.ack_required = False
        st.session_state.ack_done = False

    if (st.session_state.ack_required and st.session_state.ack_done) or (not st.session_state.ack_required):
        if st.button("📨 Zum Verlauf hinzufügen"):
            st.session_state.chat_history.append((new_prompt, bot_response))
            st.session_state.current_prompt = ""
            st.session_state.current_bot_response = ""
            st.session_state.ack_done = False
            st.rerun()
else:
    st.info("Gib eine Frage und eine Antwort ein – die Ampel zeigt sofort die semantische Divergenz.")
