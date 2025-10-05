import os
import glob
import numpy as np
from typing import List, Dict
from .embeddings import EmbeddingModel
from sklearn.metrics.pairwise import cosine_similarity



class JobMatcher:

    def __init__(self, job_desc_dir: str, embedding_backend="sentence_transformers", model_name=None):
        self.job_desc_dir = job_desc_dir
        self.embedding_backend = embedding_backend
        self.model_name = model_name or "sentence-transformers/all-MiniLM-L6-v2"
        self.embedding_model = EmbeddingModel(backend=embedding_backend, model_name=self.model_name)
        self.job_texts = []
        self.job_meta = []
        self.job_embeddings = None
        self._load_job_descriptions()
        


    def _load_job_descriptions(self):
        files = glob.glob(os.path.join(self.job_desc_dir, "*.txt"))
        if not files:
            return
        self.job_texts = []
        self.job_meta = []
        for path in files:
            with open(path, "r", encoding="utf-8") as fh:
                txt = fh.read()
            title = os.path.basename(path).replace(".txt", "").replace("_", " ").title()
            self.job_texts.append(txt)
            self.job_meta.append({"title": title, "path": path})
            
        # compute embeddings
        try:
            self.job_embeddings = self.embedding_model.fit_transform(self.job_texts)

