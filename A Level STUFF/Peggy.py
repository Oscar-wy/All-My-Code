placeholder = " "

def find(board,choice):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if choice == board[i][j]:
                return i, j

grid = [["a",placeholder,"c","d"],["e","f","g","h"],["i","j","k","l"],["m","n","o","p"]]

def CreateGrid():
    print("Max Size 6 x 4")
    collumns = int(input("Enter Collumns: "))
    rows = int(input("Enter Rows: "))
    if collumns > 6 or rows > 6:
        print("Too Big!")
        CreateGrid()
    else:
        grid = []

def Save():
    with open("Game.txt", "w") as file:
        file.write(str(grid))

def Load():
    with open("Game.txt", "r") as file:
        grid = list(file.readline())

def show(board):
    for i in range(len(board)):
        print(grid[i])

while True:
    show(grid)
    choice = input("Enter a letter: ").lower()
    if choice == "save":
        Save()
    elif choice == "load":
        Load()
    direction = input("Enter a direction (u,d,l,r): ")

    row, column = find(grid, choice)

    if direction == "r":
        if column + 2 < len(grid[0]):
            if grid[row][column + 2] == placeholder:
                grid[row][column] = placeholder
                grid[row][column + 1] = placeholder
                grid[row][column + 2] = choice

    elif direction == "l":
        if column - 2 >= 0:
            if grid[row][column - 2] == placeholder:
                grid[row][column] = placeholder
                grid[row][column - 1] = placeholder
                grid[row][column - 2] = choice

    elif direction == "u":
        if row - 2 >= 0:
            if grid[row - 2][column] == placeholder:
                grid[row][column] = placeholder
                grid[row - 1][column] = placeholder
                grid[row - 2][column] = choice

    elif direction == "d":
        if row + 2 < len(grid):
            if grid[row + 2][column] == placeholder:
                grid[row][column] = placeholder
                grid[row + 1][column] = placeholder
                grid[row + 2][column] = choice         
