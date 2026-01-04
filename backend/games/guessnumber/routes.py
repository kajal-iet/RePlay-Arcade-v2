from fastapi import APIRouter
from .logic import GAME, guess

router = APIRouter(prefix="/guessnumber")

@router.get("/state")
def state():
    return {
        "level": GAME.level,
        "max_num": GAME.max_num,
        "max_attempts": GAME.max_attempts,
        "attempts": GAME.attempts,
        "history": GAME.history,
        "over": GAME.over
    }

@router.post("/reset/{level}")
def reset(level: str):
    GAME.reset(level)
    return {"ok": True}

@router.post("/guess/{num}")
def make_guess(num: int):
    guess(num)
    return {"ok": True}
