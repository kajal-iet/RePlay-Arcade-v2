import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    result = "CHO" if total % 2 == 0 else "HAN"
    return d1, d2, total, result
