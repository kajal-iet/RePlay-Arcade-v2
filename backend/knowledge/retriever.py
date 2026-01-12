from sentence_transformers import SentenceTransformer
from backend.knowledge.vector_store import VectorStore


model = SentenceTransformer("all-MiniLM-L6-v2")

store = VectorStore(384)
store.load("project_knowledge")

def retrieve_context(query, k=5):
    embedding = model.encode(query)
    return "\n\n".join(store.search(embedding, k))
