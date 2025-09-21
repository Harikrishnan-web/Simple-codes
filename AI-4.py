def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i] == j:
            return False
    return True

def solve_n_queens_util(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row] = -1
    return False

def solve_n_queens(n):
    board = [-1] * n
    if solve_n_queens_util(board, 0, n):
        solution = [(i + 1, board[i] + 1) for i in range(n)]
        return solution
    else:
        return None

if __name__ == "__main__":
    n = int(input("Enter the value of N (number of queens): "))
    result = solve_n_queens(n)
    if result:
        print(f"\nOne solution to the {n}-Queens problem:")
        for pos in result:
            print(f"Queen at row {pos[0]}, column {pos[1]}")
    else:
        print(f"\nNo solution exists for N = {n}")
