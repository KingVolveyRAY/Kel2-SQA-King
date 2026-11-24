"""
oracle_vector_engine.py
Simulates Oracle Database 23ai AI Vector Search and RAG pipeline as detailed
in Oracle Academy: "Introduction to Vector Search with Oracle Database 23ai".

Key Features:
- Vector representation & Dense Embedding generator (L2-normalized)
- Vector distance metrics: COSINE, MANHATTAN, EUCLIDEAN, DOT PRODUCT
- SQL-like Vector Query execution:
    SELECT rule_id, title, description,
           VECTOR_DISTANCE(rule_vector, :query_vec, COSINE) as distance
    FROM sqa_rules
    ORDER BY distance ASC FETCH FIRST k ROWS ONLY;
- Retrieval-Augmented Generation (RAG) context injection
"""

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict, Any, Tuple

class Oracle23aiVectorDatabase:
    def __init__(self, vector_dim: int = 128):
        self.vector_dim = vector_dim
        self.rules: List[Dict[str, Any]] = []
        self.vector_store: np.ndarray = np.empty((0, vector_dim))
        self.vectorizer = TfidfVectorizer(
            max_features=vector_dim,
            ngram_range=(1, 3),
            sublinear_tf=True
        )
        self.is_indexed = False

    def load_knowledge_base(self, filepath: str = "data/oracle_sqa_knowledge_base.json"):
        """Loads SQA rules into Oracle Vector Table format."""
        with open(filepath, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)
            
        corpus = [
            f"{r['title']} {r['description']} {' '.join(r.get('keywords', []))} {r.get('bad_example', '')}"
            for r in self.rules
        ]
        
        # Fit vectorizer on domain corpus
        tfidf_matrix = self.vectorizer.fit_transform(corpus).toarray()
        
        # Pad or project to exact vector_dim if needed
        if tfidf_matrix.shape[1] < self.vector_dim:
            padding = np.zeros((tfidf_matrix.shape[0], self.vector_dim - tfidf_matrix.shape[1]))
            tfidf_matrix = np.hstack([tfidf_matrix, padding])
            
        # L2 Normalization (Oracle standard for unit hypersphere cosine search)
        norms = np.linalg.norm(tfidf_matrix, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        self.vector_store = tfidf_matrix / norms
        self.is_indexed = True
        print(f"[Oracle 23ai Vector DB] Initialized and indexed {len(self.rules)} SQA guidelines with {self.vector_dim}-dim vectors.")

    def embed_text(self, text: str) -> np.ndarray:
        """Converts query or code diff into a normalized vector embedding."""
        raw_vec = self.vectorizer.transform([text]).toarray()
        if raw_vec.shape[1] < self.vector_dim:
            padding = np.zeros((1, self.vector_dim - raw_vec.shape[1]))
            raw_vec = np.hstack([raw_vec, padding])
        norm = np.linalg.norm(raw_vec)
        if norm > 0:
            raw_vec = raw_vec / norm
        return raw_vec[0]

    @staticmethod
    def calculate_distance(vec_a: np.ndarray, vec_b: np.ndarray, metric: str = "COSINE") -> float:
        """
        Mathematical distance functions covered in Oracle Academy (Slide 8):
        - Cosine Distance: 1 - (A . B) / (||A|| * ||B||)
        - Manhattan Distance: sum(|A_i - B_i|)
        - Euclidean Distance: sqrt(sum((A_i - B_i)^2))
        - Dot Product Distance: 1 - (A . B)
        """
        metric = metric.upper()
        if metric == "COSINE":
            dot = np.dot(vec_a, vec_b)
            return float(max(0.0, 1.0 - dot))
        elif metric == "MANHATTAN":
            return float(np.sum(np.abs(vec_a - vec_b)))
        elif metric == "EUCLIDEAN":
            return float(np.linalg.norm(vec_a - vec_b))
        elif metric == "DOT":
            return float(-np.dot(vec_a, vec_b))
        else:
            raise ValueError(f"Unknown metric: {metric}")

    def vector_search(self, query_code: str, top_k: int = 2, metric: str = "COSINE") -> List[Dict[str, Any]]:
        """
        Simulates Oracle Database 23ai SQL Vector Search query:
        SELECT rule_id, category, title, description, severity,
               VECTOR_DISTANCE(rule_vector, :query_vec, COSINE) AS distance
        FROM sqa_review_guidelines
        ORDER BY distance ASC
        FETCH FIRST :top_k ROWS ONLY;
        """
        if not self.is_indexed:
            raise RuntimeError("Vector database is not indexed. Call load_knowledge_base() first.")
            
        q_vec = self.embed_text(query_code)
        
        results = []
        for i, rule in enumerate(self.rules):
            dist = self.calculate_distance(q_vec, self.vector_store[i], metric=metric)
            # Similarity score: 1 - distance (for cosine)
            sim = max(0.0, 1.0 - dist)
            results.append({
                "rule_id": rule["rule_id"],
                "category": rule["category"],
                "title": rule["title"],
                "description": rule["description"],
                "severity": rule["severity"],
                "distance": round(dist, 4),
                "similarity": round(sim, 4),
                "bad_example": rule.get("bad_example", ""),
                "good_example": rule.get("good_example", "")
            })
            
        results.sort(key=lambda x: x["distance"])
        return results[:top_k]

    def build_rag_context(self, code_diff: str, top_k: int = 2, threshold_sim: float = 0.15) -> str:
        """Retrieves top-k relevant SQA rules and formats them as RAG context for LLM prompt."""
        matches = self.vector_search(code_diff, top_k=top_k, metric="COSINE")
        relevant_rules = [m for m in matches if m["similarity"] >= threshold_sim]
        
        if not relevant_rules:
            return "No specific architectural SQA rules triggered from Oracle Vector Database."
            
        context_blocks = []
        for r in relevant_rules:
            block = (
                f"[Oracle 23ai Vector Match: {r['rule_id']} - {r['title']} (Similarity: {r['similarity']:.2f}, Severity: {r['severity']})]\n"
                f"Rule Description: {r['description']}\n"
                f"Defective Pattern: {r['bad_example']}\n"
                f"Compliant Fix: {r['good_example']}"
            )
            context_blocks.append(block)
            
        return "\n\n".join(context_blocks)
