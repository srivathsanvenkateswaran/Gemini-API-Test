from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

from PIL import Image

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(image, input_text):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)

    return response.text

st.set_page_config(page_title='LLM Image App')
st.header('Gemini Image LLM App')

input = st.text_input("Question: ", key=input)
uploaded_file = st.file_uploader(
    label="Choose an image...",
    type=["jpg", "jpeg", "png"]  
)
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image=image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Describe the image")

if submit:
    response = get_gemini_response(image=image, input_text=input)

    st.subheader("Answer: ")
    st.write(response)