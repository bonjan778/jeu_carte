import random
from .carte import RANKS, SUITS, Card


class Deck(list):
    def __init__(self):
        for rank in RANKS:
            for suit in SUITS:
                carte = Card(suit, rank)
                self.append(carte)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self)

    def draw_card(self):
        try:
            return self.pop()
        except IndexError:
            return None
