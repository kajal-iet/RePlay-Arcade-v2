import random

CATEGORIES = {
    "Animals": "ANT BABOON BADGER BAT BEAR CAMEL CAT DOG DONKEY DUCK EAGLE FOX FROG GOAT LION MONKEY OTTER PIGEON RABBIT TIGER WOLF ZEBRA".split(),
    "Fruits": "APPLE BANANA CHERRY GRAPE MANGO ORANGE PAPAYA PEACH PEAR PINEAPPLE".split(),
    "Countries": "INDIA CANADA FRANCE GERMANY ITALY JAPAN NEPAL NORWAY SPAIN SWEDEN".split()
}

HANGMAN_PICS = [ "...", "...", "...", "...", "...", "...", "..." ]
GUILLOTINE_PICS = [ "...", "...", "...", "...", "...", "...", "..." ]


class Game:
    def __init__(self):
        self.reset(random.choice(list(CATEGORIES.keys())))

    def reset(self, category):
        self.category = category
        self.secret = random.choice(CATEGORIES[category])
        self.missed = []
        self.correct = []
        self.style = "Hangman"
        self.game_over = False
        self.message = ""

game = Game()
