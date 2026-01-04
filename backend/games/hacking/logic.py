import random

WORDS = [
    "MONITOR","CONTAIN","RESOLVE","CHICKEN","ADDRESS",
    "DESPITE","DISPLAY","PENALTY","IMPROVE","REFUGEE",
    "CAPTURE","COMPUTE","HANGING","MISSION","NETWORK"
]

MAX_TRIES = 4

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.words = random.sample(WORDS, 12)
        self.secret = random.choice(self.words)
        self.tries = 0
        self.logs = []
        self.locked = False

GAME = Game()

def matching_letters(a, b):
    return sum(1 for i in range(len(a)) if a[i] == b[i])

def heat_label(matches):
    if matches <= 1: return "🧊 Cold"
    if matches <= 4: return "🌡 Warm"
    return "🔥 Hot"

def submit_guess(guess):
    if GAME.locked: return

    if guess not in GAME.words:
        GAME.logs.append("INVALID INPUT — NOT IN MEMORY")
        return

    GAME.tries += 1
    matches = matching_letters(GAME.secret, guess)
    heat = heat_label(matches)

    if guess == GAME.secret:
        GAME.logs.append("A C C E S S   G R A N T E D")
        GAME.locked = True
    else:
        GAME.logs.append(f"ACCESS DENIED ({matches}/7 correct) — {heat}")

    if GAME.tries >= MAX_TRIES and not GAME.locked:
        GAME.logs.append(f"SYSTEM LOCKED — PASSWORD WAS {GAME.secret}")
        GAME.locked = True
