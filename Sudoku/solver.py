practice_board = [
    [0, 0, 0, 5, 9, 0, 0, 1, 0],
    [2, 1, 6, 0, 0, 7, 0, 3, 0],
    [7, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 8, 6, 0, 0, 0, 2, 1],
    [0, 0, 4, 2, 3, 9, 8, 0, 0],
    [9, 6, 0, 0, 0, 8, 7, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 4],
    [0, 8, 0, 4, 0, 0, 1, 7, 6],
    [0, 2, 0, 0, 6, 1, 0, 0, 0]
]


def print_board(board):
    """
    Purpose
    ----------
    This function is used to print board throughout solver

    Parameters
    ----------
    board: array (9x9)
    """

    for ii in range(len(board)):
        if ii % 3 == 0 and ii != 0:
            print('- - - - - - - - - - - - -')

        for jj in range (len(board[0])):
            if jj % 3 == 0 and jj != 0:
                print(' | ', end = "")

            if jj == 8:
                print(board[ii][jj])
            else:
                print(str(board[ii][jj]) + " ", end = "")


def find_empty(board):
    """
    Purpose
    ----------
    To find the empty cells indicated by a zero in the inputted board
    Parameters
    ----------
    board

    Returns
    -------
    Position of empty cell indicated by a zero
    """
    for ii in range(len(board)):
        for jj in range(len(board[ii])):
            if board[ii][jj] == 0:
                print('Empty: ', (jj , ii))  # column, row
                return jj, ii                # column, row
    return None


def validation(board, number, position):
    """

    Parameters
    ----------
    board: array of arrays
    number: int. number we are trying in board
    position:

    Returns
    -------

    """

    # Check row
    for ii in range(len(board[0])):
        # pos[0] is the position we just inserted into so we don't need to check that one
        if board[position[1]][ii] == number and position[0] != ii:
            print("Incorrect guess")
            return False

    # Check column
    for jj in range(len(board)):
        # jj and position switched places because it reads column row not row column
        if board[jj][position[0]] == number and position[1] != jj:
            print("Incorrect guess")
            return False

    # Check square
    # Gives what box we are in
    box_x = position[0] // 3
    box_y = position[1] // 3
    for aa in range(box_y * 3, box_y * 3 + 3):
        for bb in range(box_x * 3, box_x * 3 + 3):
            if board[aa][bb] == number and position[0] != aa and position[1] != bb:
                print("Incorrect guess")
                return False

    return True


def main_solver(board):
    print_board(board)
    find = find_empty(board)

    # If the board is solved
    if not find:
        return True
    # Else start solving for the place found
    else:
        col, row = find

    # Plug number into a place and see if it works
    for ii in range(1,10):
        if validation(board, ii, (col, row)): # validation returns true
            board[row][col] = ii # set the position equal to the number

            if main_solver(board): # recursive to move to the next number
                return True
                print_board(board) # prints board at the end

            # If validation returns false the number is reset
            board[row][col] = 0
    return False
