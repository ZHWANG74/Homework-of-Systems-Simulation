import pandas as pd

state = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def show_grid(state):
    """
    Show the game state using a pandas data frame.
    """
    print(pd.DataFrame(state))

def count_empty_cells(state):
    """
    Count the number of empty cells in a game state.
    """
    count = 0
    # loop over each row
    for i in range(3):
        # loop over each column
        for j in range(3):
            # if the cell value is blank (" ")
            if state[i][j] == " ":
                # increment the count
                count += 1
    return count

def is_valid(row, col):
    """
    Determine if the location (row,col) is valid for a move.
    """
    return state[row][col] == " "

def mark_x(state, row, col):
    """
    Attempt to make an x mark at location (row, col)
    """
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "x"

# define a function to mark an 'o' at a row and column
def mark_o(state, row, col):
    """
    Attempt to make an o mark at location (row, col)
    """
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "o"

def reset_game(state):
    """
    Reset the game state, returning every cell to a blank space.
    """
    # loop over each row
    for i in range(3):
        # loop over each column
        for j in range(3):
            # empty the state location at (i,j)
            state[i][j] = " "

def get_winner(state):
    """
    Check if there is a winner for this game.
    If there is a winner, return the corresponding letter ("x" or "o").
    Otherwise, return the special value None.
    """
    for i in range(3):
        q = 0
        p = 0
        for j in range(3):
            if state[i][j] == state[i][0]:
                p += 1
            if p == 3:
                return state[i][0]
            if state[j][i] == state[0][i]:
                q += 1
            if q == 3:
                return state[0][i]
        q = 0
        w = 0
        for j in range(2):
            if state[2][2] == state[j][j]:
                q += 1
            if state[j][2 - j] == state[2][0]:
                w += 1
            if q == 2:
                return state[2][2]
            if w == 2:
                return state[2][0]
    return None


def is_tie(state):
    if count_empty_cells(state) == 0 and get_winner(state) == None:
        return "the game is tie"

mark_x(state, 0,0)
show_grid(state)
mark_o(state, 1,1)
show_grid(state)
mark_o(state, 0,1)
show_grid(state)
mark_o(state,2,1)
show_grid(state)

print(get_winner(state))
