import json
import os
from rapidfuzz import process, fuzz
from typing import List, Dict


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_PATH = os.path.join(BASE_DIR, "data", "skills_database.json")



class SkillExtractor:

    def __init__(self, skills_path: str = SKILLS_PATH, threshold: float = 80):
        with open(skills_path, "r", encoding="utf-8") as fh:
            self.skills_db = json.load(fh)
        # flatten skills
        self.skill_list = []
        for cat, skills in self.skills_db.items():
            self.skill_list.extend([s.lower() for s in skills])
