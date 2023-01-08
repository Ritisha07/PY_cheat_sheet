from Deck import Deck

deck = Deck()


class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards 

    def __str__(self) -> str:
        return "Contains {} cards".format(len(self.cards))

    def add(self, new_cards):
        self.cards.extend(new_cards)

    def remove(self):
        return self.cards.pop()
