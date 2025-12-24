from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from games.bagels.routes import router as bagels_router
from games.birthday.routes import router as birthday_router   # 👈 add this

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
