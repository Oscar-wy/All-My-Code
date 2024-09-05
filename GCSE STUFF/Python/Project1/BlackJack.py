import random
user = []
computer = []
totaluser = 0
totalcomp = 0
UserHasAce = False
CompHasAce = False
Play = True
choice = ""

def Draw():
    for i in range(2):
        number = random.randint(1,11)
        if i == 1:
            user.append(number)
        else:
            computer.append(number)

def Results(totaluser, totalcomp):
    for i in range(len(user)):
        totaluser += user[i]
        totalcomp += computer[i]
    print("User:", totaluser, "\nComputer:", totalcomp)
    print("User Has Ace:", UserHasAce, "\nComputer Has Ace:", CompHasAce)

for i in range(2):
    number1 = random.randint(1,11)
    number2 = random.randint(1,11)
    if i == 1:
        if number1 == 11 or number2 == 11:
            UserHasAce = True
        user.append(number1)
        user.append(number2)
    else:
        if number1 == 11 or number2 == 11:
            CompHasAce = True
        computer.append(number1)
        computer.append(number2)

while Play == True:
    Results(totaluser, totalcomp)
    choice = input("Do You Want To Draw Again (Y/N): ")
    if choice == "" or choice == "Y":
        Draw()
        if totaluser > 21 and not UserHasAce:
            print("You Lost!")
            Play = False
        elif totaluser > 21 and UserHasAce:
            totaluser = totaluser - 11
            user.remove(11)
        elif totalcomp > 21 and CompHasAce:
            totalcomp = totalcomp - 11
            computer.remove(11)
        elif totalcomp > 21 and totaluser < 22:
            print("You Won!")
            Play = False
    elif choice == "N":
        Play = False
        if totaluser == 21 or totaluser > totalcomp:
            print("You Win")

Results(totaluser, totalcomp)