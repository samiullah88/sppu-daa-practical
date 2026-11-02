BOARD_SIZE = 4

def display_chess(board):
    for row in board:
        print(*row)


def is_queen_place_valid(board, crnt_row, crnt_col):
    # Check left side
    for i in range(crnt_col):
        if board[crnt_row][i]:
            return False

    # Check upper-left diagonal
    i, j = crnt_row, crnt_col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = crnt_row, crnt_col
    while i < BOARD_SIZE and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_problem(board, crnt_col):
    if crnt_col >= BOARD_SIZE:
        return True

    for row in range(BOARD_SIZE):
        if is_queen_place_valid(board, row, crnt_col):
            board[row][crnt_col] = 1

            if solve_problem(board, crnt_col + 1):
                return True

            board[row][crnt_col] = 0  # Backtracking

    return False


def display_solution():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    if solve_problem(board, 0):
        print("4x4 N-Queens Matrix:")
        display_chess(board)
    else:
        print("Solution does not exist")


display_solution()