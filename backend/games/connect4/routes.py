from fastapi import APIRouter
from .logic import GAME, drop, check_winner, PLAYER_X, PLAYER_O

router = APIRouter(prefix="/connect4")

@router.get("/state")
def state():
    return {
        "board": GAME.board,
        "player": GAME.player,
        "winner": GAME.winner
    }

@router.post("/drop/{col}")
def make_move(col: int):
    if GAME.winner is not None:
        return {"ok": False}

    row = drop(col)
    if row is None:
        return {"ok": False}

    if check_winner(GAME.player):
        GAME.winner = GAME.player
    else:
        GAME.player = PLAYER_O if GAME.player == PLAYER_X else PLAYER_X

    return {"ok": True}

@router.post("/reset")
def reset():
    GAME.reset()
    return {"ok": True}
