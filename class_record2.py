from flask import Flask, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.cluster.util import cosine_distance
from video_to_audio import convert_video_to_audio_ffmpeg
import numpy as np

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()
@app.route('/upload', methods=['POST'])
def upload():
    video_file = request.files['video']
    question_times = request.form['questions']
    response_times = request.form['responses']
    # Procesamiento del video y los tiempos de las preguntas y respuestas
    return 'Archivo recibido con éxito!'


convert_video_to_audio_ffmpeg(video_file)



def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    word_tokens = [word_tokenize(sentence.lower()) for sentence in sentences]
    word_tokens = [[lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words] for words in word_tokens]
    return word_tokens

def sentence_similarity(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    if len(s1.union(s2)) == 0:
        return 0
    return len(s1.intersection(s2)) / len(s1.union(s2))

def build_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j])
    return similarity_matrix

def generate_summary(text, num_sentences=5):
    sentences = preprocess_text(text)
    sentence_similarity_matrix = build_similarity_matrix(sentences)
    scores = np.sum(sentence_similarity_matrix, axis=1)
    ranked_sentences = [sentence for _, sentence in sorted(zip(scores, sentences), reverse=True)]
    summary = " ".join(ranked_sentences[:num_sentences])
    return summary