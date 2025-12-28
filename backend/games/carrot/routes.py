from fastapi import APIRouter
from pydantic import BaseModel
from .logic import new_round, reveal

router = APIRouter(prefix="/carrot")

class StartRequest(BaseModel):
    p1: str
    p2: str

class SwapRequest(BaseModel):
    carrot_in_red: bool
    swapped: bool

@router.post("/start")
def start(data: StartRequest):
    round_data = new_round()
    return {
        "p1": data.p1,
        "p2": data.p2,
        **round_data
    }

@router.post("/reveal")
def reveal_route(data: SwapRequest):
    winner = reveal(data.carrot_in_red, data.swapped)
    return { "winner": winner }
