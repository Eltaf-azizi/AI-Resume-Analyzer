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
        self.threshold = threshold



    def extract(self, text: str) -> Dict[str, List[str]]:
        """
        Return extracted skills grouped by category (technical/soft)
        Uses fuzzy matching against the skills database.
        """

        if not text:
            return {"technical": [], "soft": []}
        text_lower = text.lower()
        found = {"technical": [], "soft": []}

        # scan word windows and also do fuzzy against known skills
        # Use rapidfuzz process.extract to find best matches from skill_list
        candidates = process.extract(text_lower, self.skill_list, scorer=fuzz.partial_ratio, limit=200)
        matched = set()
        for skill, score, _ in candidates:
            if score >= self.threshold:
                matched.add(skill)

        # map matched back to categories
        for cat, skills in self.skills_db.items():
            for s in skills:
                if s.lower() in matched:
                    found.setdefault(cat, []).append(s)

        # also try direct substring matches to catch multiword skills
        for cat, skills in self.skills_db.items():
            for s in skills:
                if s.lower() in text_lower and s not in found.get(cat, []):
                    found.setdefault(cat, []).append(s)
                    
        # dedupe
        for k in found:
            found[k] = sorted(list(set(found[k])), key=lambda x: x.lower())
        return found
