import time
import os

def CreateBoard ():
    board = []
    for i in range(5):
        row = CreateRow()
        board.append(row)
    return(board)

def CreateRow():
    row = []
    for i in range(5):
        row.append(0)
    
    return(row)

def PrintBoard(Board):
    for i in range(len(Board)):
        print(Board[i])


def SartGame():
    Board = CreateBoard()
    print(PrintBoard(Board))



SartGame()