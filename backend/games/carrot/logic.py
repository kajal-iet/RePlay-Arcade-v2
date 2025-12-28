import random

def new_round():
    return {
        "carrot_in_red": random.choice([True, False]),
        "swapped": False
    }

def reveal(carrot_in_red: bool, swapped: bool):
    if swapped:
        carrot_in_red = not carrot_in_red

    return "red" if carrot_in_red else "gold"
