def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nqueens(board, col+1, n):
                return True

            board[i][col] = 0

    return False


n = 4
board = [[0]*n for _ in range(n)]

solve_nqueens(board, 0, n)

for row in board:
    print(row)
