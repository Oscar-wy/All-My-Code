import random

def setUpBoard():
  Board = []
  for Row in range(10):
    BoardRow = []
    for Column in range(10):
      BoardRow.append("-")
    Board.append(BoardRow)
  return Board

def printBoard(board):
    print()
    print("The board looks like this: ")  
    print()
    print (" ", end="")
    for Column in range(10):
        print("  " + str(Column) + " ", end="")
    print()
    for Row in range(10):
        print (str(Row) + "| ", end="")
        for Column in range(10):
            if board[Row][Column] == "-":
                print(" ", end="")          
            else:
                print(board[Row][Column], end="")
            if Column != 10:
                print(" | ", end="")
        print()

def checkNum(coords):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    List = []
    ctr = 0
    for i in range(len(coords)):
        if ctr == 2:
            break
        for j in range(len(nums)):
            if coords[i] == nums[j]:
                ctr += 1
                List.append(coords[i])
    return List

def allowedMove(user, coords):
    if user.Coordinates == coords:
        return False
    

class Entity:
    def __init__(self, name, health):
        self.Name = name
        self.Health = health
        self.Speed = 1
        self.Coordinates = ["0", "0"]
        self.initializeCoords()
    def initializeCoords(self):
        coord1 = random.randint(0, 8)
        coord2 = random.randint(0, 8)
        self.Coordinates = [coord1, coord2]

class Player(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    def Move(self):
        Direction = input("Choose Where To Go (Collumn Row): ")
        Coordinates = checkNum(Direction)
        print(Coordinates)
        if not allowedMove(self, Coordinates):
            print("Cant Move There")
            self.Move()

class Game:
    def __init__(self, player, aoe):
        self.Player = player
        self.amountEnemies = aoe
        self.Enemies = []
    def makeEnemies(self):
        for i in range(self.amountEnemies):
            pass
    def Move():
        pass


User = Player("Player", 100)
Aoe = input("How Many Enemies Do You Want To Face: ")
Server = Game(User, Aoe)
Server.Player

Board = setUpBoard()
printBoard(Board)

