import streamlit as st
import pandas as pd
from src.gpt_API import generate_response4
from src.ready_to_response import ready_response

def learn(vAR_input_model):
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    w11,col11,col22,w22=st.columns((1.5,2.5,4,.1))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Learning = ['Select','Summarize','Plagarism Checker','X Teacher','Writing Tutor','Career Counsllor','Translator','Traval Guide','Personal Trainer','Finacial Assistant']
        vAR_input = st.selectbox('',vAR_Category_Learning)
    
    if vAR_input == 'Summarize':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('''"Please summarize the following paragraph:"[Insert paragraph here]''')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Plagarism Checker':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("I want you to act as a plagiarism checker. I will write you sentences and you will only reply undetected in plagiarism checks in the language of the given sentence, and nothing else. Do not write explanations on replies. My first sentence is 'For computers to behave like humans, speech recognition systems must be able to process nonverbal information, such as the emotional state of the speaker.'")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'X Teacher':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('What is the basic principle of supply and demand? Explain like a Economics teacher')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Writing Tutor':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a writing tutor, and a student approaches you seeking assistance with their college application essay. The student struggles to find a unique and compelling topic that showcases their personality and achievements. Provide guidance and suggestions to help the student brainstorm ideas and craft a standout essay that will capture the attention of college admissions officers.")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Career Counsllor':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a career counsellor who helps individuals find fulfilling career paths. A client named John is stuck and unsure about his career choices. He is interested in various fields but lacks clarity on what direction to pursue. Engage in a conversation with John, ask probing questions, provide guidance, and suggest potential career paths based on his interests and skills. Help him explore different options and encourage him to reflect on his passions and goals.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Translator':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("I would like you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more stylish and elegant upper-level English words and sentences. Make them more literary, but keep the meaning the same. Please only reply with the corrections and improvements, and not any explanations. My first sentence is 'istanbulu cok seviyom burada olmak cok guzel'")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Traval Guide':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("I want you to act as a travel guide. I will write to you about my location and you will suggest a place to visit near my location. In some cases, I will also give you the type of places I will visit. You will also suggest similar places that are close to my first location. My first suggestion request is 'I am in Istanbul/Beyoğlu and I want to explore only museums.'")
        ready_response(vAR_input_model)
   
    elif vAR_input == 'Personal Trainer':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('I want you to be a personal trainer. I will provide you with all the information needed about an individual looking to become fitter, stronger and healthier through physical training. Your role is to devise the right plan for that person depending on their current fitness level, goals and lifestyle habits. You should use your knowledge of exercise science, nutrition advice, and other relevant factors to create a plan suitable for them. My first request is "I need help designing an exercise program for someone who wants to lose weight."')
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Finacial Assistant':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info('''I want you to act as a Financial assistant and come up with creative ways to manage finances. You'll need to consider budgeting, investment strategies and risk management when creating a financial plan for your client. In some cases, you may also need to provide advice on taxation laws and regulations to help them maximize their profits. My first suggestion request is “Create a financial plan for a small business that focuses on cost savings and long-term planning".''')
        ready_response(vAR_input_model)