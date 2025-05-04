#GUI

import streamlit as st
from openai_handler import es_tema_valido, obtener_respuesta, temas_permitidos

st.set_page_config(page_title="Asistente Técnico", page_icon="🛠️", layout="centered")
st.title("🛠️ Asistente Técnico")

# Historial de conversación
if "historial" not in st.session_state:
    st.session_state.historial = []

# Función para registrar la conversación en un archivo log.txt
def registrar_en_log(mensaje):
    try:
        # Abre el archivo en modo de anexado, lo crea si no existe
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(mensaje + "\n")
    except Exception as e:
        print(f"Error al escribir en log.txt: {e}")

# Formulario de entrada
with st.form(key="chat_form"):
    user_input = st.text_input("Escribí tu pregunta técnica:")
    enviar = st.form_submit_button("Enviar")

if enviar and user_input:
    if es_tema_valido(user_input):
        st.session_state.historial.append({"role": "user", "content": user_input})
        registrar_en_log(f"Usuario: {user_input}")
        
        respuesta = obtener_respuesta(st.session_state.historial)
        st.session_state.historial.append({"role": "assistant", "content": respuesta})
        registrar_en_log(f"Asistente: {respuesta}")
    else:
        mensaje_error = "Este asistente solo puede ayudarte con temas técnicos de hardware y sistemas operativos como Windows, Mac o Linux."
        st.session_state.historial.append({"role": "assistant", "content": mensaje_error})
        registrar_en_log(f"Asistente: {mensaje_error}")

#Procesamiento de la pregunta

for mensaje in st.session_state.historial:
    if mensaje["role"] == "user":
        st.markdown(f"**👤 Usuario:** {mensaje['content']}")
    else:
        st.markdown(f"**🤖 Asistente:** {mensaje['content']}")

st.markdown("---")
st.caption("Preguntas válidas: " + ", ".join(temas_permitidos))
