import random, copy

BOARD_WIDTH = 12
BOARD_HEIGHT = 10
MOVES_PER_GAME = 20

TILE_TYPES = (0,1,2,3,4,5)

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = self.new_board()
        self.moves = MOVES_PER_GAME
        self.history = []
        self.message = ""
        self.hint = None

    def new_board(self):
        b = {}
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                b[(x,y)] = random.choice(TILE_TYPES)
        for _ in range(BOARD_WIDTH * BOARD_HEIGHT):
            x = random.randint(0, BOARD_WIDTH-2)
            y = random.randint(0, BOARD_HEIGHT-1)
            b[(x+1,y)] = b[(x,y)]
        return b

GAME = Game()

def flood_fill(x,y,new):
    board = GAME.board
    old = board[(x,y)]
    if new == old: return False

    stack = [(x,y)]
    visited = set()

    while stack:
        cx,cy = stack.pop()
        if (cx,cy) in visited: continue
        visited.add((cx,cy))
        if board[(cx,cy)] != old: continue

        board[(cx,cy)] = new
        if cx>0: stack.append((cx-1,cy))
        if cy>0: stack.append((cx,cy-1))
        if cx<BOARD_WIDTH-1: stack.append((cx+1,cy))
        if cy<BOARD_HEIGHT-1: stack.append((cx,cy+1))

    return True

def has_won():
    t = GAME.board[(0,0)]
    return all(GAME.board[(x,y)] == t for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT))

def simulate_gain(tile):
    copy_board = copy.deepcopy(GAME.board)
    GAME.board = copy_board
    flood_fill(0,0,tile)
    t = GAME.board[(0,0)]
    score = sum(1 for x in range(BOARD_WIDTH) for y in range(BOARD_HEIGHT) if GAME.board[(x,y)] == t)
    GAME.board = copy_board
    return score
