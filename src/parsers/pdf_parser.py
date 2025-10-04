import pdfplumber
from ..utils.text_preprocessing import normalize_whitespace



def parse_pdf(path: str) -> str:
    """
    Extract text from a PDF file.
    """
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text_parts.append(txt)
    raw_text = "\n".join(text_parts)
    return normalize_whitespace(raw_text)
