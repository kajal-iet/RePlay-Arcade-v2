from fastapi import APIRouter
from pydantic import BaseModel
from .logic import generate

router = APIRouter(prefix="/bitmap")

class BitmapRequest(BaseModel):
    message: str
    color: str

@router.post("/generate")
def generate_bitmap(data: BitmapRequest):
    grid = generate(data.message, data.color)
    return {"grid": grid}
