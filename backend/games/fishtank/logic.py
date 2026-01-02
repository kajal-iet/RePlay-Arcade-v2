import random
from typing import List

WIDTH = 70
HEIGHT = 25

FISH_TYPES = [
    {'right': ['><>'], 'left': ['<><']},
    {'right': ['>||>'], 'left': ['<||<']},
    {'right': ['>))>'], 'left': ['<[[<']},
]

CRAB_FRAMES = ["(\\_/)", "=(\\_/)"]

class Tank:
    def __init__(self):
        self.fishes: List[dict] = []
        self.crabs: List[dict] = []
        self.frame: int = 0

# 🔒 GLOBAL SINGLETON — PERSISTS ACROSS REQUESTS
GAME_TANK = Tank()

def generate_fish():
    f = random.choice(FISH_TYPES)
    return {
        "x": random.randint(0, WIDTH-4),
        "y": random.randint(2, HEIGHT-6),
        "right": f['right'],
        "left": f['left'],
        "dir": random.choice([1, -1]),
        "speed": random.randint(3, 6)
    }

def generate_crab():
    return {
        "x": random.randint(0, WIDTH-6),
        "y": HEIGHT - 2,
        "dir": random.choice([1, -1]),
        "frame": 0
    }

def update():
    for fish in GAME_TANK.fishes:
        if GAME_TANK.frame % fish["speed"] == 0:
            fish["x"] += fish["dir"]
            if fish["x"] <= 0 or fish["x"] >= WIDTH - 4:
                fish["dir"] *= -1

    for c in GAME_TANK.crabs:
        c["x"] += c["dir"]
        if c["x"] <= 0 or c["x"] >= WIDTH - 6:
            c["dir"] *= -1
        c["frame"] = (c["frame"] + 1) % 2

    GAME_TANK.frame += 1

def render():
    grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for f in GAME_TANK.fishes:
        char = f["right"][0] if f["dir"] == 1 else f["left"][0]
        for i, ch in enumerate(char):
            grid[f["y"]][f["x"] + i] = ch

    for c in GAME_TANK.crabs:
        char = CRAB_FRAMES[c["frame"]]
        for i, ch in enumerate(char):
            grid[c["y"]][c["x"] + i] = ch

    return "\n".join("".join(row) for row in grid)
