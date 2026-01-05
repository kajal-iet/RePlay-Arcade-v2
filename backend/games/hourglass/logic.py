import random

WIDTH = 30
HEIGHT = 24
SAND = "●"
EMPTY = " "
WALL = "#"

def glass_bounds(y):
    mid = HEIGHT // 2
    neck = 2
    spread = (mid - y) // 2 if y < mid else (y - mid) // 2
    center = WIDTH // 2
    return center - neck - spread, center + neck + spread

def inside_glass(x, y):
    left, right = glass_bounds(y)
    return left < x < right

def create_hourglass():
    grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for y in range(HEIGHT):
        l, r = glass_bounds(y)
        grid[y][l] = WALL
        grid[y][r] = WALL

    for y in range(3, HEIGHT // 2 - 1):
        l, r = glass_bounds(y)
        for x in range(l + 1, r):
            grid[y][x] = SAND

    return grid

def step(grid):
    moved = False

    for y in range(HEIGHT - 2, -1, -1):
        xs = list(range(1, WIDTH - 1))
        random.shuffle(xs)

        for x in xs:
            if grid[y][x] != SAND:
                continue

            if grid[y + 1][x] == EMPTY and inside_glass(x, y + 1):
                grid[y][x], grid[y + 1][x] = EMPTY, SAND
                moved = True
                continue

            for dx in (-1, 1):
                nx, ny = x + dx, y + 1
                if (
                    0 <= nx < WIDTH
                    and ny < HEIGHT
                    and grid[ny][nx] == EMPTY
                    and inside_glass(nx, ny)
                ):
                    grid[y][x], grid[ny][nx] = EMPTY, SAND
                    moved = True
                    break

    return moved

def render(grid):
    return "\n".join("".join(row) for row in grid)
