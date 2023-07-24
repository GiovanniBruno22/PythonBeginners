import tkinter as tk
from tkinter import messagebox

# Function to check winner. 
# We go through rows first and what we use list comprehension
# board is the board and player can be x or o and all(cell == player for cell in row ) will check
# if all the cell in a given row are equal to x or o
# This is repeated for columns and finally the board[i][i] is the diagonal \ 
# and the board[i][2 - i] is the diagonal /
# We will check one player first, x or o, and exit this function by returning True (mean the player has won)
# if any of the checks bools from the all function are returned as true. Otherwise, we return false and by
# this we mean that the game is not over

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Here we are checking if the board is full. Initially each cell or square or element in the 3x3 array 
# has an single space " ". If they are all not " " meaning that there is no single square that is a " "
# then we will return true , ie. the board is full.

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# turn is a global variable because it is assigned and used outside of this function. If we didnt say
# global then it would only live inside this function. 
# First off we are checking that neither player has won and the board is not full. 
# Otherwise we couldn't make a move. Next we check if the cell is empty.
# As the player alternates with each turn we can find out which player it is by taking turn and finding 
# its after dividing by 2. This will give either 0 or 1, which is x or o. The cell is then assigned 
# the player number, 0 or 1, and the turn is incremented by 1. 
# Again we check the winner or if the board is full

def on_click(row, col):
    global turn
    if not check_winner(board, "X") and not check_winner(board, "O") and not is_board_full(board):
        if board[row][col] == " ":
            player = players[turn % 2]
            buttons[row][col].config(text=player)
            board[row][col] = player
            turn += 1

            if check_winner(board, player):
                messagebox.showinfo("Game Over", f"Player {player} wins!")
            elif is_board_full(board):
                messagebox.showinfo("Game Over", "It's a draw!")

# Reset game simple returns board to a 3x3 filled with " "s.
# turn is also reset to 0 meaning xs turn.
# Here turn and board are global variables. 
# The reason is that these variables are used outside this function.
# tk.NORMAL is a tkinter user interface thing. Basically each of the cells in the user interface 
# has a state that we want to set. When we hover over it will change colour or when we click on it 
# its state will change. 
def reset_game():
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
