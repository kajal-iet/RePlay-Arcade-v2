import random

WIDTH = 15
HEIGHT = 12
NUM_ROBOTS = 8
NUM_TELEPORTS = 2

EMPTY = " "
PLAYER = "🧍"
ROBOT = "🤖"
DEAD = "💥"
WALL = "⬛"

class Game:
    def __init__(self):
        self.reset()

    def empty_board(self):
        board = {}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                board[(x, y)] = EMPTY

        for x in range(WIDTH):
            board[(x, 0)] = WALL
            board[(x, HEIGHT - 1)] = WALL
        for y in range(HEIGHT):
            board[(0, y)] = WALL
            board[(WIDTH - 1, y)] = WALL
        return board

    def random_empty(self, occupied):
        while True:
            x = random.randint(1, WIDTH - 2)
            y = random.randint(1, HEIGHT - 2)
            if self.board[(x, y)] == EMPTY and (x, y) not in occupied:
                return (x, y)

    def move_robot(self, rx, ry):
        px, py = self.player
        dx = 1 if px > rx else -1 if px < rx else 0
        dy = 1 if py > ry else -1 if py < ry else 0
        return rx + dx, ry + dy

    def reset(self):
        self.board = self.empty_board()
        self.player = self.random_empty([])
        self.robots = [self.random_empty([self.player]) for _ in range(NUM_ROBOTS)]
        self.teleports = NUM_TELEPORTS
        self.score = 0
        self.over = False

    def step(self, move=None, teleport=False):
        if self.over:
            return

        px, py = self.player

        if teleport and self.teleports > 0:
            self.teleports -= 1
            self.player = self.random_empty(self.robots)

        elif move:
            nx, ny = px + move[0], py + move[1]
            if self.board[(nx, ny)] == EMPTY:
                self.player = (nx, ny)

        next_positions = {}
        survivors = []

        for rx, ry in self.robots:
            nx, ny = self.move_robot(rx, ry)

            if (nx, ny) == self.player:
                self.over = True
                return

            next_positions.setdefault((nx, ny), 0)
            next_positions[(nx, ny)] += 1

        for pos, count in next_positions.items():
            if count == 1:
                survivors.append(pos)
            else:
                self.score += count

        self.robots = survivors

        if not survivors:
            self.over = True

    def render(self):
        grid = ""
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = (x, y)
                if pos == self.player:
                    grid += PLAYER
                elif pos in self.robots:
                    grid += ROBOT
                else:
                    grid += self.board[pos]
            grid += "\n"
        return grid
    def render_board():
        grid = ""
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = (x, y)
                if pos == GAME.player:
                    grid += PLAYER
                elif pos in GAME.robots:
                    grid += ROBOT
                else:
                    grid += GAME.board[pos]
            grid += "\n"
        return grid


GAME = Game()
