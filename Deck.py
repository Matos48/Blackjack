from Card import Card
import Global
import random

class Deck(Card):

    def __init__(self):
        self.all_cards = []
        for f in Global.figura:
            for k in Global.kolor:
                card = Card(k, f)
                self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def take_one(self):
        return self.all_cards.pop(0)