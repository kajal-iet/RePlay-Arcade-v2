from fastapi import APIRouter
from pydantic import BaseModel
from .logic import generate_board

router = APIRouter(prefix="/dicemath")

class QuestionRequest(BaseModel):
    min_dice: int
    max_dice: int

@router.post("/question")
def question(data: QuestionRequest):
    board, answer = generate_board(data.min_dice, data.max_dice)
    return {"board": board, "answer": answer}
