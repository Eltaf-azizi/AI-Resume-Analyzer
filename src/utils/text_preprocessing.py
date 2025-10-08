import re


def normalize_whitespace(text: str) -> str:
    # remove null bytes and collapse spaces

    if not text:
        return ""
    text = re.sub(r"\x00", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\r\n", "\n", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    
    return text.strip()
