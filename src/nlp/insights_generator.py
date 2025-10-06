from typing import Dict, List


class InsightsGenerator:

    def __init__(self, skills_taxonomy: Dict[str, List[str]], top_k=5):
        self.taxonomy = skills_taxonomy
        self.top_k = top_k


    def missing_skills(self, extracted_skills: Dict[str, List[str]], required_skills: List[str]) -> List[str]:
        
        """
        Given extracted skills and a list of required skills (strings),
        return missing skills ordered by frequency (basic heuristic).
        """
        extracted_normalized = {s.lower() for cat in extracted_skills.values() for s in cat}
        missing = []

        for r in required_skills:
            rn = r.lower()
            if rn not in extracted_normalized:
                missing.append(r)
                
        return missing[: self.top_k]


