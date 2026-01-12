import random

def generate_secret_number(num_digits):
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:num_digits])

def get_clues(guess, secret):
    if guess == secret:
        return "WIN", True

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")

    if not clues:
        return "Bagels", False

    return " ".join(clues), False

