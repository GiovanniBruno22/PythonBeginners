import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):

    """Checks if player has won
    
        Args: board (str list) , the board represented as a list of strings and player (str) either X or O
    
        Returns: (bool) , true if the the given player has won, false if not
    """
    # check rows
    for row in range(3):
        row_temp = []
        for col in range(3):
            row_temp.append(board[row][col])
        if all(cell == player for cell in row_temp):
            return True
    # check cols
    for col in range(3):
        col_temp = []
        for row in range(3):
            col_temp.append(board[row][col])
        if all(cell == player for cell in col_temp):
            return True    
    # check diagonal 1
    diag1 = []
    for ind in range(3):
        diag1.append(board[ind][ind])
    if all(cell == player for cell in diag1):
        return True
    # check diagonal 2
    diag2 = []
    for ind in range(3):
        diag2.append(board[ind][2 - ind])
    if all(cell == player for cell in diag2):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full.
    
        Args: board (str list) , the board represented as a list of strings
    
        Returns: (bool) , true if the board is full, false if not
    """
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def on_click(row, col):
    """Adds an X or O to the cell, checks if player has won or if board is full and increments global turn counter.
    
        Args: row and col (ints)
    """
    global turn
    if not check_winner(board, "X") and not check_winner(board, "O") and not is_board_full(board):
        if board[row][col] == " ":
            player = players[turn % 2]
            # Update the button on tkinter
            buttons[row][col].config(text=player)
            # Update the cell value on the board
            board[row][col] = player
            turn += 1

            # check for winners and print message in message box
            if check_winner(board, player):
                message = "Player " + player +" wins!"
                messagebox.showinfo("Game Over", message)
            elif is_board_full(board):
                messagebox.showinfo("Game Over", "It's a draw!")


def reset_game():
    """Resets global variables board and turn
    
    """
    global board, turn
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state=tk.NORMAL)

if __name__ == "__main__":
    # Make a window with tkinter and name it
    window = tk.Tk()
    window.title("Tic Tac Toe")

    # Define the 3 global variables. Note that players is not changed so it can be used inside 
    # functions without needing to use the keyword 'global'  
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    # Define a 3 x 3 list of buttons all Nones
    buttons = [[None for _ in range(3)] for _ in range(3)]

    # Now we go through this 3x3 list and replace the None with a tkinter button that has a width 
    # and a height and a font etc. The lambda function allows us to pass the current row and col 
    # values as arguments to the on_click function when a button is clicked. 
    # Finally we lay out these buttons in a grid
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(window, width=10, height=3, font=("Helvetica", 20),
                                      command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)
            
    # Now we include a reset button that calls the reset_game function
    reset_button = tk.Button(window, text="Reset", font=("Helvetica", 16), command=reset_game)
    reset_button.grid(row=3, columnspan=3)
    # Now we start the program
    window.mainloop()
