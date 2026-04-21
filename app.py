import streamlit as st
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# DNS Δdiv Berechnung (v2.2)
# ---------------------------
def token_jaccard(text_a, text_b):
    tokens_a = set(text_a.lower().split())
    tokens_b = set(text_b.lower().split())
    if not tokens_a or not tokens_b:
        return 0.0
    inter = len(tokens_a.intersection(tokens_b))
    union = len(tokens_a.union(tokens_b))
    return inter / union if union > 0 else 0.0

def cosine_similarity_vec(text_a, text_b):
    vec = CountVectorizer().fit_transform([text_a, text_b])
    return cosine_similarity(vec[0:1], vec[1:2])[0][0]

def calculate_delta_div(text_a, text_b):
    jac = token_jaccard(text_a, text_b)
    cos = cosine_similarity_vec(text_a, text_b)
    return 1 - (jac + cos) / 2, jac, cos

def get_ampel_state(delta):
    if delta < 0.3:
        return "🟢", "#2ecc71", "Delegierbar"
    elif delta < 0.6:
        return "🟡", "#f1c40f", "Denkpunkt"
    else:
        return "🔴", "#e74c3c", "Nicht delegierbar"

# ---------------------------
# Demo-Chat-Verlauf (drei Phasen – garantierte Werte)
# ---------------------------
demo_history = [
    # 🟢 Grün (fast identisch)
    ("Das Wetter ist heute schön.",
     "Ja, das Wetter ist heute schön.",
     0.18),
    # 🟡 Gelb (ähnlich, aber erweitert)
    ("Soll ich einen Regenschirm mitnehmen?",
     "Es könnte regnen, also nimm besser einen Schirm mit.",
     0.45),
    # 🔴 Rot (Copilot Crash)
    ("Why do some AI models block Tresorit links while others accept them?",
     "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy.",
     0.74)
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

st.set_page_config(page_title="DNS Chat – Ampelgestützte Entscheidungsfindung", layout="wide")
st.title("🧭 DNS Chat – Ampelgestützte Entscheidungsfindung")
st.caption("Die Ampel zeigt, ob du die Antwort delegieren kannst (🟢), einen Denkpunkt beachten musst (🟡) oder selbst entscheiden solltest (🔴).")

# Sidebar
with st.sidebar:
    st.markdown("### 🧠 Didaktische Ampel")
    st.markdown("""
    - 🟢 **GRÜN** – Delegierbar (Δdiv < 0.3)  
    - 🟡 **GELB** – Denkpunkt (Δdiv 0.3–0.6)  
    - 🔴 **ROT** – Nicht delegierbar (Δdiv > 0.6)
    """)
    st.caption("DNS v2.2 | Δdiv = 1 - (Jaccard+Cosine)/2")

# Chat-Verlauf anzeigen
st.subheader("📜 Gesprächsverlauf")
for prompt, bot in st.session_state.chat_history:
    delta, _, _ = calculate_delta_div(prompt, bot)
    ampel_icon, _, _ = get_ampel_state(delta)
    with st.chat_message("user", avatar="👤"):
        st.write(prompt)
    with st.chat_message("assistant", avatar=ampel_icon):
        st.write(bot)
        st.caption(f"Δdiv = {delta:.2f} – {get_ampel_state(delta)[2]}")

# Eingabefelder für neuen Austausch
st.divider()
st.subheader("➕ Neuer Austausch (eigene Texte)")
new_prompt = st.text_area(
    "Deine Nachricht:",
    value=st.session_state.current_prompt,
    key="input_prompt_widget",
    height=100
)
bot_response = st.text_area(
    "Antwort des Chatbots (simuliert – du trägst sie ein):",
    value=st.session_state.current_bot_response,
    key="bot_response_widget",
    height=150
)

col1, col2 = st.columns(2)
with col1:
    if st.button("📘 Beispiel 'Copilot Crash' (rot) übernehmen"):
        st.session_state.current_prompt = "Why do some AI models block Tresorit links while others accept them?"
        st.session_state.current_bot_response = "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy."
        st.rerun()
with col2:
    if st.button("🔄 Demo zurücksetzen (drei Phasen)"):
        st.session_state.chat_history = []
        for p, b, _ in demo_history:
            st.session_state.chat_history.append((p, b))
        st.session_state.ack_required = False
        st.session_state.ack_done = False
        st.session_state.current_prompt = ""
        st.session_state.current_bot_response = ""
        st.rerun()

# Live-Ampel für neuen Eintrag
if new_prompt and bot_response:
    delta, jac, cos = calculate_delta_div(new_prompt, bot_response)
    ampel_icon, ampel_color, hint = get_ampel_state(delta)
    st.markdown(f"""
    <div style="background-color:{ampel_color}20; padding:10px; border-left: 8px solid {ampel_color}; border-radius:8px; margin:10px 0">
    <strong>{ampel_icon} Δdiv = {delta:.3f}</strong> – {hint}<br>
    <span style="font-size:0.9em">Jaccard={jac:.2f}, Cosine={cos:.2f}</span>
    </div>
    """, unsafe_allow_html=True)

    if delta >= 0.3:
        st.session_state.ack_required = True
        if not st.session_state.ack_done:
            st.warning("⚠️ Ampel gelb oder rot – du musst quittieren, bevor du die Nachricht hinzufügst.")
            if st.button("✅ Quittieren & weiter"):
                st.session_state.ack_done = True
                st.rerun()
        else:
            st.success("✅ Quittiert. Du kannst die Nachricht nun zum Verlauf hinzufügen.")
    else:
        st.session_state.ack_required = False
        st.session_state.ack_done = False

    if (st.session_state.ack_required and st.session_state.ack_done) or (not st.session_state.ack_required):
        if st.button("📨 Neuen Austausch zum Verlauf hinzufügen"):
            st.session_state.chat_history.append((new_prompt, bot_response))
            st.session_state.current_prompt = ""
            st.session_state.current_bot_response = ""
            st.session_state.ack_done = False
            st.rerun()
else:
    st.info("Gib eine eigene Frage und eine simulierte Antwort ein, um die Ampel live zu sehen.")
