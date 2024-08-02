""" Maximum Path Sum II

By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23. 
    3
    7 4
    2 4 6
    8 5 9 3
That is, 3+7+4+9=23
Find the maximum total from top to bottom in <triangle.txt>, a 15K text file 
  containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It is not possible to 
  try every route to solve this problem, as there are 2^99 altogether! If you 
  could check one trillion (1012) routes every second it would take over twenty 
  billion years to check them all. There is an efficient algorithm to solve it. 
  ;o)
https://projecteuler.net/problem=67
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import add
from common.files import easy_open
from common.valwrap import ValWrap

# --- Conditions of the problem ---
FILE = "triangle.txt"
DELIM = " "


# --- Calculation ---
def main():
    # Read in data
    fp = easy_open(__file__, FILE, "r")
    triangle = [[int(n) for n in s.split(DELIM)] for s in fp.readlines()]
    fp.close()

    # Build a tree of greatest (largest) path to each cell from triangle top
    tree = {(0,0): ValWrap(triangle[0][0], [0])}

    # Working down the rows, across the columns
    for r,row in enumerate(triangle[1:], 1):
        for c,cell in enumerate(row):
            
            # Find best parent path to current cell
            left = (r-1,c-1)
            right = (r-1,c)
            # If only left or right exists - has to be parent
            if left not in tree: parent = tree[right]
            elif right not in tree: parent = tree[left]

            else:
                # Otherwise compare possible parent values
                if tree[left].val >= tree[right].val: parent = tree[left]
                else: parent = tree[right]
            
            # Update this cell's best path
            tree[(r,c)] = ValWrap(parent.val + cell, parent.item + [c])

    # Find max path
    last_row = len(triangle) - 1
    max_path_value = max([wrap.val for (r,_),wrap in tree.items() if r == last_row])
    

    # --- Output ---
    print(max_path_value) # 7,273
    return
