<h1 align="center">AI-Resume-Analyzer</h1>

AI Resume Analyzer is an advanced NLP-based application that analyzes resumes, extracts skills, and recommends career improvements. It helps users understand their professional strengths, missing skills, and best-fit job roles — all powered by Natural Language Processing and AI.

## Features

 - **Smart Resume Parsing:**
  Automatically extracts text from PDF and DOCX resumes.

 - **Skill Extraction:**
  Detects hard, soft, and technical skills using NLP.

 - **Job Role Matching:**
  Compares extracted skills with job descriptions and suggests matching roles.

 - **Career Insights:**
  Identifies missing skills, gaps, and suggests personalized improvements.

 - **Upskilling Recommendations:**
  Recommends online courses, certifications, or resources based on your resume.

 - **Web Interface:**
  Upload your resume and instantly get an interactive analysis report (Streamlit UI).


## Project Structure

    ai-resume-analyzer/
    ├── README.md
    ├── requirements.txt
    ├── config/
    │   ├── settings.yaml
    │   └── logging.conf
    ├── data/
    │   ├── sample_resumes/
    │   ├── job_descriptions/
    │   └── skills_database.json
    ├── src/
    │   ├── main.py
    │   ├── parsers/
    │   ├── nlp/
    │   ├── services/
    │   ├── api/
    │   ├── ui/
    │   └── utils/
    ├── tests/
    └── docs/



## 🧠 Core Workflow

 1. Upload Resume → User uploads PDF or DOCX
 2. Parsing → Extract and clean text using file parsers
 3. Skill Extraction → NLP model identifies technical and soft skills
 4. Job Matching → Compare resume with available job descriptions
 5. Insights Generation → Highlight strengths, weaknesses, and suggestions
 6. Recommendations → Recommend roles and learning paths


## ⚙️ Installation
### 1. Clone the repository
```
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```


## 🧾 Usage
### Option 1: Command Line

Run the analyzer directly:
```
python src/main.py --file path/to/resume.pdf
```
### Option 2: Web App (Streamlit UI)

Launch the interactive interface:
```
streamlit run src/ui/app.py
```

Upload your resume → get insights → explore recommended skills and roles.
