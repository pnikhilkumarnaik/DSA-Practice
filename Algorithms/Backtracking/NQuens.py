n = 4
res = []

board = [[0] * n for _ in range(n)]


def is_safe(row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def backtrack(row):

    # All queens placed
    if row == n:
        res.append([r.copy() for r in board])
        return

    # Try every column in this row
    for col in range(n):

        if is_safe(row, col):

            # CHOOSE
            board[row][col] = 1

            # EXPLORE
            backtrack(row + 1)

            # UNDO
            board[row][col] = 0


backtrack(0)



print(res)

"""
OUTPUT: [[[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]], [[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]]

"""