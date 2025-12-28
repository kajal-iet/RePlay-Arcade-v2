import random

DICE = [
(['+-------+','|       |','|   O   |','|       |','+-------+'], 1),
(['+-------+','| O     |','|       |','|     O |','+-------+'], 2),
(['+-------+','|     O |','|       |','| O     |','+-------+'], 2),
(['+-------+','| O     |','|   O   |','|     O |','+-------+'], 3),
(['+-------+','|     O |','|   O   |','| O     |','+-------+'], 3),
(['+-------+','| O   O |','|       |','| O   O |','+-------+'], 4),
(['+-------+','| O   O |','|   O   |','| O   O |','+-------+'], 5),
(['+-------+','| O   O |','| O   O |','| O   O |','+-------+'], 6),
(['+-------+','| O O O |','|       |','| O O O |','+-------+'], 6)
]

def generate_board(min_dice, max_dice):
    canvas = [[" " for _ in range(60)] for _ in range(15)]
    used = []
    total = 0
    count = random.randint(min_dice, max_dice)

    for _ in range(count):
        face, value = random.choice(DICE)
        total += value

        while True:
            x = random.randint(0, 51)
            y = random.randint(0, 10)
            if not any(px <= x < px+9 and py <= y < py+5 for px,py in used):
                used.append((x,y))
                break

        for dy in range(5):
            for dx in range(9):
                canvas[y+dy][x+dx] = face[dy][dx]

    board = "\n".join("".join(r) for r in canvas)
    return board, total
