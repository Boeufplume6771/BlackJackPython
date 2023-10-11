from player_class import Player
from deck_class import Deck
from card_class import Card

Cartes = Deck()

PlayerOne = Player("Player", False)
Dealer = Player("Dealer", True)

#Gives to the player and the dealer starter cards
for _ in range(1,3):
    PlayerOne.Hit(Cartes)
    Dealer.Hit(Cartes)

while True:
    if PlayerOne.stand and Dealer.stand:
        break
    if PlayerOne.stand != True:
        print(f"You have {PlayerOne.points} points and the dealer have {Dealer.points}")
        Choice = input("Do you want to (H)it or (S)tand?")
        if PlayerOne.stand != True:
            if Choice.lower() == "h":
                PlayerOne.Hit(Cartes)
            elif Choice.lower() == "s":
                PlayerOne.Stand()
    
    if Dealer.stand != True:
        Dealer.Hit(Cartes)


if PlayerOne.points == Dealer.points:
    print("Nobody won (Tie)")
elif PlayerOne.points > 21:
    print(f"The dealer won with {Dealer.points} points")
elif PlayerOne.points > Dealer.points:
    print(f"You won with {PlayerOne.points} points!")
else:
    print(f"Dealer won with {Dealer.points} points")