""" Largest Product in a Grid

In the 20 x 20 grid below, four numbers along a diagonal line have been marked 
  in red.
    <grid.txt>
The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up,
  down, left, right, or diagonally) in the 20 x 20 grid?
https://projecteuler.net/problem=11
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul

# --- Conditions of the problem ---
fp = open("grid.txt","r")
GRID = [[int(s) for s in l.strip().split(" ")] for l in fp.readlines()]
GRID_ROWS = len(GRID)
GRID_COLS = len(GRID[0])
SELECT = 4


# First seen in 005 - Smallest Multiple
def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base
    

# --- Calculation ---
max_prod = 0

# Check selection patterns for greatest product
for r in range(GRID_ROWS):
    for c in range(GRID_COLS):
        # Column
        if (r + SELECT-1) < GRID_ROWS: 
            selection = [GRID[y][c] for y in range(r, r+SELECT)]
            max_prod = max(max_prod, operate_list(1, selection, mul))
        
        # Row
        if (c + SELECT-1) < GRID_COLS: 
            selection = [GRID[r][x] for x in range(c, c+SELECT)]
            max_prod = max(max_prod, operate_list(1, selection, mul))

        # Diagonal decreasing
        if (r + (SELECT-1) < GRID_ROWS) and (c + (SELECT-1) < GRID_COLS):
            selection = [GRID[r+i][c+i] for i in range(SELECT)]
            max_prod = max(max_prod, operate_list(1, selection, mul))

        # Diagonal increasing
        if (r - (SELECT-1) >= 0) and (c + (SELECT-1) < GRID_COLS):
            selection = [GRID[r-i][c+i] for i in range(SELECT)]
            max_prod = max(max_prod, operate_list(1, selection, mul))


# --- Output ---
print(max_prod) # 70,600,674
