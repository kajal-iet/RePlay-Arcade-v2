EMPTY = "."
PLAYER_X = "X"
PLAYER_O = "O"
W, H = 7, 6

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [[EMPTY for _ in range(W)] for _ in range(H)]
        self.player = PLAYER_X
        self.winner = None

GAME = Game()

def drop(col):
    for r in range(H-1, -1, -1):
        if GAME.board[r][col] == EMPTY:
            GAME.board[r][col] = GAME.player
            return r
    return None

def check_winner(t):
    b = GAME.board
    for r in range(H):
        for c in range(W-3):
            if all(b[r][c+i]==t for i in range(4)): return True
    for r in range(H-3):
        for c in range(W):
            if all(b[r+i][c]==t for i in range(4)): return True
    for r in range(H-3):
        for c in range(W-3):
            if all(b[r+i][c+i]==t for i in range(4)): return True
            if all(b[r+3-i][c+i]==t for i in range(4)): return True
    return False
