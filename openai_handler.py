#Carga de dependencias
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

#Carga de la API
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#Carga los temos del JSON
def cargar_temas_permitidos():
    with open("temas_permitidos.json", "r") as f:
        data = json.load(f)
    return data["temas"]

temas_permitidos = cargar_temas_permitidos()

#Funcion para validar si la pregunta está relacionada con los temas permitidos
def es_tema_valido(pregunta):
    prompt = f"""
Solo respondé 'sí' o 'no'. La siguiente pregunta está relacionada con uno de estos temas: {', '.join(temas_permitidos)}?

#Validación y obtención de la respuesta
Pregunta: {pregunta}
"""
    validacion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sos un evaluador de temas. Respondé únicamente 'sí' o 'no' según si la pregunta está relacionada con los temas listados."},
            {"role": "user", "content": prompt}
        ]
    )
    respuesta = validacion.choices[0].message.content.strip().lower()
    return respuesta.startswith("sí")

def obtener_respuesta(historial):
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Sos un asistente de soporte técnico. Solo respondé preguntas sobre hardware de PC, Windows, Mac o Linux. Sé preciso, útil y directo, sin extenderte demasiado."}
        ] + historial
    )
    return respuesta.choices[0].message.content
