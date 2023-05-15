import concurrent.futures

def summarize(self, text):
    formatted_article_text, sentence_list = self.format_text(text)
    word_frequencies = self.get_word_frequencies(formatted_article_text)
    sentence_scores = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # parallelize the get_repeated_phrases function
        futures = {executor.submit(self.get_repeated_phrases, sentence, word_frequencies) for sentence in sentence_list}
        for future in concurrent.futures.as_completed(futures):
            # merge the results of the parallelized function
            sentence_scores.update(future.result())
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

def get_word_frequencies(self, formatted_article_text):
    word_frequencies = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # parallelize the word frequency counting
        futures = {executor.submit(self.count_word_frequency, word, self.stopwords) for word in nltk.word_tokenize(formatted_article_text)}
        for future in concurrent.futures.as_completed(futures):
            # merge the results of the parallelized function
            word, frequency = future.result()
            if word not in word_frequencies.keys():
                word_frequencies[word] = frequency
            else:
                word_frequencies[word] += frequency
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    return word_frequencies

def count_word_frequency(self, word, stopwords):
    if word not in stopwords:
        return (word, 1)
    else:
        return (word, 0)