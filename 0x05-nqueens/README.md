
## 0x05-nqueens
<<<<<<< HEAD
![queen](https://github.com/Pauloslemma/alx-interview/assets/122981444/84a03a9a-1969-4440-957b-e7684453dad3)
=======
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
    # Base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then remove queen from board[i][col]
            board[i][col] = 0

    # If queen can not be placed in any row in this column col, then return false
    return False

def solve_n_queens(N):
    # Initialize board
    board = [[0] * N for _ in range(N)]

    # Call the helper function to solve N queens problem
    if not solve_n_queens_util(board, 0, N):
        print("No solution exists")
        return

    # Print all solutions
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solve_n_queens(N)
>>>>>>> 388bab0 (updated)

