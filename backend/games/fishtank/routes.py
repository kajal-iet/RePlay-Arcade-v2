from fastapi import APIRouter
from .logic import add_fish, add_crab, add_kelp, update, render

router = APIRouter(prefix="/fishtank")

@router.get("/frame")
def frame():
    update()
    return {"frame": render()}

@router.post("/fish")
def fish(): add_fish(); return {"ok": True}

@router.post("/crab")
def crab(): add_crab(); return {"ok": True}

@router.post("/kelp")
def kelp(): add_kelp(); return {"ok": True}
