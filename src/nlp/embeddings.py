import os
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer


try:
    from sentence_transformers import SentenceTransformer
    HAVE_SBER = True
except Exception:
    HAVE_SBER = False



class EmbeddingModel:

    def __init__(self, backend="sentence_transformers", model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.backend = backend
        self.model_name = model_name
        self.model = None
