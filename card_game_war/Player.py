from Hand import Hand 
class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}".format(self.name, drawn_card))
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.remove())
        return war_cards


