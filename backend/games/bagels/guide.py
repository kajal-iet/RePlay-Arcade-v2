import json
from pathlib import Path
from fastapi import APIRouter, Request
from backend.ai.adk_client import create_game_guide_agent
from backend.knowledge.retriever import retrieve_context
from backend.ai.session_store import store
from uuid import uuid4



router = APIRouter(prefix="/bagels/guide")

BASE = Path(__file__).parent

def load_context():
    logic = (BASE / "logic.py").read_text()
    routes = (BASE / "routes.py").read_text()
    docs = (BASE / "docs.md").read_text()
    meta = json.loads((BASE / "context.json").read_text())

    return f"""
METADATA:
{json.dumps(meta, indent=2)}

DOCUMENTATION:
{docs}

BACKEND LOGIC:
{logic}

API ROUTES:
{routes}
"""

@router.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_msg = body["message"]
    session_id = body.get("session") or str(uuid4())

    store.add(session_id, "user", user_msg)

    history = store.get(session_id)
    relevant_code = retrieve_context(user_msg)

    context = load_context()

    full_context = f"""
        {context}

        RELEVANT PROJECT CODE:
        {relevant_code}

        CONVERSATION SO FAR:
        {history}
        """

    agent = create_game_guide_agent(full_context)
    response = agent.generate(user_msg)

    store.add(session_id, "ai", response.text)

    return {"reply": response.text, "session": session_id}
