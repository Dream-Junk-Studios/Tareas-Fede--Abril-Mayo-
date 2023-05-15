from flask import Flask, request
from openai_api import *
import os
import shutil

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def guardar_datos():
    video = request.files['video']
    log_chat = request.files['log_chat']
    preguntas = request.files['questions']

    # Guardar los archivos en una carpeta
    carpeta_datos = 'datos'
    os.makedirs(carpeta_datos, exist_ok=True)
    video.save(os.path.join(carpeta_datos, video.filename))
    log_chat.save(os.path.join(carpeta_datos, log_chat.filename))
    preguntas.save(os.path.join(carpeta_datos, preguntas.filename))


@app.route("/load", methods=["POST"])
def  cargar_datos():
    




    


if __name__ == "__main__":
    app.run()