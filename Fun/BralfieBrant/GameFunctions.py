import random
import json

class Player():
    def __init__(self):
        self.Money = 0
        self.Investments = {}
        self.Day = 0
        self.LocalSave = 0
        self.amountInvestedToday = 0
        self.Repaired = False
        self.repairCost = 50000
        self.Username = ""
        self.Messages = [f'It\'s day {self.Day} lets get started.', f'Rise and shine it\'s day {self.Day} time to start investing.', f'GooPlayer.Day it\'s day {self.Day}. Get the flippity dippity flop up and start investing YOU LAZY BASTARD!', 'Good morning sunshine, invest don\'t rest and get to it', f'Day {self.Day} wow look how far we\'ve come, tired of investing yet? I DONT CARE DO YOU WANT YOUR LAPTOP FIXED OR NOT!','Get up! Your snooze button isn\'t going to press itself.',f'WAKE UP! Its day {self.Day}, your pillow is begging for a break seriously.', f'Morning, it\'s day {self.Day}! Your bed might miss you but the world won\'t. I promise.']
    def Invest(self, selection, amount):
        currentStockPrice = selection.stockValue
        totalPrice = currentStockPrice * amount
        if totalPrice < self.Money:
            investmentList = [selection, amount]
            print(selection.Name)
            print(self.Investments)
            try:
                if not self.Investments[selection.Name]:
                    self.Investments[selection.Name] = investmentList
            except:
                self.Investments[selection.Name][1] += amount
            print(self.Investments)
            self.Money = self.Money - totalPrice
            print("Invested!")
            print("You Now Own", amount, "Stocks Of", selection.Name)
        else:
            print("Not Enough Money!")
    def repairLaptop(self):
        choice = input(f"The Repair Costs {self.repairCost} Are You Sure (y/n)? ").lower()
        if choice == "y":
            if self.Money >= self.repairCost and self.repairCost != 0:
                self.Money - self.repairCost
                self.repairCost = 0
                print("Congrats You Finally Fixed Your Shitty Laptop")
            elif self.repairCost == 0:
                print("You Have Already Repaired The Laptop")
            else:
                print("You Do Not Have Enough Money To Repair The Laptop.")
        else:
            print("\nShouldnt Have Bothered Me")
    def printMessage(self):
        message = random.randint(0, len(self.Messages)-1)
        print(self.Messages[message])
    def createLocal(self):
        text = ""
        try:
            with open(f"./UserSaves/UserSave{self.Username}", "r+") as file:
                text = file.readline()
                file.close()
        except:
            open(f"./UserSaves/UserSave{self.Username}", "x")
        if text != "":
            self.loadData()
    def saveData(self):
        Data = f"{self.Username}\n{str(self.Money)}\n{str(self.Investments)}\n{str(self.Day)}"
        with open("./UserSaves/UserSave"+self.Username, "w+") as file:
            file.write(Data)
            file.close()
    def loadData(self):
        player = ("./UserSaves/UserSave"+self.Username)
        try:
            with open(player, "r+") as playerdata:
                print('Save Found! Welcome back :D')
                data = []
                data = playerdata.readlines()
                self.Money = float(data[1])
                print(json.loads(data[2]))
                self.Day = int(data[3])
        except:
            self.createLocal()
            print('No player data found.')
            print('Creating new save.')
    
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