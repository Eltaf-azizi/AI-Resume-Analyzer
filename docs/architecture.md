# Architecture

- FastAPI backend (src.main) provides an endpoint `/api/analyze`.
- Parsers extract text from resumes (PDF/DOCX/TXT).
- SkillExtractor matches text to a skills taxonomy using fuzzy matching.
- JobMatcher computes similarity between resume text and job descriptions using embeddings (Sentence-Transformers) or TF-IDF fallback.
- InsightsGenerator produces missing skills and role-specific recommendations.
- Optional Streamlit UI acts as a frontend.
