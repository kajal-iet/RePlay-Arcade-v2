import time, random

class Game:
    def __init__(self):
        self.phase = "idle"
        self.draw_time = None
        self.attempts = 0
        self.wins = 0
        self.losses = 0
        self.times = []

GAME = Game()

def start_round():
    GAME.phase = "waiting"
    GAME.draw_time = None

def trigger_draw():
    GAME.draw_time = time.time()
    GAME.phase = "draw"

def click(allowed):
    if GAME.phase != "draw":
        return None

    reaction = time.time() - GAME.draw_time
    GAME.attempts += 1

    if reaction <= allowed:
        GAME.wins += 1
        result = "win"
    else:
        GAME.losses += 1
        result = "lose"

    GAME.times.append(reaction)
    GAME.phase = "idle"
    GAME.draw_time = None

    return result, round(reaction, 4)

def get_stats():
    return {
        "attempts": GAME.attempts,
        "wins": GAME.wins,
        "losses": GAME.losses,
        "times": GAME.times,
        "phase": GAME.phase
    }

def reset():
    GAME.__init__()
