import re
import heapq
import requests
import nltk
from inscriptis import get_text
from googletrans import Translator
from file_handler import Singleton, FileHandler

nltk.download('punkt')
nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words('spanish')
        self.translator = Translator()

    def _format_text(self, text):
        article_text = text
        # Se remueven los corchetes (Square brackets) y espacios extra
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)
        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
        formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
        # Tokenizacion
        sentence_list = nltk.sent_tokenize(article_text)
        return formatted_article_text, sentence_list

    def _get_word_frequencies(self, formatted_article_text):
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in self.stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
        return word_frequencies

    def _get_repeated_phrases(self, sentence_list, word_frequencies):
        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]
        return sentence_scores

    def summarize(self, text):
        formatted_article_text, sentence_list = self._format_text(text)
        word_frequencies = self._get_word_frequencies(formatted_article_text)
        sentence_scores = self._get_repeated_phrases(sentence_list, word_frequencies)
        summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary

    def translate(self, text, dest_lang):
        translation = self.translator.translate(text, dest=dest_lang)
        return translation.text



def main():
    
 

    text_processor = TextProcessor()
    summary = text_processor.summarize(get_text(texto))
    print(summary)

if __name__ == '__main__':
    main()