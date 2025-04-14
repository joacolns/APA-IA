from openai import OpenAI

# API Key
client = OpenAI(api_key="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")

historial = []

def es_problema_tecnico(pregunta):
    validacion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu única tarea es responder con 'sí' si la siguiente pregunta describe un problema técnico que necesita solución, o 'no' si no lo es."},
            {"role": "user", "content": pregunta}
        ]
    )
    respuesta = validacion.choices[0].message.content.strip().lower()
    return respuesta.startswith("sí")

print("Asistente Técnico (escribí 'salir' para cerrar)")

while True:
    entrada = input("Vos: ")
    if entrada.lower() in ["salir", "exit", "quit"]:
        print("Chau!")
        break

    if es_problema_tecnico(entrada):
        historial.append({"role": "user", "content": entrada})

        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Sos un asistente técnico. Tu trabajo es ayudar a resolver problemas técnicos de forma precisa, clara y útil."}] + historial
        )

        mensaje_asistente = respuesta.choices[0].message.content
        print("Asistente:", mensaje_asistente)

        historial.append({"role": "assistant", "content": mensaje_asistente})
    else:
        print("Asistente: Este asistente solo está diseñado para ayudarte con problemas técnicos.")
