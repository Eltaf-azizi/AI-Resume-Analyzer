from typing import Dict, List


class InsightsGenerator:

    def __init__(self, skills_taxonomy: Dict[str, List[str]], top_k=5):
        self.taxonomy = skills_taxonomy
        self.top_k = top_k


