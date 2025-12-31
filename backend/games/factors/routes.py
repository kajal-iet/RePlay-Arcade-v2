from fastapi import APIRouter
from pydantic import BaseModel
from .logic import find_factors

router = APIRouter(prefix="/factors")

class Req(BaseModel):
    number: int

@router.post("/analyze")
def analyze(req: Req):
    return find_factors(req.number)
