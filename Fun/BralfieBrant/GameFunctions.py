import random

class Player():
    def __init__(self):
        self.Money = 0
        self.Investments = {}
        self.Day = 0
        self.LocalSave = 0
    
class Investment:
    def __init__(self, name):
        self.Name = name
        self.stockPercent = 0
        self.stockRate = 0
        self.stockValue = 1
    def changeStock(self):
        self.stockPercent = random.randint(-10,10)
        self.stockRate = self.stockRate * (self.stockPercent + 1)
        if self.stockValue >= 1:
            self.stockValue = round(self.stockValue * (1 + (self.stockPercent/100)), 2)

McDonalds = Investment("McDonalds")
BurgerKing = Investment("Burger King")
WiggetGroup = Investment("Wigget Group")
Investments = [McDonalds, BurgerKing, WiggetGroup]