from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.games.bagels.routes import router as bagels_router
from backend.games.birthday.routes import router as birthday_router   # 👈 add this
from backend.games.bitmap.routes import router as bitmap_router
from backend.games.blackjack.routes import router as blackjack_router
from backend.games.dvd.routes import router as dvd_router
from backend.games.caesar.routes import router as caesar_router
from backend.games.calendar.routes import router as calendar_router
from backend.games.carrot.routes import router as carrot_router
from backend.games.chohan.routes import router as chohan_router
from backend.games.clickbait.routes import router as clickbait_router
from backend.games.collatz.routes import router as collatz_router
from backend.games.timer.routes import router as timer_router
from backend.games.diamonds.routes import router as diamonds_router
from backend.games.dicemath.routes import router as dicemath_router
from backend.games.diceroller.routes import router as diceroller_router
from backend.games.matrix.routes import router as matrix_router
from backend.games.ducklings.routes import router as ducklings_router
from backend.games.etching.routes import router as etching_router
from backend.games.factors.routes import router as factors_router
from backend.games.fibonacci.routes import router as fibonacci_router
from backend.games.fastdraw.routes import router as fastdraw_router
from backend.games.fishtank.routes import router as fishtank_router
from backend.games.flooder.routes import router as flooder_router
from backend.games.connect4.routes import router as connect4_router
from backend.games.guessnumber.routes import router as guessnumber_router
from backend.games.gullible.routes import router as gullible_router
from backend.games.hacking.routes import router as hacking_router
from backend.games.hangman.routes import router as hangman_router
from backend.games.pattern_carpet.routes import router as pattern_carpet_router
from backend.games.hourglass.routes import router as hourglass_router
# from games.robots.routes import router as robots_router
from backend.games.piglatin.routes import router as piglatin_router
from backend.games.bagels.guide import router as bagels_guide_router
from backend.games.birthday.guide import router as birthday_guide_router


from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()

import os

print("KEY PRESENT:", bool(os.getenv("GOOGLE_API_KEY")))


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
app.include_router(etching_router)
app.include_router(factors_router)
app.include_router(fibonacci_router)
app.include_router(fastdraw_router)
app.include_router(fastdraw_router)
app.include_router(fishtank_router)
app.include_router(flooder_router)
app.include_router(connect4_router)
app.include_router(guessnumber_router)
app.include_router(gullible_router)
app.include_router(hacking_router)
app.include_router(hangman_router)
app.include_router(pattern_carpet_router)
app.include_router(hourglass_router)
# app.include_router(robots_router)
app.include_router(piglatin_router)
app.include_router(bagels_guide_router)
app.include_router(birthday_guide_router)