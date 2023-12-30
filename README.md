## Gemini API Applications

This repository contains few of the test applications I've built using streamlit to test and learn about the newly launched GEMINI API. 

## Context

Google Launched it's new Multi Modal Language Model GEMINI and the develooper API was launched on December 13. <br>

This repository contains few of the sample appications I have built while playing around with the GEMINI API. I have used Gemini Python SDK and Streamlit to build the application.

## Applications present

#### Question and Answer Bot

The file ```app.py``` contains the code for a sample Question and Answer bot application built with the help of streamlit to test the capabilities of ```gemini-pro``` model.

#### Image Analysis App

The file ```vision.py``` contains the code for a sample Image analysis application built with the help of streamlit to test the capabilities of ```gemini-pro-vision```, the image counterpart of ```gemini-pro```.

#### Question and Answer Chat Bot

The file ```QnA.py``` contains the code for a sample chat bot application that answers questions using Gemini while displaying the entire Chat History. <br>

Unlike the previous two applications, this app streams the content i.e. In case of a large response from Gemini, the text is displayed one by one instead of waiting for the whole response. 