#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid

    grid is a list of list of integers:

        0 represents water
        1 represents land

        Each cell is square, with a side length of 1

        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100

    The grid is completely surrounded by water

    There is only one island (or nothing).

    The island doesn’t have “lakes”
    (water inside that isn’t connected to the water surrounding the island).
    """

    perimeter = 0

    for row in range(len(grid)):
        for j in range(len(grid[row])):
            if grid[row][j] == 1:
                perimeter += 4

                if row > 0 and grid[row-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[row][j - 1] == 1:
                    perimeter -= 2
    return perimeter
