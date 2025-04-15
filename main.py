from openai import OpenAI

client = OpenAI(api_key="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")

historial = []

def es_problema_tecnico(pregunta):
    validacion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu tarea es evaluar si la pregunta se refiere a un tema técnico general. Si es así, responde 'sí'. Si no, responde 'no'. Por ejemplo, preguntas como '¿qué es un PCB?' o '¿cómo funciona una red eléctrica?' son técnicas."},
            {"role": "user", "content": pregunta}
        ]
    )
    respuesta = validacion.choices[0].message.content.strip().lower()
    return respuesta.startswith("sí")

print("Asistente Técnico (escribí 'salir' para cerrar)")

while True:
    entrada = input("User: ")
    if entrada.lower() in ["salir", "exit", "quit"]:
        print("Chau!")
        break

    if es_problema_tecnico(entrada):
        historial.append({"role": "user", "content": entrada})

        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Sos un asistente técnico. Tu trabajo es ayudar a resolver problemas técnicos de forma precisa, clara y útil. Respuestas que no sean largas y no gastes muchos tokens"}] + historial
        )

        mensaje_asistente = respuesta.choices[0].message.content
        print("Asistente:", mensaje_asistente)

        historial.append({"role": "assistant", "content": mensaje_asistente})
    else:
        print("Asistente: Este asistente solo está diseñado para ayudarte con problemas técnicos.")
