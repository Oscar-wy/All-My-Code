import GameFunctions as GF
Stop = False

Investments = GF.Investments
Player = GF.Player()

def Invest():
    for i in range(len(Investments)):
        print(f"{i+1} - {Investments[i].Name} £{Investments[i].stockValue} {Investments[i].stockPercent}%")
    selection = int(input("Choose Which To Invest In: "))
    print(f"{Player.Money}")
    amount = int(input("How Much: "))
    Player.Invest(Investments[selection-1], amount)

if __name__ == "__main__":
    if Player.Username == "":
        user = input("Enter Your Username: ")
        Player.Username = user
        Player.createLocal()
    while Stop != True:
        currentDay = Player.Day
        for i in Investments:
            i.changeStock()
        if currentDay == Player.Day:
            Player.printMessage()
        Choice = input("What Do You Want To Do Today? ").lower()
        if Choice == "invest":
            Invest()
        elif Choice == "repair" or Choice == "fix":
            Player.repairLaptop()
        else:
            print("Not A Part Of The Game?")
        Player.saveData()