import random
import os

class pieceClass():
    def __init__(self):
        pieceSelect = random.randint(1, 7)
        self.piece = []
        if pieceSelect == 1:
            self.piece = [["X","X"],["X","X"]]
        elif pieceSelect == 2:
            self.piece = [["X"],["X"],["X"],["X"]]
        elif pieceSelect == 3:
            self.piece = [[" ","X","X"], ["X","X"," "]]
        elif pieceSelect == 4:
            self.piece = [["X","X"," "], [" ","X","X"]]
        elif pieceSelect == 5:
            self.piece = [["X"," "], ["X"," "], ["X","X"]]
        elif pieceSelect == 6:
            self.piece = [[" ","X"], [" ", "X"], [" ", "X"]]
        elif pieceSelect == 7:
            self.piece = [["X","X","X"], [" ", "X", " "]]

class gameClass():
    def __init__(self, player):
        self.Board = []
        self.Points = 0
        self.Player = player
        self.Shapes = []
    def createBoard(self):
        for column in range(24):
            rowList = []
            for row in range(10):
                rowList.append("-")
            self.Board.append(rowList)
    def printBoard(self):
        for row in self.Board:
            rowList = "|"
            for column in row:
                if column == "-":
                    rowList += "   |"
                else:
                    rowList += column+"   |"
            print(rowList)
    def getShape(self):
        print("Doing Shape")
        shape = pieceClass()
        self.Shapes.append(shape)
        pos = random.randint(0, len(self.Board)-1)
        size = len(shape.piece[0])
        for rows in shape.piece:
            print("Rowing Shape")
            for row in self.Board:
                for column in range(len(row)):
                    for i in range(size):
                        if column == pos-(i-1):
                            print("Successing")
                            row[column] == rows[i]
        #add piece to board
    def input(self):
        #get keyboard input
        return self.changeShapeBoard()
    def changeShapeBoard(self):
        #change position on board
        #check if position is at the bottom
        #if it is return True else False
        #check if piece hits another piece if it does stop and return True
        #if it hits another and its at the top return "End"
        #else continue
        return False
    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def Play(self):
        done = False
        ctr = 0
        pieceComplete = True
        while not done:
            self.Clear()
            if pieceComplete:
                self.getShape()
            self.printBoard()
            pieceComplete = self.input()
            done = True
            #CheckBoard to see if any lines complete
            #Add points if completed


class playerClass():
    def __init__(self):
        self.Username = ""
        self.bestScore = 0
        self.Wins = 0
        self.Password = ""
    def createUsersFile(self):
        file = open("./Users.txt", "x")
        file.close()
    def checkUserExists(self, Username):
        file = open("./Users.txt", "r")
        text = file.readlines()
        for line in text:
            line = line.split(":")
            if Username == line[0]:
                return True
            else:
                return False
    def getPlayer(self):
        check = True
        user = input("Enter Your Username: ")
        passw = input("Enter Your Password: ")
        done = False
        try:
            with open("./Users.txt", "r") as userFile:
                text = userFile.readlines()
                for line in text:
                    line = line.split(":")
                    if line[0] == user:
                        if line[1] == passw+"\n":
                            self.Username = line[0]
                            self.Password = line[1]
                            done = True
                userFile.close()
            if not done:
                print("No Account Exists")
                print("Creating Account")
                check = True
                while check:
                    user = input("Enter A Usename: ")
                    check = self.checkUserExists(user)
                self.Username = user
                self.Password = passw
                self.savePlayer()
                print("Saved")
            else:
                print("Got")
        except:
            print("No File Exists Or Error Occured")
            print("\nCreating File")
            self.createUsersFile()
            self.getPlayer()
    def savePlayer(self):
        try:
            with open("./Users.txt", "a+") as usersFile:
                usersFile.write(f"{self.Username}:{self.Password}\n")
                usersFile.close()
        except:
            print("No File Exists Or Error Occured")
            print("\nCreating File")
            self.createUsersFile()
            self.savePlayer()
        try:
            with open(f"./{self.Username}Data", "a") as userFile:
                userFile.write(f"{self.bestScore}:{self.Wins}")
                userFile.close()
        except:
            print("Error Occured")
            file = open(f"./{self.Username}Data", "x")
            file.close()
        with open(f"./{self.Username}Data", "a") as userFile:
            userFile.write(f"{self.bestScore}:{self.Wins}")
            userFile.close()

Player = playerClass()
Game = gameClass(Player)

if __name__ == "__main__":
    Player.getPlayer()
    Game.createBoard()
    Game.Play()
