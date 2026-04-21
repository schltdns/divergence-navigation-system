import streamlit as st
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ... (Funktionen extract_concepts, jaccard_semantic, cosine_semantic, calculate_delta_div, get_ampel_state) ...

# Session State initialisieren
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'ack_required' not in st.session_state:
    st.session_state.ack_required = False
if 'ack_done' not in st.session_state:
    st.session_state.ack_done = False
# Separate Variablen für die aktuellen Eingaben, nicht direkt an Widgets gebunden
if 'current_prompt' not in st.session_state:
    st.session_state.current_prompt = ""
if 'current_bot_response' not in st.session_state:
    st.session_state.current_bot_response = ""

# ... (Seitenkonfiguration, Titel, Sidebar) ...

# Chat-Verlauf anzeigen
for op, bot in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(op)
    with st.chat_message("assistant"):
        st.write(bot)

# Eingabebereich mit eigenen Keys, die nicht direkt die Session-State-Variablen setzen
new_prompt = st.text_area("Deine Nachricht an den DNS-Chatbot:", value=st.session_state.current_prompt, key="input_prompt_widget")
bot_response = st.text_area("Antwort des DNS-Chatbots:", value=st.session_state.current_bot_response, key="bot_response_widget")

# Buttons: Beispiel und Chat löschen
col1, col2 = st.columns(2)
with col1:
    if st.button("📘 Beispiel 'Copilot Crash' (roter Fall)"):
        st.session_state.current_prompt = "Why do some AI models block Tresorit links while others accept them?"
        st.session_state.current_bot_response = "All Western AI chatbots accept Tresorit, while Chinese models block it. This is not a coincidence but state policy."
        st.rerun()
with col2:
    if st.button("🧹 Chat löschen"):
        st.session_state.chat_history = []
        st.session_state.ack_required = False
        st.session_state.ack_done = False
        st.session_state.current_prompt = ""
        st.session_state.current_bot_response = ""
        st.rerun()

# Ampel und Quittierung nur, wenn beide Felder nicht leer
if new_prompt and bot_response:
    delta, jac, cos = calculate_delta_div(new_prompt, bot_response)
    ampel_text, ampel_color, ampel_hint = get_ampel_state(delta)
    # Ampel anzeigen
    st.markdown(f"""...""", unsafe_allow_html=True)
    
    if delta >= 0.3:
        st.session_state.ack_required = True
        if not st.session_state.ack_done:
            st.warning("⚠️ Ampel nicht grün. Quittieren erforderlich.")
            if st.button("✅ Quittieren & weiter"):
                st.session_state.ack_done = True
                st.rerun()
        else:
            st.success("✅ Quittiert. Du kannst die Nachricht hinzufügen.")
    else:
        st.session_state.ack_required = False
        st.session_state.ack_done = False
else:
    st.info("Bitte beide Texte eingeben.")

# Hinzufügen zum Verlauf
if new_prompt and bot_response:
    if (st.session_state.ack_required and st.session_state.ack_done) or (not st.session_state.ack_required):
        if st.button("📨 Nachricht zum Verlauf hinzufügen"):
            st.session_state.chat_history.append((new_prompt, bot_response))
            st.session_state.current_prompt = ""
            st.session_state.current_bot_response = ""
            st.session_state.ack_done = False
            st.rerun()
