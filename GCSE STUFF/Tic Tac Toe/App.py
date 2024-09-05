import TicTacToe
import os

board = [" " for x in range(9)]

def PrintBoard():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print(row1+"\n"+row2+"\n"+row3)
    
def PlayerMove(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = icon
        return True
    else:
        return False

def IsVictory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or (board[3] == icon and board[4] == icon and board[5] == icon) or (board[6] == icon and board[7] == icon and board[8] == icon) or (board[0] == icon and board[3] == icon and board[6] == icon) or (board[1] == icon and board[4] == icon and board[7] == icon) or (board[2] == icon and board[5] == icon and board[8] == icon) or (board[0] == icon and board[4] == icon and board[8] == icon) or (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def IsDraw():
    if " " not in board:
        return True
    else:
        return False
    
def Clear():
    os.system('cls' if os.name=='nt' else 'clear')

Stop = False

def Tictactoe():
    while Stop == False:
        PrintBoard()
        if not PlayerMove("X"):
            Clear()
            PrintBoard()
            print("That Space Is Taken!")
        else:
            Clear()
            PrintBoard()
        if IsVictory("X"):
            print("X Wins!")
        elif IsDraw():
            print("Its A Draw")
        if not PlayerMove("X"):
            Clear()
            PrintBoard()
            print("That Space Is Taken!")
        else:
            Clear()
        if IsVictory("O"):
            print("O Wins!")
        elif IsDraw():
            print("Its A Draw")


if __name__ == "__main__":
    Tictactoe()
