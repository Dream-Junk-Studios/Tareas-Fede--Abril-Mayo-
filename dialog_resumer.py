import openai
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict


openai.api_key = "API_KEY"

# Función para identificar los temas principales utilizando la API de OpenAI
def get_topics(dialogue):
    response = openai.Completion.create(
        engine="davinci", 
        prompt="Identify the main topics in the following dialogue: " + dialogue,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    topic = response.choices[0].text.strip()
    return topic


dialogues = ["Diálogo 1", "Diálogo 2", "Diálogo 3"]

# Crea un diccionario para almacenar las oraciones relevantes de cada diálogo
dialogue_summaries = defaultdict(list)

# Preprocesamos los datos
stop_words = set(stopwords.words('spanish'))

for dialogue in dialogues:
    # Identifica los temas principales utilizando la API de OpenAI
    topics = get_topics(dialogue)
    # Tokeniza las oraciones
    sentences = sent_tokenize(dialogue.lower())
    for sentence in sentences:
        # Tokeniza las palabras de la oración y elimina las palabras vacías y los signos de puntuación
        words = [word for word in word_tokenize(sentence) if word.isalnum() and word not in stop_words]
        for topic in topics:
            if topic.lower() in sentence.lower():
                # Si la oración contiene uno de los temas principales, la agregam al resumen del diálogo correspondiente
                dialogue_summaries[dialogue].append(sentence)

# Genera el resumen de cada diálogo
for dialogue, sentences in dialogue_summaries.items():
    print("Resumen del diálogo:")
    print(" ".join(sentences))
