# from fastapi import APIRouter
# from pydantic import BaseModel
# from .logic import translate, hack

# router = APIRouter(prefix="/caesar", tags=["Caesar Cipher"])


# class TranslateRequest(BaseModel):
#     message: str
#     key: int
#     mode: str


# class HackRequest(BaseModel):
#     message: str


# @router.post("/translate")
# def caesar_translate(data: TranslateRequest):
#     output = translate(data.message, data.key, data.mode)
#     return {"output": output}


# @router.post("/hack")
# def caesar_hack(data: HackRequest):
#     results = hack(data.message)
#     return {"results": results}
