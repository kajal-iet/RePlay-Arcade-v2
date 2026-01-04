from fastapi import APIRouter
from .logic import GAME, process_response
from .logic import GAME, process_response, get_level


router = APIRouter(prefix="/gullible")

@router.get("/state")
def state():
    return {
        "yes_count": GAME.yes_count,
        "finished": GAME.finished,
        "message": GAME.message,
        "level": get_level()   # 👈 THIS must exist
    }




@router.post("/respond")
async def respond(payload: dict):
    process_response(payload["text"])
    return {"ok": True}

@router.post("/reset")
def reset():
    GAME.reset()
    return {"ok": True}
