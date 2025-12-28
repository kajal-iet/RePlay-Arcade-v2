from fastapi import APIRouter
from pydantic import BaseModel
from .logic import caesar_translate, SYMBOLS

router = APIRouter(prefix="/caesar")

class TranslateRequest(BaseModel):
    message: str
    key: int
    mode: str

class HackRequest(BaseModel):
    message: str

@router.post("/translate")
def translate(data: TranslateRequest):
    result = caesar_translate(data.message, data.key, data.mode)
    return { "result": result }

@router.post("/hack")
def hack(data: HackRequest):
    results = []
    for key in range(len(SYMBOLS)):
        text = caesar_translate(data.message, key, "decrypt")
        results.append({ "key": key, "text": text })
    return results
