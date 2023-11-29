#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """returns perimeter of island in grid"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0
    if rows > 100:
        return
    if cols > 100:
        return

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell adds 4 to perimeter
                # Check neighboring cells and deduct for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 for each adjacent land cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 for each adjacent land cell

    return perimeter
