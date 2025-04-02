import random
import json

class Investment:
    def __init__(self, name):
        self.Name = name
        self.stockpercent = 0
        self.stockrate = 0
        self.stockValue = 1
    def changeStock(self):
        self.stockpercent = random.randint(-10,10)
        self.stockrate = self.stockrate * (self.stockpercent + 1)
        if self.stockValue >= 1:
            self.stockValue = round(self.stockValue * (1 + (self.stockpercent/100)), 2)

class User:
    def __init__(self):
        self.Money = 1000
        self.Investments = {}
        self.Day = 0
        self.LocalSave = ""
        self.Username = ""
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

Player = User()

McDonalds = Investment("McDonalds")
BurgerKing = Investment("Burger King")
WiggetGroup = Investment("Wigget Group")
Investments = [McDonalds, BurgerKing, WiggetGroup]

def CreateLocal():
    num = random.randint(0, 999999)
    text = ""
    try:
        with open("./UserSaves/UserSave"+Player.Username, "r+") as file:
            text = file.readline()
            file.close()
    except:
        open("./UserSaves/UserSave"+Player.Username, "x")
    if text == "":
        Player.LocalSave = "UserSave" + str(num)
    else:
        Player.LocalSave = text
        print(Player.LocalSave)

def SaveData():
    Data = Player.LocalSave + "\n" + str(Player.Money) + "\n" + (Player.Investments) + "\n" + str(Player.Day)
    with open("./UserSaves/UserSave"+Player.Username, "w+") as file:
        file.write(Data)
        file.close()

def LoadData():
    player = ("./UserSaves/UserSave"+Player.Username)
    try:
        with open(player, "r+") as playerdata:
            print('Save Found! Welcome back :D')
            data = []
            data = playerdata.readlines()
            Player.Money = float(data[1])
            print(json.loads(data[2]))
            Player.Day = int(data[3])
    except:
        CreateLocal()
        print('No player data found.')
        print('Creating new save.')


def stockinvest():
    for i in range(len(Investments)):
        print(i + 1, "-", Investments[i].Name, "£"+str(Investments[i].stockValue), str(Investments[i].stockpercent) + '%')
    investment = int(input('where do you want to invest: '))
    investment = Investments[investment-1]
    print('Balance -', Player.Money)
    amount = float(input('How much: '))
    Player.Invest(investment, amount)

def startday():
    Game = True
    while Game != False:
        for i in range(len(Investments)):
            Investments[i].changeStock()
        Player.Day += 1
        messages = [f'It\'s day {Player.Day} lets get started.', f'Rise and shine it\'s day {Player.Day} time to start investing.', f'GooPlayer.Day it\'s day {Player.Day}. Get the flippity dippity flop up and start investing YOU LAZY BASTARD!', 'Good morning sunshine, invest don\'t rest and get to it', f'Day {Player.Day} wow look how far we\'ve come, tired of investing yet? I DONT CARE DO YOU WANT YOUR LAPTOP FIXED OR NOT!','Get up! Your snooze button isn\'t going to press itself.',f'WAKE UP! Its day {Player.Day}, your pillow is begging for a break seriously.', f'Morning, it\'s day {Player.Day}! Your bed might miss you but the world won\'t. I promise.']
        choice = random.randint(0, len(messages) - 1)
        print(messages[choice])
        print("What Do You Want To Do?")
        userChoice = input(">")
        if userChoice == "exit":
            Game = False
        else:
            stockinvest()
    SaveData()

def startgame():
    print()
    print('Welcome to Bralfie Brant Simulator the hit investment game!')
    print('your goal is to make as much money as possible from your savings')
    print('so you can afford to pay to fix your super sick RGB gaming laptop')
    print('after it broke T-T. Good luck :D')
    print()
    Username = input("Enter A Username: ")
    Player.Username = Username
    LoadData()
    startday()

startgame()

