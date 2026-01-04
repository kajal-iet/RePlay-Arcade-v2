import random

CATEGORIES = {
    "Animals": "ANT BABOON BADGER BAT BEAR CAMEL CAT DOG DONKEY DUCK EAGLE FOX FROG GOAT LION MONKEY OTTER PIGEON RABBIT TIGER WOLF ZEBRA".split(),
    "Fruits": "APPLE BANANA CHERRY GRAPE MANGO ORANGE PAPAYA PEACH PEAR PINEAPPLE".split(),
    "Countries": "INDIA CANADA FRANCE GERMANY ITALY JAPAN NEPAL NORWAY SPAIN SWEDEN".split()
}

HANGMAN_PICS = [
""" +--+
 |  |
    |
    |
    |
    |
=====""",
""" +--+
 |  |
 O  |
    |
    |
    |
=====""",
""" +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
""" +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
""" +--+
 |  |
 O  |
/|\\ |
    |
    |
=====""",
""" +--+
 |  |
 O  |
/|\\ |
/   |
    |
=====""",
""" +--+
 |  |
 O  |
/|\\ |
/ \\ |
    |
====="""
]

class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.reset()

    def reset(self, category=None):
        if not category:
            category = random.choice(list(CATEGORIES.keys()))
        self.category = category
        self.secret = random.choice(CATEGORIES[category])
        self.correct = []
        self.missed = []
        self.logs = []
        self.locked = False

GAME = Game()

def submit_guess(letter):
    if GAME.locked:
        return

    if letter in GAME.correct or letter in GAME.missed:
        return

    if letter in GAME.secret:
        GAME.correct.append(letter)
        if all(c in GAME.correct for c in GAME.secret):
            GAME.logs.append(f"🎉 YOU WON — Word was {GAME.secret}")
            GAME.wins += 1
            GAME.locked = True
    else:
        GAME.missed.append(letter)
        if len(GAME.missed) >= len(HANGMAN_PICS) - 1:
            GAME.logs.append(f"💀 GAME OVER — Word was {GAME.secret}")
            GAME.losses += 1
            GAME.locked = True
