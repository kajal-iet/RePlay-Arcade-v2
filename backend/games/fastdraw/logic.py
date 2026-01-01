import time, random

def start_round():
    wait = random.uniform(2, 4)
    return { "wait": wait }

def handle_click(draw_time, allowed):
    now = time.time()
    reaction = now - draw_time

    if reaction <= allowed:
        return {"result": "win", "reaction": round(reaction, 4)}
    else:
        return {"result": "lose", "reaction": round(reaction, 4)}
