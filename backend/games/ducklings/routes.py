from fastapi import APIRouter
from pydantic import BaseModel
from .logic import generate_ducks

router = APIRouter(prefix="/ducklings")

class DuckRequest(BaseModel):
    count: int
    seasonal: bool

@router.post("/generate")
def generate(data: DuckRequest):
    return generate_ducks(data.count, data.seasonal)
