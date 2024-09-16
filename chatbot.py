import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")
genai.configure(api_key=fetched_api_key)

def LLM_Response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text


st.title("Q&A Application Using Gemini Pro")
input = st.text_input("Ask a question: ")
submit = st.button('Submit')

if submit:
    result=LLM_Response(input)
    st.subheader("The response is: ")
    st.write(result)