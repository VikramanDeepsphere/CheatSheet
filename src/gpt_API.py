import openai
import os
openai.api_key = os.environ["API_KEY"]

def generate_response4(prompt):
    
    response = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0,
    max_tokens=3500,
    messages=[{'role':'user','content':prompt}],
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']

def generate_response3_5(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.2,
    max_tokens=3000,
    messages=[{'role':'user','content':prompt}],
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']

def generate_response3(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    return response["choices"][0]["text"]