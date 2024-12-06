#!/usr/bin/python3
"""
Solves the island perimeter problem
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    :param grid: List of lists of integers representing the grid.
                 0 represents water, 1 represents land.
    :return: Integer representing the perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Start with 4 sides
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
