import random

class Player():
    def __init__(self):
        self.Money = 0
        self.Investments = {}
        self.Day = 0
        self.LocalSave = 0
        self.amountInvestedToday = 0
        self.Messages = [f'It\'s day {self.Day} lets get started.', f'Rise and shine it\'s day {self.Day} time to start investing.', f'GooPlayer.Day it\'s day {self.Day}. Get the flippity dippity flop up and start investing YOU LAZY BASTARD!', 'Good morning sunshine, invest don\'t rest and get to it', f'Day {self.Day} wow look how far we\'ve come, tired of investing yet? I DONT CARE DO YOU WANT YOUR LAPTOP FIXED OR NOT!','Get up! Your snooze button isn\'t going to press itself.',f'WAKE UP! Its day {self.Day}, your pillow is begging for a break seriously.', f'Morning, it\'s day {self.Day}! Your bed might miss you but the world won\'t. I promise.']
    def Invest(self, selection, amount):
        currentStockPrice = selection.stockValue
        totalPrice = currentStockPrice * amount
        if totalPrice < self.Money:
            investmentList = [selection, amount]
            self.Investments[selection.Name] = investmentList
            print(self.Investments)
            self.Money = self.Money - totalPrice
            print("Invested!")
            print("You Now Own", amount, "Stocks Of", selection.Name)
        else:
            print("Not Enough Money!")
    def printMessage(self):
        message = random.randint(0, len(self.Messages)-1)
        print(self.Messages[message])
    
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