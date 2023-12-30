from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def  get_gemini_response(user_input):
    response = model.generate_content(user_input, stream=True)
    return response

st.set_page_config('QnA App')
st.header('Gemini Question & Answer Application')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Enter a prompt here")
submit = st.button("Submit")

if input and submit:
    st.session_state['chat_history'].append(('You', input))
    response = get_gemini_response(input)
    # st.subheader("Response:")
    for chunk in response:
        # st.write(chunk.text)
        st.session_state['chat_history'].append(('AI', chunk.text))
    
st.subheader('Chat:')
print(len(st.session_state['chat_history']))

for role, text in st.session_state['chat_history']:
    if role == "You":
        st.write("You: ")
    st.write(f"{text}")
    if role == "You":
        st.write("Bard: ")