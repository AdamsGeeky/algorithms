#!/usr/bin/python3
"""
Extracted from Cracking the Coding Interview 6th edition chapter 8
Imagine a robot sitting on the upper left corner of grid with r rows
and c columns. The robot can only move in two directions, right and down,
but certain cells are "off limits" such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""


def naive_recursive(x, y, grid):
    """
    make a tree of all the calls
    Start from the end, then check if moving up 1 row works, if it does
    recurse on that, otherwise try moving left 1 column.
    If nothing works return None

    Arguments:
        x: the endpoint row value
        y: the endpoint column value
        grid: the grid

    Return:
        a path, or None
    """
    if x == 0 and y == 0:
        return [[0, 0]]
    if x >= 1 and grid[x - 1][y] != 'X':
        nr = naive_recursive(x - 1, y, grid)
        if nr != None:
            return  nr + [[x, y]]
    if y >= 1 and grid[x] [y - 1] != 'X':
        nr = naive_recursive(x, y - 1, grid)
        if nr != None:
            return nr + [[x, y]]
    return None


def dyn_r(x, y, grid, already_checked=[]):
    """
    Store the positions already checked so as to not go
    through the same position twice

    Arguments:
        x: endpoint row value
        y: endpoint column value
        grid: the grid
        already_checked, a list of coordinates already tested

    Return:
       a path or None
    """
    if x == 0 and y == 0:
        return [[0, 0]]
    if [x, y] in already_checked:
        return None
    if x >= 1 and grid[x - 1][y] != 'X':
        nr = dyn_r(x - 1, y, grid, already_checked)
        already_checked.append([x - 1, y])
        if nr != None:
            return  nr + [[x, y]]
    if y >= 1 and grid[x] [y - 1] != 'X':
        nr = dyn_r(x, y - 1, grid, already_checked)
        already_checked.append([x, y - 1])
        if nr != None:
            return nr + [[x, y]]
    return None


if __name__ == "__main__":
    grid = [['0', '0', '0', 'X'],
            ['0', '0', '0', '0'],
            ['0', '0', 'X', '0'],
            ['0', '0', 'X', '0']]
    print(naive_recursive(3, 3, grid))
    print(dyn_r(3, 3, grid, []))

    grid = [['0', 'X', '0', 'X'],
            ['0', 'X', '0', '0'],
            ['0', 'X', '0', '0'],
            ['0', '0', 'X', '0']]
    print(naive_recursive(3, 3, grid))
    print(dyn_r(3, 3, grid, []))

    grid = [['0', 'X', '0', 'X', '0', '0', 'X'],
            ['0', '0', '0', '0', 'X', '0', '0'],
            ['0', 'X', '0', '0', '0', '0', '0'],
            ['0', 'X', '0', '0', '0', 'X', '0'],
            ['0', 'X', '0', '0', '0', 'X', '0'],
            ['0', '0', 'X', '0', 'X', 'X', '0']]
    print(naive_recursive(6, 6, grid))
    print(dyn_r(6, 6, grid, []))
