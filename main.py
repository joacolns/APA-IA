from openai import OpenAI

#hardcodeado porque no se como se entrega (?)
client = OpenAI(api_key="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")

historial = []

print("Chatbot (escribí 'salir' para cerrar)")

while True:
    entrada = input("Vos: ")
    if entrada.lower() in ["salir", "exit", "quit"]:
        print("Chau!")
        break

    historial.append({"role": "user", "content": entrada})

    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historial
    )

    mensaje_asistente = respuesta.choices[0].message.content
    print("Asistente:", mensaje_asistente)

    historial.append({"role": "assistant", "content": mensaje_asistente})
