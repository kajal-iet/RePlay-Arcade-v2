from fastapi import APIRouter
from pydantic import BaseModel
from .logic import *

router = APIRouter(prefix="/clickbait")

class GenerateRequest(BaseModel):
    count: int
    topic: str
    tone: str


@router.post("/generate")
def generate(req: GenerateRequest):
    words = [DEFAULT_OBJECT_PRONOUNS, DEFAULT_POSSESIVE_PRONOUNS, DEFAULT_PERSONAL_PRONOUNS,
             DEFAULT_STATES, DEFAULT_NOUNS, DEFAULT_PLACES, DEFAULT_WHEN]

    headlines = []

    for _ in range(req.count):
        h = generate_headline(words)

        if req.topic:
            h = h.replace(random.choice(DEFAULT_NOUNS), req.topic)

        if req.tone == "dramatic":
            h = h.upper() + "!!!"
        elif req.tone == "serious":
            h = h.replace("!", ".")

        headlines.append(h)

    return { "headlines": headlines }

