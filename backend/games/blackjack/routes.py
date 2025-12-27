from fastapi import APIRouter
from .logic import *

router = APIRouter(prefix="/blackjack")

game = {
    "deck": [],
    "player": [],
    "dealer": []
}

@router.post("/start")
def start():
    game["deck"] = getDeck()
    game["player"] = [game["deck"].pop(), game["deck"].pop()]
    game["dealer"] = [game["deck"].pop(), game["deck"].pop()]
    return game

@router.post("/hit")
def hit():
    game["player"].append(game["deck"].pop())
    return game

@router.post("/stand")
def stand():
    game["dealer"] = dealerPlay(game["deck"], game["dealer"])
    return game
