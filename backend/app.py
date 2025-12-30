from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from games.bagels.routes import router as bagels_router
from games.birthday.routes import router as birthday_router   # 👈 add this
from games.bitmap.routes import router as bitmap_router
from games.blackjack.routes import router as blackjack_router
from games.dvd.routes import router as dvd_router
from games.caesar.routes import router as caesar_router
from games.calendar.routes import router as calendar_router
from games.carrot.routes import router as carrot_router
from games.chohan.routes import router as chohan_router
from games.clickbait.routes import router as clickbait_router
from games.collatz.routes import router as collatz_router
from games.timer.routes import router as timer_router
from games.diamonds.routes import router as diamonds_router
from games.dicemath.routes import router as dicemath_router
from games.diceroller.routes import router as diceroller_router
from games.matrix.routes import router as matrix_router
from games.ducklings.routes import router as ducklings_router

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
app.include_router(caesar_router)
app.include_router(calendar_router)
app.include_router(carrot_router)
app.include_router(chohan_router)
app.include_router(clickbait_router)
app.include_router(collatz_router)
app.include_router(timer_router)
app.include_router(diamonds_router)
app.include_router(dicemath_router)
app.include_router(diceroller_router)
app.include_router(matrix_router)
app.include_router(ducklings_router)

