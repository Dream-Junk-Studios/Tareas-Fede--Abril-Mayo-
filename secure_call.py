import spacy
from textblob import TextBlob
import re

def detectar_trabajo_a_escondidas(texto_chat):
    patrones = ['trabaj(o|ando) a escondidas', 'trabaj(o|ando) sin (ti|nosotros)']
    for patron in patrones:
        if re.search(patron, texto_chat, re.IGNORECASE):
            return True
    return False

# Cargar el modelo pre-entrenado de spaCy para inglés
nlp = spacy.load('en_core_web_sm')

def detectar_trabajo_equipo(texto):
    # Procesar el texto con el modelo de spaCy
    doc = nlp(texto)

    # Buscar palabras clave relacionadas con trabajar en equipo o por su cuenta
    equipo = ["trabajo en equipo", "colaboración", "cooperación", "trabajar juntos", "trabajar en grupo", "equipo de trabajo", "trabajo colaborativo"]
    individual = ["trabajo individual", "trabajar solo", "trabajo autónomo", "trabajar por cuenta propia", "trabajo independiente"]

    # Inicializar contadores
    equipo_count = 0
    individual_count = 0

    # Contar la frecuencia de ocurrencia de palabras clave en el texto
    for token in doc:
        if token.text.lower() in equipo:
            equipo_count += 1
        elif token.text.lower() in individual:
            individual_count += 1

    # Analizar el sentimiento general del texto
    sentimiento = TextBlob(texto).sentiment.polarity

    # Determinar si el texto hace mención a trabajar en equipo o por su cuenta, utilizando tanto las palabras clave como el análisis semántico
    if equipo_count > individual_count and sentimiento > 0:
        return "Trabajo en equipo"
    elif individual_count > equipo_count and sentimiento < 0:
        return "Trabajo individual"
    else:
        return "No se pudo determinar"
