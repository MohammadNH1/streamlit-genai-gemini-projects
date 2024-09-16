import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")
genai.configure(api_key=fetched_api_key)


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-1.5-flash') 
    response = model.generate_content(input)
    return response.text

# Prompt Template for Email Generation without Resume
input_prompt = """
I would like you to act as a professional career consultant. Based on the provided job description,
please write an email template that an applicant can use to apply for the job. The email should be formal,
highlight key skills and experiences that match the job description, and include a polite closing.

Job Description: {jd}

The email should have the following structure:

Subject: [Job Title] Application - [Your Name]

Body:
Dear [Hiring Manager's Name],

I hope this email finds you well. I am writing to express my interest in the [Job Title] position at [Company Name]. 
Based on the job description, I am confident that my skills in [List Skills] align well with the requirements of this role. 
I have successfully [Mention Key Achievements or Experiences relevant to the job].

I look forward to discussing how my background, skills, and qualifications align with the needs of your team.

Thank you for your time and consideration. I look forward to the opportunity to contribute to the success of [Company Name].

Best regards,
[Your Name]
"""

st.title("Job Application Email Generator")
st.text("Generate a professional email template for your job application.")
jd = st.text_area("Paste the Job Description")
submit = st.button("Submit")


if submit:
    if jd:
        prompt = input_prompt.format(jd=jd)
        response = get_gemini_response(prompt)
        st.subheader('Generated Email Template:')
        st.write(response)
