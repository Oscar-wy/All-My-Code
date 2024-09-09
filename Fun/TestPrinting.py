import time
import os

def CreateBoard ():
    board = []
    for i in range(10):
        row = CreateRow()
        board.append(row)
    return(board)

def CreateRow():
    row = []
    for i in range(20):
        row.append(" ")
    
    return(row)

def PrintBoard(Board):
    for i in range(len(Board)):
        print(Board[i])
    return('')


def StartGame():
    Board = CreateBoard()
    print(PrintBoard(Board))



StartGame()