import random
import os
import pygame

class pieceClass():
    def __init__(self):
        pieceSelect = random.randint(1, 7)
        self.piece = []
        self.Type = ""
        self.Orientation = ""
        self.Coordinates = []
        orientationSelect = random.randint(1, 4)
        if orientationSelect == 1:
            self.Orientation = "U"
        elif orientationSelect == 2:
            self.Orientation = "D"
        elif orientationSelect == 3:
            self.Orientation = "L"
        else:
            self.Orientation = "R"
        if pieceSelect == 1:
            self.piece = [["X","X"],["X","X"]]
            self.Type = "Square"
        elif pieceSelect == 2:
            self.piece = [["X"],["X"],["X"],["X"]]
            self.Type = "Line"
        elif pieceSelect == 3:
            self.piece = [[" ","X","X"], ["X","X"," "]]
            self.Type = "LStair"
        elif pieceSelect == 4:
            self.piece = [["X","X"," "], [" ","X","X"]]
            self.Type = "RStair"
        elif pieceSelect == 5:
            self.piece = [["X"," "], ["X"," "], ["X","X"]]
            self.Type = "LPiece"
        elif pieceSelect == 6:
            self.piece = [[" ","X"], [" ", "X"], ["X", "X"]]
            self.Type = "RPiece"
        elif pieceSelect == 7:
            self.piece = [[" ","X"," "], ["X", "X", "X"]]
            self.Type = "Middle"
    def createCoords(self, Board):
        colCoord = random.randint(1, len(Board[0])-1)
        size = len(self.piece[0])      
        for column in range(len(Board[0])):
            if column == colCoord:
                for shapeRow in range(len(self.piece)):
                    for shapeCol in range(size):
                        if self.Orientation == "D":
                            if self.piece[(len(self.piece)-1)-shapeRow][shapeCol] == " ":
                                print(shapeRow, column+(shapeCol-1), "Not It")
                            else:
                                self.Coordinates.append([shapeRow, column+(shapeCol-1)])
                        elif self.Orientation == "U":
                            if self.piece[shapeRow][shapeCol] == " ":
                                print(shapeRow, column+(shapeCol-1), "Not It")
                            else:
                                self.Coordinates.append([shapeRow, column+(shapeCol-1)])
                        elif self.Orientation == "L":
                            if self.piece[shapeRow][shapeCol] == " ":
                                print(shapeCol, column+(shapeRow-1), "Not It")
                            else:
                                self.Coordinates.append([shapeCol, column+(shapeRow-1)])
                        else:
                            if self.piece[shapeRow][shapeCol] == " ":
                                print(shapeRow, column-(shapeRow-1), "Not It")
                            else:
                                self.Coordinates.append([shapeRow, column+(shapeCol-1)])

class gameClass():
    def __init__(self, player):
        self.Board = []
        self.Points = 0
        self.Player = player
        self.Shapes = []
        self.currentShape = None
    def createBoard(self):
        self.Board = []
        for column in range(24):
            rowList = []
            for row in range(10):
                rowList.append("-")
            self.Board.append(rowList)
    def printBoard(self):
        for row in range(len(self.Board)):
            rowList = "|"
            for column in range(len(self.Board[row])):
                done = False
                for shape in self.Shapes:
                    for coords in shape.Coordinates:
                        if coords[0] == row and coords[1] == column:
                            rowList += " X |"
                            done = True
                if not done:
                    rowList += "   |"
            print(rowList)
    def getShape(self):
        shape = pieceClass()
        self.currentShape = shape
        self.Shapes.append(shape)
        shape.createCoords(self.Board)
        print(shape.Coordinates)
        print(shape.Type)
        print(shape.piece)
        print(shape.Orientation)         
    def changeShapeBoard(self):
        hitFloor = False
        hitBlock = False
        pos = self.currentShape.Coordinates
        print(pos)
        user = input(">").lower()
        for i in pos:
            if user == "a":
                if i[1] != 0:
                    i[1] -= 1
            elif user == "d":
                if i[1] != 9:
                    i[1] += 1
            elif user == "w":
                if i[0] != 0:
                    i[0] -= 1
            elif user == "s":
                if i[0] != 23 and not hitFloor:
                    i[0] += 1
            else:
                print("Error")
        for i in pos:
            if i[0] == 23:
                hitFloor = True
        for shape in self.Shapes:
            for shCoords in shape.Coordinates:
                for coords in pos:
                    for col in range(-1, 1):
                        if (shCoords[1] == (coords[1]+col) and shCoords[0] == coords[0]+col) and shape != self.currentShape:
                            hitBlock = True
        if hitBlock:
            print("Hit")
            for coords in self.currentShape.Coordinates:
                if coords[0] == 0:
                    return "End"
                else:
                    return True
        if hitFloor:
            print("Floor")
            return True
        elif hitBlock:
            print("Block")
            return True
        else:
            self.currentShape.Coordinates = pos
        return False
    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def checkBoard(self):
        pass
    def Play(self):
        done = False
        pieceComplete = True
        while not done:
            #self.Clear()
            if pieceComplete:
                pieceComplete = False
                self.getShape()
            print(self.Shapes)
            self.printBoard()
            check = self.changeShapeBoard()
            if check == "End":
                break
            elif check == True:
                pieceComplete = True
            self.printBoard()
            #pieceComplete = self.input()
            self.checkBoard()
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
