from fastapi import APIRouter
from pydantic import BaseModel
from .logic import roll_dice, JAPANESE_NUMBERS

router = APIRouter(prefix="/chohan")

class RollRequest(BaseModel):
    bet: int
    choice: str
    purse: int

@router.post("/roll")
def roll(data: RollRequest):
    if data.bet < 1:
        return { "error": "Invalid bet" }

    if data.bet > data.purse:
        return { "error": "Not enough funds" }
    d1, d2, total, correct = roll_dice()

    if data.choice == correct:
        fee = data.bet // 10
        net = data.bet - fee
        purse = data.purse + net
    else:
        net = -data.bet
        purse = data.purse - data.bet

    return {
        "d1": d1,
        "d2": d2,
        "total": total,
        "correct": correct,
        "net": net,
        "purse": purse,
        "j1": JAPANESE_NUMBERS[d1],
        "j2": JAPANESE_NUMBERS[d2]
    }
