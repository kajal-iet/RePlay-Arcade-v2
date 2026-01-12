import os
from sentence_transformers import SentenceTransformer
from backend.knowledge.vector_store import VectorStore

model = SentenceTransformer("all-MiniLM-L6-v2")

store = VectorStore(384)

if os.path.exists("backend/project_knowledge.index"):
    store.load("backend/project_knowledge")
    print("✅ Knowledge index loaded")
else:
    print("⚠️ Knowledge index not found. Run ingest_repo.py")



