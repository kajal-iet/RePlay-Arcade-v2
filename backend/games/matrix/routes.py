from fastapi import APIRouter
from pydantic import BaseModel
from .logic import get_matrix_config

router = APIRouter(prefix="/matrix")

class ModeRequest(BaseModel):
    mode: str

@router.post("/config")
def matrix_config(data: ModeRequest):
    return get_matrix_config(data.mode)
