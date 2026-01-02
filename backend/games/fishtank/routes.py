from fastapi import APIRouter
from .logic import GAME_TANK, generate_fish, generate_crab, update, render

router = APIRouter()

@router.get("/frame")
def get_frame():
    update()
    return {"frame": render()}

@router.post("/fish")
def add_fish():
    GAME_TANK.fishes.append(generate_fish())
    return {"ok": True}

@router.post("/crab")
def add_crab():
    GAME_TANK.crabs.append(generate_crab())
    return {"ok": True}
