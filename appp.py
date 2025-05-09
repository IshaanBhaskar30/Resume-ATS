import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

# Streamlit page config
st.set_page_config(page_title="ATS Resume Expert")
st.title("🧠 ATS Resume Analyzer with Gemini")

# --- Sidebar: API Key Input ---
st.sidebar.title("🔑 API Key Configuration")
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

# --- Validate API Key ---
if not api_key:
    st.warning("Please enter your Google API key in the sidebar.")
    st.stop()
else:
    genai.configure(api_key=api_key)

# --- Gemini Response Function ---
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content([input_text, *pdf_content, prompt])
    return response.text

# --- Convert PDF to base64 image parts ---
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        pdf_parts = []
        for image in images:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            pdf_parts.append({
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            })
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# --- User Inputs ---
input_text = st.text_area("📋 Job Description", key="input")
uploaded_file = st.file_uploader("📎 Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully.")

# --- Prompts for Gemini ---
input_prompt1 = """
You are an experienced Technical Human Resource Manager in the field of any one job role from Data Science, Full Stack Web development, Big Data Engineering, DEVOPS, Data Analyst. 
Your task is to review the provided resume against the job description for these profiles. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role from Data Science, Full Stack Web development, Big Data Engineering, DEVOPS, Data Analyst and deep ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as percentage and then keywords missing and last, final thoughts.
"""

# --- Buttons ---
submit1 = st.button("🔍 Evaluate Resume Fit")
submit3 = st.button("📊 Percentage Match (ATS Style)")

# --- Processing Logic ---
if submit1:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt1)
        st.subheader("📝 Resume Evaluation")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")

if submit3:
    if uploaded_file:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_prompt3)
        st.subheader("📈 ATS Match Results")
        st.write(response)
    else:
        st.warning("⚠️ Please upload a resume.")
