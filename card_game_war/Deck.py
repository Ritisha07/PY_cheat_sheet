from random import shuffle


class Deck:
    SUITE = "H D S C".split()
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self) -> None:
        self.card_list = [(s, r) for s in self.SUITE for r in self.RANKS]

    def sufflt(self):
        shuffle(self.card_list)

    def split_in_half(self):
        return (self.card_list[:26], self.card_list[26:])
