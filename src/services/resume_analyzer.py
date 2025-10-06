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
