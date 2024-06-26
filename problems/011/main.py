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
from common.files import easy_open
from common.iters import operate_list

# --- Conditions of the problem ---
FILE = "grid.txt"
SELECT = 4
    

# --- Calculation ---
def main():
    # Read in data
    fp = easy_open(__file__, FILE, "r")
    grid = [[int(s) for s in l.strip().split(" ")] for l in fp.readlines()]
    fp.close()
    
    n_rows = len(grid)
    n_cols = len(grid[0])

    max_prod = 0

    # Check selection patterns for greatest product
    for r in range(n_rows):
        for c in range(n_cols):
            # Column
            if (r + SELECT-1) < n_rows: 
                selection = [grid[y][c] for y in range(r, r+SELECT)]
                max_prod = max(max_prod, operate_list(1, selection, mul))
            
            # Row
            if (c + SELECT-1) < n_cols: 
                selection = [grid[r][x] for x in range(c, c+SELECT)]
                max_prod = max(max_prod, operate_list(1, selection, mul))

            # Diagonal decreasing
            if (r + (SELECT-1) < n_rows) and (c + (SELECT-1) < n_cols):
                selection = [grid[r+i][c+i] for i in range(SELECT)]
                max_prod = max(max_prod, operate_list(1, selection, mul))

            # Diagonal increasing
            if (r - (SELECT-1) >= 0) and (c + (SELECT-1) < n_cols):
                selection = [grid[r-i][c+i] for i in range(SELECT)]
                max_prod = max(max_prod, operate_list(1, selection, mul))


    # --- Output ---
    print(max_prod) # 70,600,674
