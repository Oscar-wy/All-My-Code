import time
import os
import pygame
Game = True
ctr = 0
Board = ["X"]

def printBoard(Board):
    os.system("clear")
    string = ""
    for i in range(len(Board)):
        string += Board[i] 
    print(string)

while Game != False:
    time.sleep(.2)
    ctr += 1
    if ctr >= 1:
        Board.insert(0, " ")
    printBoard(Board)

