from openai_api import make_prompt,get_topics

path = 'prueba/log.txt'

with open(path,'r') as  f:
        text = f.read()

def resume_call(text):
    summarized_call = make_prompt("Tell me what is this call about: " + text)
    return summarized_call

def get_essential_words(text):
    important_words = make_prompt("Based on the context of the call, tell me what are the most important words: " + text)
    return important_words

def get_call_topics(text):
    topics = get_topics(text)
    return topics




def main():



if __name__ == '__main__':
    main()