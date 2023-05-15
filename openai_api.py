import openai

openai.api_key = "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"

def make_prompt(prompt, engine="davinci"):
    response = openai.Completion.create(engine=engine, prompt=prompt)
    answer = response.choices[0].text.strip()
    return answer

# Función para identificar los temas principales
def get_topics(text):
    response = openai.Completion.create(
        engine="davinci", 
        prompt="Identify the main topics in the following text: " + text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    topics = response.choices[0].text.strip()
    return topics

def resume_text(text):
    response = openai.Completion.create(
        engine="davinci", 
        prompt="Summarize this text, make sure you identify the main features and that they are understood in the summary: " + text
    )
    resumen = response.choices[0].text.strip()
    return resumen

def reformulate_text(text):
    response = openai.Completion.create(
        engine="davinci", 
        prompt="Reformulate this text, make sure you identify the main features and that they are understood in the summary: " + text
    )
    reformulated_text = response.choices[0].text.strip()
    return reformulated_text