from pathlib import Path
from sentence_transformers import SentenceTransformer
from backend.knowledge.vector_store import VectorStore

model = SentenceTransformer("all-MiniLM-L6-v2")

# Only ingest these folders
ROOT = Path(__file__).resolve().parents[2]
TARGET_DIRS = ["backend/games", "backend/ai", "frontend"]

FILES = [".py", ".js", ".jsx", ".md"]

def chunk(text, size=600):
    return [text[i:i+size] for i in range(0, len(text), size)]

store = VectorStore(384)
chunks = []

for folder in TARGET_DIRS:
    base = ROOT / folder
    for file in base.rglob("*"):
        if file.suffix in FILES:
            try:
                text = file.read_text(encoding="utf-8", errors="ignore")
                for part in chunk(text):
                    chunks.append(f"{file}\n{part}")
            except:
                continue

print(f"🔹 Total chunks: {len(chunks)}")

embeddings = model.encode(chunks, show_progress_bar=True)
store.add(embeddings, chunks)
store.save("backend/project_knowledge")

print("✅ Knowledge index built")
