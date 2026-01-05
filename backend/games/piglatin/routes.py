from fastapi import APIRouter
from .logic import GAME

router = APIRouter(prefix="/piglatin")

@router.get("/state")
def state():
    return {
        "scores": GAME.scores,
        "turn": GAME.turn,
        "question": GAME.question
    }

@router.post("/submit/{text}")
def submit(text: str):
    if text.strip() == GAME.answer:
        GAME.scores[GAME.turn] += 1
    GAME.turn = 1 - GAME.turn
    GAME.new_round()
    return {"ok": True}

@router.post("/reset")
def reset():
    GAME.reset()
    return {"ok": True}
