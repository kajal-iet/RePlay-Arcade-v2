from fastapi import APIRouter
from .logic import start_round, trigger_draw, click, get_stats, reset, GAME
import time, random

router = APIRouter(prefix="/fastdraw")

@router.post("/start")
def start():
    start_round()
    wait = random.uniform(2,4)
    time.sleep(wait)
    trigger_draw()
    return {"phase": GAME.phase}

@router.post("/click")
def player_click(allowed: float):
    result = click(allowed)
    return {"result": result}

@router.get("/stats")
def stats():
    return get_stats()

@router.post("/reset")
def reset_game():
    reset()
    return {"ok": True}
