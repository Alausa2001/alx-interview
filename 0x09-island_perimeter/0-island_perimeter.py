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

    index = []

    hor = []
    ver = [0] * len(grid[0])
    for i in range(len(grid)):
        idx = []
        hor_c = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ver[j] += 1
            if j < len(grid[i]) - 1:
                if grid[i][j] == 1 and grid[i][j+1] == 1:
                    hor_c += 1
                elif grid[i][j] == 0:
                    idx.append(j)
                else:
                    if hor_c != 0:
                        hor.append(hor_c+1)
                    hor_c = 0
        index.append(idx)
        if hor_c != 0:
            hor.append(hor_c+1)
            idx.append(j)
    if index.index((min(index, key=len))) <= max(ver):
        return 2 * (max(hor) + max(ver))
