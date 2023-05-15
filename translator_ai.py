import openai
from googletrans import Translator

# Configuración de la API de OpenAI GPT-3
openai.api_key = "api_key"
model_engine = "text-davinci-002"


def traducir(texto):
    translator = Translator()
    resultado = translator.translate(texto, src='en', dest='es')
    return resultado.text

# Función para parafrasear un texto utilizando OpenAI GPT-3
def parafrasear(texto):
    prompt = "Reescribe el siguiente texto de una manera diferente: \n" + texto + "\n"
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      temperature=0.7,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    parafraseado = response.choices[0].text.strip()
    return parafraseado

# Texto de ejemplo para traducir y parafrasear
texto_ingles = "I have a cat and a dog. They are both very friendly."

# Traducción del texto a castellano
texto_castellano = traducir(texto_ingles)

# Parafraseo del texto en castellano
texto_parafraseado = parafrasear(texto_castellano)

# Evaluación del texto parafraseado utilizando OpenAI GPT-3
evaluacion = openai.Completion.create(
  engine=model_engine,
  prompt="Evalúa la siguiente oración en términos de calidad gramatical y semántica: \n" + texto_parafraseado + "\n",
  temperature=0,
  max_tokens=1,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# Resultado de la evaluación
resultado_evaluacion = evaluacion.choices[0].text.strip()

# Impresión del resultado final
print("Texto original: ", texto_ingles)
print("Traducción: ", texto_castellano)
print("Parafraseo: ", texto_parafraseado)
print("Evaluación: ", resultado_evaluacion)