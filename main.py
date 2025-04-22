import streamlit as st
from openai_handler import es_tema_valido, obtener_respuesta, temas_permitidos

st.set_page_config(page_title="Asistente Técnico", page_icon="🛠️", layout="centered")
st.title("🛠️ Asistente Técnico")

if "historial" not in st.session_state:
    st.session_state.historial = []

with st.form(key="chat_form"):
    user_input = st.text_input("Escribí tu pregunta técnica:")
    enviar = st.form_submit_button("Enviar")

if enviar and user_input:
    if es_tema_valido(user_input):
        st.session_state.historial.append({"role": "user", "content": user_input})
        respuesta = obtener_respuesta(st.session_state.historial)
        st.session_state.historial.append({"role": "assistant", "content": respuesta})
    else:
        st.session_state.historial.append({
            "role": "assistant",
            "content": "Este asistente solo puede ayudarte con temas técnicos de hardware y sistemas operativos como Windows, Mac o Linux."
        })

# Mostrar historial
for mensaje in st.session_state.historial:
    if mensaje["role"] == "user":
        st.markdown(f"**👤 Usuario:** {mensaje['content']}")
    else:
        st.markdown(f"**🤖 Asistente:** {mensaje['content']}")

st.markdown("---")
st.caption("Preguntas válidas: " + ", ".join(temas_permitidos))
