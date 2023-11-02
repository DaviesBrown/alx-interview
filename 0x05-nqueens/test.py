import sys

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    def backtrack(col):
        if col == n:
            solutions.append(list(board))
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                backtrack(col + 1)

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print([row, solution.index(row)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)



#!/usr/bin/python3
'''
Module that solves the N Queens puzzle
'''
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    solution = []

    def solve_queens(row, n, solution):
        if (row == n):
            print(solution)
        else:
            for col in range(n):
                placement = [row, col]
                if valid_placement(solution, placement):
                    solution.append(placement)
                    solve_queens(row + 1, n, solution)
                    solution.remove(placement)

    def valid_placement(solution, placement):
        for queen in solution:
            if queen[1] == placement[1]:
                return False
            if (queen[0] + queen[1]) == (placement[0] + placement[1]):
                return False
            if (queen[0] - queen[1]) == (placement[0] - placement[1]):
                return False
        return True

    solve_queens(0, n, solution)