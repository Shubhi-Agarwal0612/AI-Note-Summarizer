import streamlit as st

st.title("AI Note Summarizer — Day 1")
uploaded = st.file_uploader("Upload your notes (txt/pdf)", type=["txt", "pdf"])
text = st.text_area("Or paste your notes here:")
import pdfplumber
from PyPDF2 import PdfReader    

if uploaded is not None:
    if uploaded.name.endswith(".pdf"):
        with pdfplumber.open(uploaded) as pdf:
            text_data = "\n".join([page.extract_text() for page in pdf.pages])
    else:
        text_data = uploaded.read().decode("utf-8")
else:
    text_data = text
st.write(text_data)
