import streamlit as st
from src.learning_How_to_prompt import How_to_prompt
from src.role_playing import role_playing
from src.learning import learn
from src.Writing_Styles import writing
from src.jailbreak import jail_breake
from src.Prompting_techniques import Prompt_technique

def Chatgpt_Cheat():
    w1,col1,col2,w2=st.columns((1,4,5,.5))
    cc2,cc1,cc3=st.columns((2,8,0.2))
    with col1:
        st.markdown("### ")
        st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model</span></p>", unsafe_allow_html=True)
    with col2:
        st.markdown("## ")
        vAR_Model = ['GPT-3','GPT-3.5','GPT-4']
        vAR_input_model = st.radio(' ',vAR_Model,horizontal=True,index=0)
    if vAR_input_model != 'Select':
        with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Model Category</span></p>", unsafe_allow_html=True)
        with col2:
            vAR_Category = ['Select','Jailbreak','Role Playing','Learning','Writing Styles','Prompting Techniques','Learning How to Prompt?']
            vAR_input = st.selectbox(' ',vAR_Category)
        if vAR_input =='Jailbreak':
            with cc1:
                st.write("# ")
                # jail_breake(vAR_input_model)
                st.warning("Currently Not Available")
        elif vAR_input =='Role Playing':
            role_playing(vAR_input_model)
        elif vAR_input =='Learning':
            learn(vAR_input_model)
        elif vAR_input =='Writing Styles':
            writing(vAR_input_model)
        elif vAR_input =='Learning How to Prompt?':
            How_to_prompt(vAR_input_model)
        elif vAR_input == 'Prompting Techniques':
            Prompt_technique(vAR_input_model)
