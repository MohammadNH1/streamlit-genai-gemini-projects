from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")
genai.configure(api_key=fetched_api_key)

def LLM_Response(question):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(question)
    return response.text

st.title('Q&A Application using Gemini Pro')


user_question = st.text_input("Ask a question:")
button = st.button('Ask')
if button:
    result = LLM_Response(user_question)
    st.subheader('The Response is: ')
    for word in result:
        st.write(word.text)