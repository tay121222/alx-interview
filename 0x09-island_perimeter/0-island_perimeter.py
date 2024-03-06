#!/usr/bin/python3
"""function island_perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    m, n = len(grid), len(grid[0])
    land, edge = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land += 1
                if i < m - 1 and grid[i+1][j] == 1:
                    edge += 1
                if j < n - 1 and grid[i][j+1] == 1:
                    edge += 1
    return (land * 4) - (2 * edge)
