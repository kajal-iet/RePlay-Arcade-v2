from fastapi import APIRouter
from pydantic import BaseModel
from .logic import WORK_TIME, BREAK_TIME, next_pomodoro

router = APIRouter(prefix="/timer")

class StartRequest(BaseModel):
    mode: str
    seconds: int | None = None
    pomodoro_state: str

@router.post("/start")
def start(data: StartRequest):
    if data.mode == "countdown":
        return { "remaining": data.seconds }
    else:
        if data.pomodoro_state == "work":
            return { "remaining": WORK_TIME }
        else:
            return { "remaining": BREAK_TIME }

@router.post("/next")
def next_phase(state: dict):
    new_state, remaining = next_pomodoro(state["pomodoro_state"])
    return { "pomodoro_state": new_state, "remaining": remaining }
