from pathlib import Path
from sentence_transformers import SentenceTransformer
from backend.knowledge.vector_store import VectorStore


model = SentenceTransformer("all-MiniLM-L6-v2")

ROOT = Path(__file__).resolve().parents[2]
FILES = [".py", ".js", ".jsx", ".md"]

def chunk(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

store = VectorStore(384)

chunks = []

for file in ROOT.rglob("*"):
    if file.suffix in FILES:
        try:
         text = file.read_text(encoding="utf-8", errors="ignore")
        except:
            continue


        for part in chunk(text):
            chunks.append(f"{file}\n{part}")

embeddings = model.encode(chunks)
store.add(embeddings, chunks)
store.save("project_knowledge")
