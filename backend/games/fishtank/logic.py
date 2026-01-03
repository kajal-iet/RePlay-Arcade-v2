import random

WIDTH = 70
HEIGHT = 25

FISH_TYPES = ["><>","<><",">||>","<||<",">))>","<[[<"]
CRAB_FRAMES = ["(\\_/)", "=(\\_/)"]
KELP_CHARS = ["(", ")"]

class Tank:
    def __init__(self):
        self.fishes = []
        self.crabs = []
        self.kelps = []
        self.bubbles = []
        self.bubblers = [10, 30, 55]
        self.frame = 0

GAME = Tank()

# ---------------- SPAWNERS ----------------

def add_fish():
    GAME.fishes.append({
        "x": random.randint(2, WIDTH-10),
        "y": random.randint(3, HEIGHT-6),
        "shape": random.choice(FISH_TYPES),
        "dir": random.choice([-1,1])
    })

def add_crab():
    GAME.crabs.append({
        "x": random.randint(2, WIDTH-10),
        "y": HEIGHT-3,
        "frame": 0,
        "dir": random.choice([-1,1])
    })

def add_kelp():
    height = random.randint(5, 12)
    GAME.kelps.append({
        "x": random.randint(1, WIDTH-2),
        "segments": [random.choice(KELP_CHARS) for _ in range(height)]
    })

# ---------------- SIMULATION ----------------

def update():
    GAME.frame += 1

    # Fish swim
    for f in GAME.fishes:
        f["x"] += f["dir"]
        if f["x"] <= 0 or f["x"] >= WIDTH-5:
            f["dir"] *= -1

    # Crabs walk
    for c in GAME.crabs:
        c["x"] += c["dir"]
        if c["x"] <= 0 or c["x"] >= WIDTH-5:
            c["dir"] *= -1
        c["frame"] = (c["frame"] + 1) % 2

    # Kelp waves
    for k in GAME.kelps:
        for i in range(len(k["segments"])):
            if random.randint(1, 10) == 1:
                k["segments"][i] = "(" if k["segments"][i] == ")" else ")"

    # Bubble generators
    for b in GAME.bubblers:
        if random.randint(1, 6) == 1:
            GAME.bubbles.append({"x": b, "y": HEIGHT-4})

    # Bubbles rise
    for bub in GAME.bubbles:
        bub["y"] -= 1

    GAME.bubbles = [b for b in GAME.bubbles if b["y"] > 0]

# ---------------- RENDER ----------------

def render():
    grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Kelp
    for k in GAME.kelps:
        for i, seg in enumerate(k["segments"]):
            y = HEIGHT - 2 - i
            x = k["x"] if seg == "(" else k["x"] + 1
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                grid[y][x] = seg

    # Bubbles
    for b in GAME.bubbles:
        if 0 <= b["x"] < WIDTH and 0 <= b["y"] < HEIGHT:
            grid[b["y"]][b["x"]] = "o"

    # Fish
    for f in GAME.fishes:
        for i,ch in enumerate(f["shape"]):
            x = f["x"]+i
            if 0 <= x < WIDTH:
                grid[f["y"]][x] = ch

    # Crabs
    for c in GAME.crabs:
        frame = CRAB_FRAMES[c["frame"]]
        for i,ch in enumerate(frame):
            x = c["x"]+i
            if 0 <= x < WIDTH:
                grid[c["y"]][x] = ch

    # Sand
    for x in range(WIDTH):
        grid[HEIGHT-1][x] = "░"

    return "\n".join("".join(row) for row in grid)
