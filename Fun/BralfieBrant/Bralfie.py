import GameFunctions as GF
Stop = False

Investments = GF.Investments
Player = GF.Player()

def Invest():
    pass

if __name__ == "__main__":
    while Stop != True:
        currentDay = Player.Day
        if currentDay == Player.Day:
            Player.printMessage()
        Choice = input("What Do You Want To Do Today? ")
        if Choice.lower() == "invest":
            Invest()
        else:
            print("Not A Part Of The Game?")