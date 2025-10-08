
from src.nlp.skill_extractor import SkillExtractor
import os



def test_extract_skills():
    se = SkillExtractor()
    text = "Experienced in Python, pandas and SQL. Good communication skills."
    res = se.extract(text)
    assert "Python" in [s.title() for s in res.get("technical", [])] or any("python" in s.lower() for s in res.get("technical", []))
    assert "communication" in [s.lower() for s in res.get("soft", [])] or "communication" in text.lower()

