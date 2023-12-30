from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title='LLM Q&A App')
st.header('Gemini LLM App')

input = st.text_input("Question: ", key=input)
submit = st.button("Ask")

if submit:
    response_text = get_gemini_response(input)
    st.subheader('Answer: ')
    st.write(response_text)

