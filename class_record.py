import speech_recognition as sr
import mysql.connector
import json
import os


with open("BD_INFO.json", "r") as j:
    data = json.load(j)
    db = mysql.connector.connect(
    host = data["host"],
    user = data["user"],
    password = data["password"],
    database = data["database"])
cursor = db.cursor()


class Clase:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.preguntas = []

    
        


    def grabar(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Comenzando a grabar...")
            audio = r.listen(source)
            print("Grabación finalizada.")
        try:
            pregunta = r.recognize_google(audio, language='es-ES')
            self.preguntas.append(pregunta)
            print("Pregunta registrada:", pregunta)
        except sr.UnknownValueError:
            print("No se pudo entender lo que se dijo.")
        except sr.RequestError as e:
            print("Error al solicitar la API de reconocimiento de voz; {0}".format(e))

    def editar(self):
        # Función para editar las clases grabadas

    def publicar(self):
        # Función para publicar las clases grabadas

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.preguntas = []

    def hacer_pregunta(self):
        pregunta = input("¿Cuál es tu pregunta? ")
        self.preguntas.append(pregunta)
        print("Pregunta registrada:", pregunta)

class Academia:
    _instance = None

    def __new__(cls, nombre):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nombre = nombre
            cls._instance.clases = []
            cls._instance.usuarios = []
        return cls._instance

    def crear_clase(self, nombre, profesor):
        clase = Clase(nombre, profesor)
        self.clases.append(clase)
        print("Clase creada:", clase.nombre)

    def registrar_usuario(self, nombre, apellido):
        usuario = Usuario(nombre, apellido)
        self.usuarios.append(usuario)
        print("Usuario registrado:", usuario.nombre, usuario.apellido)

    def guardar_preguntas(self, usuario, clase):
        for pregunta in usuario.preguntas:
            clase.preguntas.append((usuario, pregunta))

# Ejemplo de uso
academia = Academia("Academia Dream Junk")




# Crear una clase y grabar preguntas
academia.crear_clase("Matemáticas", "Profesor A")
academia.registrar_usuario("Juan", "Pérez")
clase = academia.clases[0]

clase.grabar()

# Guardar preguntas del usuario en la clase correspondiente
usuario = academia.usuarios[0]
academia1.guardar_preguntas(usuario, clase)
print(clase.preguntas)

# Editar y publicar la clase
clase.editar()
clase.publicar()