from fastapi import APIRouter
from .logic import GAME, submit_guess, CATEGORIES, HANGMAN_PICS

router = APIRouter(prefix="/hangman")

@router.get("/state")
def state():
    return {
        "category": GAME.category,
        "secret": GAME.secret,
        "correct": GAME.correct,
        "missed": GAME.missed,
        "logs": GAME.logs,
        "locked": GAME.locked,
        "wins": GAME.wins,
        "losses": GAME.losses,
        "pics": HANGMAN_PICS,
        "categories": list(CATEGORIES.keys())
    }

@router.post("/guess/{letter}")
def guess(letter: str):
    submit_guess(letter.upper())
    return {"ok": True}

@router.post("/reset/{category}")
def reset(category: str):
    GAME.reset(category)
    return {"ok": True}
