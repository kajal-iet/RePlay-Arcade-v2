from fastapi import APIRouter
from pydantic import BaseModel
from .logic import build_canvas, canvas_to_string, render_image

router = APIRouter(prefix="/etching")

class MoveRequest(BaseModel):
    moves: list[str]

@router.post("/draw")
def draw(req: MoveRequest):
    canvas, cx, cy = build_canvas(req.moves)
    return {"frame": canvas_to_string(canvas, cx, cy)}

@router.post("/export")
def export(req: MoveRequest):
    canvas, _, _ = build_canvas(req.moves)
    return {"png": render_image(canvas)}
