import os
from src.parsers.text_cleaner import clean_text


def test_clean_text_basic():
    txt = "Hello\x00\x00 --- __\n\n\nWorld"
    out = clean_text(txt)
    assert "Hello" in out
    assert "World" in out
    assert "\n\n" in out

