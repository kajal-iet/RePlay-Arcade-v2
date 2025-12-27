from fastapi import APIRouter
from .logic import init_logos, step

router = APIRouter(prefix="/dvd", tags=["DVD"])

@router.post("/start")
def start(data: dict):
    logos = init_logos(data["num"], data["width"], data["height"], data["size"])
    return { "logos": logos, "corner_hits": 0 }

@router.post("/frame")
def frame(data: dict):
    logos, hit = step(
        data["logos"],
        data["width"],
        data["height"],
        data["size"],
        data["speed"],
        data["random_colors"]
    )
    return {
        "logos": logos,
        "corner_hit": hit
    }
