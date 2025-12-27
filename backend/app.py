from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from games.bagels.routes import router as bagels_router
from games.birthday.routes import router as birthday_router   # 👈 add this
from games.bitmap.routes import router as bitmap_router
from games.blackjack.routes import router as blackjack_router
from games.dvd.routes import router as dvd_router
# from games.caesar.routes import router as caesar_router
from games.calendar.routes import router as calendar_router



app = FastAPI()

# CORS (already working for Bagels)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all game routes
app.include_router(bagels_router)
app.include_router(birthday_router)   # 👈 add this
app.include_router(bitmap_router)
app.include_router(blackjack_router)
app.include_router(dvd_router)
# app.include_router(caesar_router)
app.include_router(calendar_router)

