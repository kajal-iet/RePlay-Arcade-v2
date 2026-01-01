from fastapi import APIRouter
from .logic import new_state, simulate, generate_fish, generate_crab, generate_kelp

router = APIRouter()
state = new_state()

@router.post("/step")
def step():
    global state
    state = simulate(state)
    return state

@router.post("/fish")
def add_fish():
    state["fishes"].append(generate_fish())
    return state

@router.post("/crab")
def add_crab():
    state["crabs"].append(generate_crab())
    return state

@router.post("/kelp")
def add_kelp():
    state["kelps"].append(generate_kelp())
    return state

@router.post("/feed")
def feed(payload: dict):
    state["foods"].append({"x": payload["x"], "y": payload["y"]})
    return state
