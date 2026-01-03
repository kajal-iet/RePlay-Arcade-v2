from fastapi import APIRouter
from .logic import GAME, flood_fill, has_won

router = APIRouter(prefix="/flooder")

@router.get("/state")
def get_state():
    board = [[GAME.board[(x, y)] for x in range(12)] for y in range(10)]
    return {
        "board": board,
        "moves": GAME.moves,
        "message": GAME.message,
        "won": has_won()
    }

@router.post("/pick/{tile}")
def pick(tile: int):
    if GAME.moves <= 0:
        return {"ok": False}

    changed = flood_fill(0, 0, tile)
    if not changed:
        GAME.message = "Already that color"
        return {"ok": False}

    GAME.moves -= 1

    if has_won():
        GAME.message = "🎉 You won!"
    elif GAME.moves == 0:
        GAME.message = "💀 Out of moves!"
    else:
        GAME.message = f"Picked color {tile}"

    return {"ok": True}

@router.post("/reset")
def reset():
    GAME.reset()
    return {"ok": True}
