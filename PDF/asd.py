import spacy
from spacy.lang.es import Spanish
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")

def reformulate_sentence(sentence):
    input_ids = tokenizer.encode(sentence, return_tensors="pt")
    outputs = model.generate(input_ids, max_length=50, num_beams=5, early_stopping=True)
    reformulated_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reformulated_sentence

nlp = spacy.load('es_core_news_sm')

# Define la oración de entrada
entrada = "El gato es un animal doméstico común que se encuentra en muchos hogares."

# Analiza la oración con spaCy
doc = nlp(entrada)


# Extrae las características de la oración
sustantivos = [token.text for token in doc if token.pos_ == 'NOUN']
verbos = [token.text for token in doc if token.pos_ == 'VERB']
adjetivos = [token.text for token in doc if token.pos_ == 'ADJ']


# Resumen automático de la oración
resumen = doc[:5].text


# Reformulación de la oración
reformulacion = reformulate_sentence(entrada)


# Imprime los resultados
print("Oración de entrada: ", entrada)
print("Resumen automático: ", resumen)
print("Reformulación: ", reformulacion)
print("Sustantivos: ", sustantivos)
print("Verbos: ", verbos)
print("Adjetivos: ", adjetivos)