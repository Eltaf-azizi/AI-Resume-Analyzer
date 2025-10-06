from typing import List, Dict



# basic mapping to resources (in a real product this would be richer)
RESOURCE_DB = {
    "deep learning": ["fast.ai Practical Deep Learning", "Coursera Deep Learning Specialization"],
    "tensorflow": ["TensorFlow official tutorials", "Coursera: TensorFlow in Practice"],
    "pytorch": ["PyTorch tutorials", "Deep Learning with PyTorch (book)"],
    "aws": ["AWS Cloud Practitioner", "AWS Developer Fundamentals"],
    "docker": ["Docker getting started", "Pluralsight Docker paths"],
    "airflow": ["Apache Airflow docs", "Hands-On Airflow"],
    "sql": ["Mode SQL tutorial", "LeetCode SQL practice"]
}




class RecommendationEngine:
    def recommend_for_missing(self, missing_skills: List[str]) -> Dict[str, List[str]]:
        recs = {}

        for skill in missing_skills:
            k = skill.lower()

            if k in RESOURCE_DB:
                recs[skill] = RESOURCE_DB[k]

            else:
                # fuzzy fallback: suggest a generic learning link
                recs[skill] = [f"Search courses for '{skill}' on major learning platforms (Coursera, Udemy)"]
        
        return recs
