import openai
import streamlit as st
import os
openai.api_key = os.environ["API_KEY"]

def generate_response4(prompt):
    
    response = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0,
    max_tokens=3000,
    messages=[{'role':'user','content':prompt}],
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )
    return response['choices'][0]['message']['content']