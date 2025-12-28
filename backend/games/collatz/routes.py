from fastapi import APIRouter
from pydantic import BaseModel
from .logic import collatz_sequence

router = APIRouter(prefix="/collatz")

class SingleRequest(BaseModel):
    n: int

class CompareRequest(BaseModel):
    numbers: list[int]

@router.post("/single")
def single(data: SingleRequest):
    seq = collatz_sequence(data.n)
    return {
        "sequence": seq,
        "length": len(seq),
        "max": max(seq),
        "odd": sum(x % 2 for x in seq),
        "even": sum(x % 2 == 0 for x in seq)
    }

@router.post("/compare")
def compare(data: CompareRequest):
    results = []
    for n in data.numbers:
        seq = collatz_sequence(n)
        results.append({
            "start": n,
            "length": len(seq),
            "max": max(seq)
        })
    return results
