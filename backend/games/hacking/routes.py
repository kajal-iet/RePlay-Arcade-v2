from fastapi import APIRouter
from .logic import GAME, submit_guess

router = APIRouter(prefix="/hacking")

@router.get("/state")
def state():
    return {
        "words": GAME.words,
        "logs": GAME.logs,
        "tries": GAME.tries,
        "locked": GAME.locked
    }

@router.post("/guess/{word}")
def guess(word: str):
    submit_guess(word.upper())
    return {"ok": True}

@router.post("/reset")
def reset():
    GAME.reset()
    return {"ok": True}
