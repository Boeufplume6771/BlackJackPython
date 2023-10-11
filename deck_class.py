Suits = ["Pique", "Coeur", "Trèfle", "Carreau"]
from card_class import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()
    
    def build(self):
        for s in Suits:
            for v in range(1,14):
                self.cards.append(Card(v, s))
        random.shuffle(self.cards)

    def Pick(self):
        return self.cards.pop(0)

