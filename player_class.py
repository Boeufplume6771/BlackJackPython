class Player:
    def __init__(self, name, isDealer) -> None:
        self.Hand = []
        self.name = name
        self.points = 0
        self.isDealer = isDealer
        self.stand = False

    def Hit(self, deck):
        PickedCard = deck.Pick()
        self.Hand.append(PickedCard)
        
        if not self.isDealer:
            if PickedCard.type == 1:
                if self.points >= 11:
                    self.points += 1
                else:
                    self.points += 11
            else:
                self.points += PickedCard.value
        else:
            self.points += PickedCard.value
        
        if self.isDealer:
            if self.points > 17:
                self.stand = True
        else:
            if self.points > 21:
                self.stand = True
        print(f"{self.name} picked: {PickedCard.title} de {PickedCard.suit}")

    def Stand(self):
        self.stand = True
        print(f"{self.name} standed")