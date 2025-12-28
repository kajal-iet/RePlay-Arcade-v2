import random

def process_roll(diceStr):
    clean = diceStr.lower().replace(" ", "")

    if clean == "quit":
        return {"quit": True}

    dIndex = clean.find("d")
    if dIndex == -1:
        raise Exception('Missing "d"')

    numDice = int(clean[:dIndex])

    modIndex = clean.find("+")
    if modIndex == -1:
        modIndex = clean.find("-")

    if modIndex == -1:
        numSides = int(clean[dIndex + 1:])
        modAmount = 0
    else:
        numSides = int(clean[dIndex + 1:modIndex])
        modAmount = int(clean[modIndex + 1:])
        if clean[modIndex] == "-":
            modAmount = -modAmount

    rolls = [random.randint(1, numSides) for _ in range(numDice)]
    total = sum(rolls) + modAmount

    return {
        "input": diceStr,
        "rolls": rolls,
        "total": total,
        "modifier": modAmount
    }
