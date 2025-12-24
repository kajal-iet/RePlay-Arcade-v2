import datetime
import random

def getBirthdays(num):
    start = datetime.date(2001, 1, 1)
    return [start + datetime.timedelta(random.randint(0, 364)) for _ in range(num)]

def getMatch(birthdays):
    seen = set()
    for b in birthdays:
        if b in seen:
            return b
        seen.add(b)
    return None

def calculate_probabilities(a, b):
    sizes = list(range(a, b))
    values = []

    for size in sizes:
        match_count = 0
        for _ in range(1000):
            if getMatch(getBirthdays(size)):
                match_count += 1
        values.append(match_count / 1000)

    return sizes, values
