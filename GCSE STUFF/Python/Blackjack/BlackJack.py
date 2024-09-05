import random

class PersonObject:
    hasAce = False
    def __init__(self, *cards):
        self.cards = cards
    def GiveCards(self, *cards):
        self.cards.append(cards)

Player = PersonObject(random.randint(1,11), random.randint(1,11))
Computer = PersonObject(random.randint(1,11), random.randint(1,11))
