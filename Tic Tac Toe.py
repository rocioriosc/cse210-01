"""
Assignment: Tic-Tac-Toe
Author: Hilda Rocio Rios


"""

from doctest import ELLIPSIS_MARKER



def show_board(board):
    for raw in board:
        for i in range(len(raw)):
            if i == len(raw) - 1:
                print(raw[i], end="\n")
            else:
                print(raw[i], end=" ")

def change_board(board, position, player):
    if player:
        symbol ="x"
    else:
        symbol ="O"
    if position == 7:
        if board[4][0] == ' ':
            board[4][0] = symbol
            return 0
        else:
            return 'This place 1is not available.'
    elif position == 8:
        if board[4][2] == ' ':
            board[4][2] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 9:
        if board[4][4] == ' ':
            board[4][4] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 4:
        if board[2][0] == ' ':
            board[2][0] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 5:
        if board[2][2] == ' ':
            board[2][2] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 6:
        if board[2][4] == ' ':
            board[2][4] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 1:
        if board[0][0] == ' ':
            board[0][0] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 2:
        if board[0][2] == ' ':
            board[0][2] = symbol
            return 0
        else:
            return 'This place is not available.'
    elif position == 3:
        if board[0][4] == ' ':
            board[0][4] = symbol
            return 0
        else:
            return 'This place is not available.'
    else:
        return 'This place doesn´t exist'



def winner(board):
    for symbol in ["x", "o"]:
        row_0 = board[0][0] == symbol and board[0][2] == symbol and board[0][4] == symbol
        row_2 = board[2][0] == symbol and board[2][2] == symbol and board[2][4] == symbol
        row_4 = board[4][0] == symbol and board[4][2] == symbol and board[4][4] == symbol
        column_0 = board[0][0] == symbol and board[2][0] == symbol and board[4][0] == symbol
        column_2 = board[0][2] == symbol and board[2][2] == symbol and board[4][2] == symbol
        column_4 = board[0][4] == symbol and board[2][4] == symbol and board[4][4] == symbol
        diagonally_up = board[0][0] == symbol and board[2][2] == symbol and board[4][4] == symbol
        diagonally_down = board[4][0] == symbol and board[2][2] == symbol and board[0][4] == symbol

        if row_0 or row_2 or row_4 or column_0 or column_2 or column_4 or diagonally_down or diagonally_up:
            if symbol == 'x':
                return 1
            elif symbol == 'o':
                return 2
            break

board = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]

turn_1= True
player_A= " PLAYER_x"
player_B= "PLAYER_o "
turn = 0

show_board(board)

while turn < 9:
    if turn_1:
         print(f"{player_A}'s turn to choose a square (1-9): " )
    else:
        print(f"{player_B}'s turn to choose a square (1-9): " )
    play = int(input())

    give_value= change_board(board,play,turn_1)
    if give_value ==0:
        turn_1 = not turn_1
        turn += 1
        show_board(board)
        if winner(board) ==1:
            print("PLAYER_x won. Good game. Thanks for playing!")
            break
        elif winner(board) ==2:
            print("PLAYER_o won. Good game. Thanks for playing!")
            break
    else:
        print(give_value)
    if turn ==9:
        print("Tie")

