
def is_safe(board, row, col):
    for i in range(1, row):
        if board[i] == col:                    # same column
            return False
        if abs(board[i] - col) == abs(i - row):  # same diagonal
            return False
    return True


def nqueen(board, row, n, solutions):
    if row > n:
        solutions[0] += 1
        print_board(board, n, solutions[0])
        return

    for col in range(1, n + 1):
        if is_safe(board, row, col):
            board[row] = col
            nqueen(board, row + 1, n, solutions)
            board[row] = 0                      # backtrack


def print_board(board, n, count):
    print(f"\nSolution {count}: {board[1:]}")
    for r in range(1, n + 1):
        print(" ".join("Q" if board[r] == c else "." for c in range(1, n + 1)))


if __name__ == "__main__":
    n = int(input("Enter number of queens (N): "))
    board = [0] * (n + 1)          # 1-indexed, board[row] = column
    solutions = [0]
    nqueen(board, 1, n, solutions)
    if solutions[0] == 0:
        print("No solution exists.")
    else:
        print(f"\nTotal solutions: {solutions[0]}")
