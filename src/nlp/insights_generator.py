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



    def skill_gap_summary(self, extracted_skills: Dict[str, List[str]], matched_roles: List[Dict]) -> Dict:
        """
        Return a simple summary of gaps across matched roles.
        """

        role_recs = []
        for role in matched_roles:
            # crude extraction: split job excerpt into words that look like skills (very simple)
            # In practice, you'd parse the JD more carefully.
            words = role["excerpt"].split()

            # pick nouns/tech tokens heuristically by comparison with taxonomy
            required = []
            tax_flat = {s.lower() for cat in self.taxonomy.values() for s in cat}
            
            for token in words:
                t = token.strip(",.()").lower()
                if t in tax_flat and t not in required:
                    required.append(t)

            missing = self.missing_skills(extracted_skills, required)
            role_recs.append({"role": role["title"], "missing": missing, "score": role["score"]})
        return {"role_recommendations": role_recs}
