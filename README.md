# Como usar + Instalar

## 1. Clonar el repositorio

HTTPS:

` git clone https://github.com/joacolns/APA-IA.git `

SSH:

` git clone git@github.com:joacolns/APA-IA.git `

## 2. Instalar bibliotecas

**Individualmente:**

` pip install openai `

` pip install python-dotenv `

` pip install json `

` pip install streamlit `

**En conjunto:**

Ejecutar ` bib.bat `.

## 3. Setup de la API Key

Para que el programa funcione se necesita configurar la API Key de OpenAI, para hacerlo, en el mismo directorio del repositorio se tiene que crear un archivo ".env", que contenga;
` OPENAI_API_KEY=APIKEY `.

## 4. Ejecución

El programa se ejecuta en navegador via streamlit, por lo tanto para correrlo, abrir la consola en el mismo directorio de ` main.py ` y ` openai_handler.py ` y ejecutar ` streamlit run main.py `, se abrirá una pagina en localhost. Si la IA no responde nada, quiere decir que hubo un problema con la API, puede ser por falta de tokens o que la API es incorrecta.

## Manejo del JSON

El archivo ` temas_permitdos.json ` es el listado de contenido que se carga en ` openai_handler.py ` para que la API tenga contexto de que responder y que no, se puede mejorar agregando muchos temas en el mismo archivo json, siempre separando los temas con ",".

Ejemplo:

```json
{
  "temas": ["hardware", "Windows", "Linux", "Mac", "componentes", "BIOS"]
}
```

# Explicación del codigo

Este proyecto está dividido en dos partes:

## openai_handler.py

Es el archivo que maneja todo lo relacionado con la API de OpenAI:

Carga el archivo JSON con los temas permitidos.

Evalúa si la pregunta que hace el usuario está relacionada con alguno de esos temas.

Envía la conversación a la API y devuelve una respuesta técnica clara y breve.

**Funciones principales:**

es_tema_valido(pregunta) → Filtra si se puede responder.

obtener_respuesta(historial) → Consulta a GPT con el historial acumulado.

## main.py

Este archivo maneja la interfaz visual usando Streamlit:

Muestra el título y un input donde el usuario puede hacer preguntas.

Procesa cada pregunta:

Si es válida, responde con la IA.

Si no es válida, avisa al usuario.

Muestra todo el historial del chat (tanto preguntas como respuestas).

También muestra al final una nota con los temas válidos que se cargan desde el JSON.