import sys

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, N):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(N):
    if not isinstance(N, int):
        print("N must be a number.", file=sys.stderr)
        sys.exit(1)
    if N < 4:
        print("N must be an integer greater or equal to 4.", file=sys.stderr)
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("No solution exists.", file=sys.stderr)
        sys.exit(1)

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number.", file=sys.stderr)
        sys.exit(1)
    solve_n_queens(N)

