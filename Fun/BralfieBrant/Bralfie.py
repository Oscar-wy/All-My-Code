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
        Choice = input("What Do You Want To Do Today? ").lower()
        if Choice == "invest":
            Invest()
        elif Choice == "repair" or Choice == "fix":
            Player.repairLaptop()
        else:
            print("Not A Part Of The Game?")