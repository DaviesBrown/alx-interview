#!/usr/bin/python3
"""
n queens algo
"""
import sys


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


if __name__ == "__main__":
    solve_queens(0, n, solution)
