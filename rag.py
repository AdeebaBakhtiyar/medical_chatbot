import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents(folder="docs"):
    docs, file_names = [], []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
                file_names.append(file)
    return docs, file_names

def build_faiss_index(docs):
    embeddings = embedding_model.encode(docs)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings

def get_most_similar(query, docs, index, embeddings):
    query_embedding = embedding_model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    return docs[I[0][0]]
