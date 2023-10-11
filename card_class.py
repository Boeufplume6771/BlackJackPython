Titles = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
Values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
# Types:1=A,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=J,12=Q,13=K

class Card:
    def __init__(self, type, suit) -> None:
        self.type = type
        self.suit = suit
        self.title = Titles[self.type - 2]
        self.value = Values[self.type - 2]
    
    def show(self):
        print(f"{self.title} de {self.suit}")