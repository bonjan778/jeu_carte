from Controllers.base import Controller
from Modules.deck import Deck
from Views.base import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


main()
