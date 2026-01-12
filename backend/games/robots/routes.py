# from fastapi import APIRouter
# from .logic import GAME

# router = APIRouter(prefix="/robots")

# @router.get("/state")
# def state():
#     return {
#         "frame": render_board(),
#         "robots": len(GAME.robots),
#         "score": GAME.score,
#         "teleports": GAME.teleports,
#         "over": GAME.over

#     }

# @router.post("/move/{dx}/{dy}")
# def move(dx: int, dy: int):
#     GAME.step((dx, dy))
#     return {"ok": True}

# @router.post("/teleport")
# def teleport():
#     GAME.step(teleport=True)
#     return {"ok": True}

# @router.post("/reset")
# def reset():
#     GAME.reset()
#     return {"ok": True}
