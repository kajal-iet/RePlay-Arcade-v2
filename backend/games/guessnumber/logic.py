import random

class Game:
    def __init__(self):
        self.reset("Easy")

    def reset(self, level):
        self.level = level
        self.history = []
        self.over = False
        self.attempts = 0

        if level == "Easy":
            self.max_num, self.max_attempts = 50, 10
        elif level == "Medium":
            self.max_num, self.max_attempts = 100, 10
        else:
            self.max_num, self.max_attempts = 500, 12

        self.secret = random.randint(1, self.max_num)

GAME = Game()

def guess(n):
    if GAME.over: return None

    GAME.attempts += 1

    if n == GAME.secret:
        GAME.history.append((n, "Correct"))
        GAME.over = True
    elif n < GAME.secret:
        GAME.history.append((n, "Low"))
    else:
        GAME.history.append((n, "High"))

    if GAME.attempts >= GAME.max_attempts and not GAME.over:
        GAME.over = True

    return True
