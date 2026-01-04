from fastapi import APIRouter
from .logic import game, CATEGORIES, HANGMAN_PICS, GUILLOTINE_PICS

router = APIRouter()

@router.get("/state")
def get_state():
    return game.__dict__

@router.post("/start")
def start(category: str):
    game.reset(category)
    return {"ok": True}

@router.post("/guess")
def guess(letter: str):
    letter = letter.upper()

    if game.game_over:
        return {"ok": False}

    if letter in game.missed + game.correct:
        return {"ok": True}

    if letter in game.secret:
        game.correct.append(letter)
        if all(c in game.correct for c in game.secret):
            game.message = f"🎉 YOU WON! Word was {game.secret}"
            game.game_over = True
    else:
        game.missed.append(letter)
        if game.style == "Hangman" and len(game.missed) == len(HANGMAN_PICS) - 1:
            game.message = f"💀 GAME OVER — Word was {game.secret}"
            game.game_over = True
        if game.style == "Guillotine" and len(game.missed) == len(GUILLOTINE_PICS) - 1:
            game.message = f"💀 GAME OVER — Word was {game.secret}"
            game.game_over = True

    return {"ok": True}

@router.post("/style")
def set_style(style: str):
    game.style = style
    return {"ok": True}

@router.get("/pics")
def get_pics():
    return {
        "hangman": HANGMAN_PICS,
        "guillotine": GUILLOTINE_PICS
    }

@router.get("/categories")
def get_categories():
    return list(CATEGORIES.keys())
