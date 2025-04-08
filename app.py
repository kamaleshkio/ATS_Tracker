from dotenv import load_dotenv
load_dotenv()

import os 
import PyPDF2 as pdf
import json 
import google.generativeai as genai
import streamlit as st



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(input)
    return response.text

def convert_pdf_to_images(pdf_file):
    reader=pdf.PdfReader(pdf_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
    

input_prompt1 = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
Here is the file, resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# input_prompt2 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# here is the job description - {jd}, Here is the resume - {text}.

# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.

# """

# input_prompt3 = """
# you are an experienced exper in the specified field, 
# here is the job description - {jd}, Here is the resume - {text}.
# your task is to provide the suggestion to the candidate to improve 
# his resume and the skills they should focus on the specific skills field
# """
st.title("smart AI for Application Tracking System Resume Analyzer")
st.text("Improve your resume by scanning this PDF and providing the required information.")
jd = st.text_area("Paste your job description here")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

if uploaded_file:
    st.write("file uploaded successfully.")

submit1 = st.button("Analyze")

#submit2 = st.button("get the percentage of match")

#submit3 = st.button("Here are the suggestions to improve your resume")

if submit1:
    if uploaded_file is not None:
        text = convert_pdf_to_images(uploaded_file)
        response = get_gemini_response(input_prompt1)

        st.subheader(response)
        
    else:
        st.write("Please upload a PDF file to analyze.")

# elif submit2:
#     if uploaded_file is not None:
#         text = convert_pdf_to_images(uploaded_file)
#         response = get_gemini_response( input_prompt2)

#         st.subheader("Response")
#         st.write(response)
#     else:
#         st.write("Please upload a PDF file to analyze.")

# elif submit3:
#     if uploaded_file is not None:
#         text = convert_pdf_to_images(uploaded_file)
#         response = get_gemini_response(input_prompt3)

#         st.subheader("Response")
#         st.write(response)
#     else:
#         st.write("Please upload a PDF file to analyze.")
