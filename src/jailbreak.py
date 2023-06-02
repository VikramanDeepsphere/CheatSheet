import streamlit as st
import pandas as pd

def jail_breake():
    w1,col1,col2,w2=st.columns((1.5,2.5,4,.1))
    with col1:
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Select Functionality</span></p>", unsafe_allow_html=True)
    with col2:
        vAR_Category_Jailbreak = ['Select','The Jailbreak Prompt','The DAN 6.0 Prompt','The S.T.A.N Prompt','The DUDE Prompt','Illegality Mode','Alphabreak','Developer Mode','ChatGPT']
        vAR_input = st.selectbox('',vAR_Category_Jailbreak)
    
    if vAR_input == 'The Jailbreak Prompt':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
    
    
    elif vAR_input == 'The DAN 6.0 Prompt':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
    
    
    elif vAR_input == 'The S.T.A.N Prompt':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
   
   
    elif vAR_input == 'The DUDE Prompt':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
    
    
    elif vAR_input == 'Illegality Mode':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
   
   
    elif vAR_input == 'Alphabreak':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
    
    
    elif vAR_input == 'Developer Mode':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
   
   
    elif vAR_input == 'ChatGPT':
        with col1:
            st.write('# ')
            st.write('# ')
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Example Prompt</span></p>", unsafe_allow_html=True)
        with col2:
            st.write('# ')
            st.info()
   
   
    