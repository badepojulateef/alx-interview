#!/usr/bin/python3
"""
Create a function def island_perimeter(grid): that returns
the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
    - grid (List[List[int]]): A list of lists representing the 2D grid,
    where 0 is water and 1 is land.

    Returns:
    - int: The perimeter of the island.
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # For each land cell, add 4 to the perimeter
                perimeter += 4

                # Check the left neighbor, if it's land,
                # subtract 2 from the perimeter
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check the up neighbor, if it's land,
                # subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
