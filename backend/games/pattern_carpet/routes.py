from fastapi import APIRouter
from .logic import GAME, apply_changes, build_carpet, generate_image

router = APIRouter(prefix="/carpet")

@router.get("/state")
def state():
    return {
        "pattern": GAME.pattern,
        "x": GAME.x,
        "y": GAME.y,
        "bg": GAME.bg,
        "output": build_carpet()
    }

@router.post("/apply")
def apply(data: dict):
    apply_changes(data["pattern"], data["x"], data["y"], data["bg"])
    return {"ok": True}

@router.get("/image")
def image():
    return generate_image()
