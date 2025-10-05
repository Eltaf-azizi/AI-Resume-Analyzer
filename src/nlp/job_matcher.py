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
