class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.yes_count = 0
        self.finished = False
        self.message = ""

GAME = Game()

def process_response(text):
    cleaned = text.strip().lower()

    if GAME.finished:
        return

    if cleaned in ("n", "no"):
        GAME.finished = True

    elif cleaned in ("y", "yes"):
        GAME.yes_count += 1
        if GAME.yes_count % 5 == 0:
            GAME.message = "😄 Still waiting... aren’t you curious?"
        else:
            GAME.message = ""

    else:
        GAME.message = f'"{text}" is not a valid yes/no response.'

def get_level():
    y = GAME.yes_count
    if y < 5: return "Skeptic 🧐"
    if y < 15: return "Curious 😅"
    if y < 30: return "Gullible 😄"
    if y < 50: return "Very Gullible 🤭"
    return "Legendary Gullible 🏆"
