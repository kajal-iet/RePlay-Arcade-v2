import random

HEARTS = "♥"
DIAMONDS = "♦"
SPADES = "♠"
CLUBS = "♣"
BACKSIDE = "backside"

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def getHandValue(cards):
    value = 0
    aces = 0
    for rank, _ in cards:
        if rank == 'A': aces += 1
        elif rank in ('K','Q','J'): value += 10
        else: value += int(rank)
    value += aces
    for _ in range(aces):
        if value + 10 <= 21: value += 10
    return value

def dealerPlay(deck, hand):
    while getHandValue(hand) < 17:
        hand.append(deck.pop())
    return hand
