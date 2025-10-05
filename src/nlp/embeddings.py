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
        
        if backend == "sentence_transformers" and HAVE_SBER:
            self.model = SentenceTransformer(model_name)
        else:
            self.vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)


    def fit_transform(self, texts: List[str]):
        if self.backend == "sentence_transformers" and self.model:
            return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
        else:
            return self.vectorizer.fit_transform(texts).toarray()


    def transform(self, texts: List[str]):
        if self.backend == "sentence_transformers" and self.model:
            return self.model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
        else:
            return self.vectorizer.transform(texts).toarray()

