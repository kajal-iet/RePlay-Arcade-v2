from fastapi import APIRouter
from pydantic import BaseModel
from .logic import getBirthdays, getMatch, calculate_probabilities

router = APIRouter(prefix="/birthday")

class SimRequest(BaseModel):
    people: int
    simulations: int

class GraphRequest(BaseModel):
    start: int
    end: int

@router.post("/simulate")
def simulate(data: SimRequest):
    birthdays = getBirthdays(data.people)
    match = getMatch(birthdays)

    sim_match = sum(
        1 for _ in range(data.simulations)
        if getMatch(getBirthdays(data.people))
    )

    probability = round(sim_match / data.simulations * 100, 2)

    return {
        "birthdays": [b.strftime("%d %b") for b in birthdays],
        "match": match.strftime("%d %b") if match else None,
        "simulations": data.simulations,
        "people": data.people,
        "matches": sim_match,
        "probability": probability
    }

@router.post("/graph")
def graph(data: GraphRequest):
    sizes, values = calculate_probabilities(data.start, data.end)
    return {"sizes": sizes, "values": values}
