
from pydantic import BaseModel
from typing import List, Dict, Any



class AnalyzeResponse(BaseModel):
    parsed_text_snippet: str
    skills: Dict[str, List[str]]
    matched_roles: List[Dict[str, Any]]
    insights: Dict[str, Any]
