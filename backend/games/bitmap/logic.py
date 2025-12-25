import random

BITMAP = """
....................................................................
   *************   ***     ***   *************   *************
   *************   ***     ***   *************   *************
   ***             ***     ***   ***             ***          
   ***             ***     ***   ***             ***          
   *************   ***********   *************   *************
   *************   ***********   *************   *************
            ***   ***     ***             ***   ***     ***
            ***   ***     ***             ***   ***     ***
   *************   ***     ***   *************   *************
   *************   ***     ***   *************   *************
....................................................................
"""

def vary_color(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    r = min(255, max(0, r + random.randint(-40, 40)))
    g = min(255, max(0, g + random.randint(-40, 40)))
    b = min(255, max(0, b + random.randint(-40, 40)))

    return f"rgb({r},{g},{b})"

def generate(message, base_color):
    result = []
    idx = 0

    for line in BITMAP.splitlines():
        row = []
        for c in line:
            if c == "*":
                ch = message[idx % len(message)]
                idx += 1
                row.append([ch, vary_color(base_color)])
            else:
                row.append([" ", None])
        result.append(row)

    return result
