from fastapi import APIRouter
from pydantic import BaseModel
from .logic import process_roll

router = APIRouter(prefix="/diceroller")

class RollRequest(BaseModel):
    expression: str

@router.post("/roll")
def roll(data: RollRequest):
    try:
        return process_roll(data.expression)
    except:
        return {"error": "Invalid dice format"}
