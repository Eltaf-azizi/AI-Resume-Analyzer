import re
from ..utils.text_preprocessing import normalize_whitespace



def clean_text(text: str) -> str:
    """
    Basic cleaning: remove excessive whitespace and non-printables,
    collapse repeated newlines, remove common email footers if found.
    """
    if not text:
        return ""
    # drop binary noise
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    # drop long runs of dashes or underscores
    text = re.sub(r"(-{3,}|_{3,})", " ", text)
    # collapse multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return normalize_whitespace(text)
