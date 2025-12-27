import random

def random_color():
    return [random.randint(80, 255) for _ in range(3)]

def init_logos(num, width, height, size):
    logos = []
    for _ in range(num):
        logos.append({
            "x": random.randint(0, width - size),
            "y": random.randint(0, height - size),
            "dx": random.choice([-1, 1]),
            "dy": random.choice([-1, 1]),
            "color": random_color()
        })
    return logos

def step(logos, width, height, size, speed, random_colors):
    corner_hit = False

    for logo in logos:
        logo["x"] += logo["dx"] * speed
        logo["y"] += logo["dy"] * speed

        hit_x = hit_y = False

        if logo["x"] <= 0 or logo["x"] + size >= width:
            logo["dx"] *= -1
            hit_x = True

        if logo["y"] <= 0 or logo["y"] + size >= height:
            logo["dy"] *= -1
            hit_y = True

        if hit_x and hit_y:
            corner_hit = True

        if random_colors and (hit_x or hit_y):
            logo["color"] = random_color()

    return logos, corner_hit
