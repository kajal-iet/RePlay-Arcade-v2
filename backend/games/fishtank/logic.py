import random

WIDTH = 70
HEIGHT = 25

FISH_TYPES = [
    {'right': ['><>'], 'left': ['<><']},
    {'right': ['>||>'], 'left': ['<||<']},
    {'right': ['>))>'], 'left': ['<[[<']},
]

CRAB_FRAMES = ["(\\_/)", "(=\\_/)"]
SAND_CHAR = "░"
KELP_CHARS = ["(", ")"]

def new_state():
    return {
        "fishes": [],
        "crabs": [],
        "foods": [],
        "kelps": [],
        "bubbles": [],
        "bubblers": [10, 30, 55],
        "frame": 0,
    }

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
        "y": HEIGHT-2,
        "dir": random.choice([1, -1]),
        "frame": 0
    }

def generate_kelp():
    height = random.randint(5, 12)
    return {
        "x": random.randint(1, WIDTH - 2),
        "segments": [random.choice(KELP_CHARS) for _ in range(height)]
    }

def simulate(state):
    for fish in state["fishes"]:
        if state["foods"]:
            target = min(state["foods"], key=lambda f: abs(f["x"]-fish["x"]) + abs(f["y"]-fish["y"]))
            fish["x"] += (target["x"] > fish["x"]) - (target["x"] < fish["x"])
            fish["y"] += (target["y"] > fish["y"]) - (target["y"] < fish["y"])
            fish["dir"] = 1 if target["x"] > fish["x"] else -1
        elif state["frame"] % fish["speed"] == 0:
            fish["x"] += fish["dir"]
            if fish["x"] <= 0 or fish["x"] >= WIDTH-4:
                fish["dir"] *= -1

    for crab in state["crabs"]:
        crab["x"] += crab["dir"]
        if crab["x"] <= 0 or crab["x"] >= WIDTH-6:
            crab["dir"] *= -1
        crab["frame"] = (crab["frame"] + 1) % 2

    for kelp in state["kelps"]:
        for i in range(len(kelp["segments"])):
            if random.randint(1, 10) == 1:
                kelp["segments"][i] = "(" if kelp["segments"][i] == ")" else ")"

    for b in state["bubblers"]:
        if random.randint(1, 6) == 1:
            state["bubbles"].append({"x": b, "y": HEIGHT-3})

    for bubble in state["bubbles"]:
        bubble["y"] -= 1

    state["bubbles"] = [b for b in state["bubbles"] if b["y"] > 0]

    for food in state["foods"]:
        food["y"] += 1

    state["foods"] = [f for f in state["foods"] if f["y"] < HEIGHT-2]

    state["frame"] += 1
    return state
