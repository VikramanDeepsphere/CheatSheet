import streamlit as st
from src.ready_to_response import ready_response

def writing(vAR_input_model):
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Writing_Styles = ['Select','Formal','Informal','Pesuasive','Descriptive','Humoros','Narrative','Inspirational','Confrontational']
        vAR_input = st.selectbox('',vAR_Category_Writing_Styles)
    
    if vAR_input == 'Formal':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Please provide a detailed analysis of the economic impact of renewable energy adoption, considering factors such as job creation, environmental sustainability, and long-term cost savings.")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Informal':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Hey ChatGPT, what's your favorite movie of all time? Let's chat about some cool flicks and share our thoughts on the finest films out there!")
        ready_response(vAR_input_model)
    
    elif vAR_input == 'Pesuasive':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("You are a passionate advocate for renewable energy. Engage in a conversation with ChatGPT and present a compelling argument for renewable energy sources. Highlight their environmental benefits, economic advantages, and long-term sustainability.")
        ready_response(vAR_input_model)

   
    elif vAR_input == 'Descriptive':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Describe the mesmerizing beauty of a vibrant sunset over a serene ocean. The golden hues merge with the tranquil waves and paint the sky in a breathtaking display of nature's artistry.")
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Humoros':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Tell me a joke that will make me laugh and brighten my day.")
        ready_response(vAR_input_model)

   
    elif vAR_input == 'Narrative':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Imagine you are embarking on a thrilling quest through a mystical forest, seeking a fabled artifact said to grant extraordinary powers. Share with me your journey, the challenges you face, the allies you meet, and the ultimate outcome of your adventure.")
        ready_response(vAR_input_model)

    
    elif vAR_input == 'Inspirational':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Sharing some words of wisdom and inspiration that can motivate and uplift someone facing challenges. This will remind them of their inner strength and limitless possibilities.")
        ready_response(vAR_input_model)

   
    elif vAR_input == 'Confrontational':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info("Present an argument challenging the effectiveness of renewable energy sources in mitigating climate change. This argument highlights potential drawbacks and limitations that often become unnoticed.")
        ready_response(vAR_input_model)
        