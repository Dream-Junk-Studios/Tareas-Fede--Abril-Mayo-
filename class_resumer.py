import speech_recognition as sr
from aylienapiclient import textapi



class ResumenVoz:
    def __init__(self, api_id, api_key):
        self.aylien_client = textapi.Client(api_id, api_key)
        self.recognizer = sr.Recognizer()

    def obtener_resumen(self, num_frases=3):
        with sr.Microphone() as source:
            print("Di algo...")
            audio = self.recognizer.listen(source)

        # Transcribir el audio a texto utilizando el servicio de reconocimiento de voz de Google
        text = self.recognizer.recognize_google(audio)

        # Resumir el texto utilizando la API de resumen de texto de Aylien
        summary = self.aylien_client.Summarize({'text': text, 'sentences_number': num_frases})

        # Imprimir el resumen del texto
        print(summary['sentences'])


resumen_voz = ResumenVoz(api_id="API_ID", api_key="API_KEY")
resumen_voz.obtener_resumen(num_frases=3)

 '''
import speech_recognition as sr
from transformers import pipeline

class ResumenClase:
    def __init__(self, modelo_resumen='t5-base', modelo_reconocimiento='google'):
        self.modelo_resumen = pipeline('summarization', model=modelo_resumen, tokenizer=modelo_resumen)
        self.modelo_reconocimiento = modelo_reconocimiento
        self.recognizer = sr.Recognizer()

    def obtener_resumen(self, num_frases=3):
        # Reconocer la clase (voz o texto)
        if self.modelo_reconocimiento == 'google':
            with sr.Microphone() as source:
                print("Di algo...")
                audio = self.recognizer.listen(source)

            # Transcribir el audio a texto utilizando el servicio de reconocimiento de voz de Google
            texto = self.recognizer.recognize_google(audio)
        elif self.modelo_reconocimiento == 'texto':
            texto = input("Introduce el texto de la clase: ")
        else:
            raise ValueError("Modelo de reconocimiento no válido")

        # Generar un resumen del texto utilizando el modelo de resumen
        resumen = self.modelo_resumen(texto, max_length=num_frases, min_length=1, do_sample=False)
        resumen = resumen[0]['summary_text']

        # Imprimir el resumen del texto
        print(resumen)

resumen_clase = ResumenClase(modelo_resumen='t5-base', modelo_reconocimiento='google')
resumen_clase.obtener_resumen(num_frases=3)

 '''