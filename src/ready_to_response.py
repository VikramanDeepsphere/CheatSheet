import streamlit as st
from src.gpt_API import generate_response4

def ready_response():
    w11,col11,col22,w22=st.columns((1.5,2.5,4,.1))
    cc2,cc1,cc3=st.columns((2,8,0.2))
    with col11:
        st.write('# ')
        st.write('# ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Enter paragraph</span></p>", unsafe_allow_html=True)
    with col22:
        vAR_para_input = st.text_area('')
        prompt = vAR_para_input
        if vAR_para_input != "":
            st.write(" ")
            if st.button("Sumbit"):
                respone = generate_response4(prompt)
                with cc1:
                    st.write("# ")
                    st.success(respone)