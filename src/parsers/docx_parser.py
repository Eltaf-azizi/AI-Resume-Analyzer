from docx import Document
from ..utils.text_preprocessing import normalize_whitespace



def parse_docx(path: str) -> str:
    """
    Extract text from a DOCX file.
    """
    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text]
    return normalize_whitespace("\n".join(paragraphs))
