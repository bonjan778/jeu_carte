from typing import List
from .carte import RANKS, SUITS, Card

class Hand(List):
    def append(self, object):
        if not isinstance(object, Card):
            return ValueError("Vous ne pouvez ajouter que des cartes!")
        return super().append(object)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
