from fastapi import APIRouter
from pydantic import BaseModel
from .logic import outline, filled, rotate

router = APIRouter(prefix="/diamonds")

class GenerateRequest(BaseModel):
    size: int
    type: str

class RotateRequest(BaseModel):
    lines: list[str]

@router.post("/generate")
def generate(data: GenerateRequest):
    lines = outline(data.size) if data.type == "Outline" else filled(data.size)
    return { "lines": lines }

@router.post("/rotate")
def rotate_lines(data: RotateRequest):
    return { "lines": rotate(data.lines) }
