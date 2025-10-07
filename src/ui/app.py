
import streamlit as st
import requests
import tempfile
import os


API_URL = "http://127.0.0.1:8000/api/analyze"


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")


st.title("AI Resume Analyzer")
st.write("Upload a resume (PDF, DOCX, TXT) and get skills and job role suggestions.")



uploaded = st.file_uploader("Upload resume", type=["pdf", "docx", "txt"])

if uploaded:
    with st.spinner("Uploading and analyzing..."):

        # save to temp file
        suffix = "." + uploaded.name.split(".")[-1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.getbuffer())
            tmp_path = tmp.name
        files = {"file": open(tmp_path, "rb")}

