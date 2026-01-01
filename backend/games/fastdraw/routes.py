from fastapi import APIRouter
from .logic import start_round, handle_click

router = APIRouter(prefix="/fastdraw")

@router.post("/start")
def start():
    return start_round()

@router.post("/click")
def click(payload: dict):
    return handle_click(payload["draw_time"], payload["allowed"])
