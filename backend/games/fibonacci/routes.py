from fastapi import APIRouter
from pydantic import BaseModel
from .logic import fib_fast, fib_safe, build_timeline

router = APIRouter(prefix="/fibonacci")

class Req(BaseModel):
    n: int
    mode: str

@router.post("/compute")
def compute(req: Req):
    if req.mode == "iterative":
        value = fib_fast(req.n)
        timeline = build_timeline(req.n)
    else:
        value = fib_safe(req.n)
        timeline = build_timeline(req.n)

    phi = None
    if req.n >= 3:
        phi = fib_fast(req.n) / fib_fast(req.n - 1)

    return {
        "value": value,
        "timeline": timeline,
        "phi": phi
    }
