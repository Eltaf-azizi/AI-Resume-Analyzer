import os
from typing import Dict, Any
from ..parsers.pdf_parser import parse_pdf
from ..parsers.docx_parser import parse_docx
from ..parsers.text_cleaner import clean_text
from ..nlp.skill_extractor import SkillExtractor
from ..nlp.job_matcher import JobMatcher
from ..nlp.insights_generator import InsightsGenerator
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ResumeAnalyzerService:

    def __init__(self, settings: Dict):
        self.settings = settings
        skills_path = settings["paths"]["skills_db"]
        job_dir = settings["paths"]["job_desc_dir"]
        backend = settings["app"].get("model_backend", "sentence_transformers")
        model_name = settings["app"].get("embedding_model")
        self.skill_extractor = SkillExtractor(skills_path)
        self.job_matcher = JobMatcher(job_dir, embedding_backend=backend, model_name=model_name)
        
        with open(skills_path, "r", encoding="utf-8") as fh:
            self.taxonomy = json.load(fh)
        self.insights = InsightsGenerator(self.taxonomy)



    def _parse_file(self, path: str) -> str:
        ext = os.path.splitext(path)[1].lower()

        if ext == ".pdf":
            raw = parse_pdf(path)
        elif ext in [".docx", ".doc"]:
            raw = parse_docx(path)
