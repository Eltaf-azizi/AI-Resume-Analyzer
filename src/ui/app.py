
import streamlit as st
import requests
import tempfile
import os


API_URL = "http://127.0.0.1:8000/api/analyze"


st.set_page_config(page_title="AI Resume Analyzer", layout="centered")


st.title("AI Resume Analyzer")
st.write("Upload a resume (PDF, DOCX, TXT) and get skills and job role suggestions.")
