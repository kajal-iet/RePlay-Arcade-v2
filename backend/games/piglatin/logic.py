import random
import re

VOWELS = ("a","e","i","o","u")

SENTENCES = [
    "Pig Latin is fun", "Hello world!", "This game is awesome",
    "Python makes coding enjoyable", "Streamlit is very powerful",
    "Can you translate this sentence?", "Programming is not magic",
    "String manipulation is tricky", "Watch out for punctuation!",
    "HELLO THERE", "I love Python!", "Do robots eat food?",
    "Artificial Intelligence is fascinating", "Quick brown fox jumps",
    "Why is Pig Latin funny?", "Multiple players make it fun",
    "Try not to cheat!", "Practice makes progress", "Never stop learning"
]

class PigLatinGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.scores = [0,0]
        self.turn = 0
        self.new_round()

    def new_round(self):
        self.question = random.choice(SENTENCES)
        self.answer = english_to_pig_latin(self.question)
        self.submitted = False
        self.correct = None

GAME = PigLatinGame()

def english_to_pig_latin(sentence):
    output = []

    for word in sentence.split():
        prefix = re.match(r"^\W*", word).group()
        suffix = re.search(r"\W*$", word).group()
        core = word[len(prefix):len(word)-len(suffix)]

        if not core.isalpha():
            output.append(word)
            continue

        was_upper = core.isupper()
        was_title = core.istitle()

        core = core.lower()
        match = re.match(r"[^aeiou]+", core)

        if match:
            cons = match.group()
            pig = core[len(cons):] + cons + "ay"
        else:
            pig = core + "yay"

        if was_upper: pig = pig.upper()
        elif was_title: pig = pig.capitalize()

        output.append(prefix + pig + suffix)

    return " ".join(output)
