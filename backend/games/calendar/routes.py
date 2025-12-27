from fastapi import APIRouter
from pydantic import BaseModel
from .logic import build_calendar
import json, os

router = APIRouter(prefix="/calendar", tags=["Calendar"])

NOTES_FILE = "calendar_notes.json"

if os.path.exists(NOTES_FILE):
    with open(NOTES_FILE) as f:
        NOTES = json.load(f)
else:
    NOTES = {}

class CalendarRequest(BaseModel):
    year: int
    month: int

class NoteRequest(BaseModel):
    date: str
    text: str

@router.post("/get")
def get_calendar(data: CalendarRequest):
    return build_calendar(data.year, data.month, NOTES)

@router.post("/save-note")
def save_note(data: NoteRequest):
    NOTES[data.date] = data.text
    with open(NOTES_FILE, "w") as f:
        json.dump(NOTES, f, indent=2)
    return {"status": "saved"}
