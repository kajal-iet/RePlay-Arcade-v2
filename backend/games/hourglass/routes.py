from fastapi import APIRouter
from .logic import create_hourglass, step, render

router = APIRouter(prefix="/hourglass")

STATE = {
    "grid": create_hourglass()
}

@router.get("/frame")
def frame():
    moved = step(STATE["grid"])
    return {
        "frame": render(STATE["grid"]),
        "moved": moved
    }

@router.post("/reset")
def reset():
    STATE["grid"] = create_hourglass()
    return {"ok": True}
