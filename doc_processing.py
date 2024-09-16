from dotenv import load_dotenv
import PyPDF2 as pdf
import streamlit as st
import os
import google.generativeai as genai


load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")
genai.configure(api_key=fetched_api_key)



def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, "Can you summarize this document as a bulleted list?"])
    return response.text

       
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
#

st.set_page_config(page_title="Gemini Document Processing Demo")

st.header("Gemini Application")
uploaded_file = st.file_uploader("Upload Your PDF Document",type="pdf",help="Please uplaod the pdf")

submit=st.button("Submit")

if submit:
    extracted_text = input_pdf_text(uploaded_file)
    response=get_gemini_response(extracted_text)
    st.subheader("The Response is")
    st.write(response)