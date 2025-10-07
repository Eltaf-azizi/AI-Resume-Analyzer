
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

        try:
            resp = requests.post(API_URL, files=files, timeout=120)
            resp.raise_for_status()
            data = resp.json()
            st.subheader("Extracted skills")
            skills = data.get("skills", {})
            st.write(skills)
            st.subheader("Top matching job roles")
            for r in data.get("matched_roles", []):
                st.markdown(f"**{r['title']}** — score: {r['score']:.2f}")
                st.write(r.get("excerpt", "")[:400])
            st.subheader("Insights")
            st.write(data.get("insights"))

        except Exception as e:
            st.error(f"Error analyzing resume: {e}")

        finally:
            try:
                os.remove(tmp_path)
                
            except Exception:
                pass
