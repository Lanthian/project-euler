""" Maximum Path Sum I

By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23. 
    3
    7 4
    2 4 6
    8 5 9 3
That is, 3+7+4+9=23
Find the maximum total from top to bottom of the triangle below:
    <triangle.txt>
NOTE: As there are only 16384 routes, it is possible to solve this problem by 
  trying every route. However, Problem 67, is the same challenge with a triangle 
  containing one-hundred rows; it cannot be solved by brute force, and requires 
  a clever method! ;o)
https://projecteuler.net/problem=18
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import add
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "triangle.txt"
DELIM = " "


def sub_triangle(triangle: list[list], index: int) -> list[list]:
    """Takes a triangle `triangle` (list of lists of items, each row larger than
    the prior) and returns a subtriangle with root at `index` of second row."""
    return [row[index:i+index+1] for i,row in enumerate(triangle[1:])]

def max_tri_recurse(triangle: list[list], op, base: ...) -> ...:
    """Via brute force (testing each path) and maximimising at each tree node,
    finds the maximum possible value of a binary operation `op` enacted across a
    triangular list of lists, `triangle`. Returns this value."""
    rows = len(triangle)
    # Check if triangle == [] initially...
    if rows == 0: return base
    # or if at the bottom of triangle
    if rows == 1: return max(triangle[0])

    # Otherwise, recurse and operate
    sub_maxes = []
    for i in range(len(triangle[1])):
        # Generate sub triangle and find it's maximum
        sub_tri = sub_triangle(triangle, i)
        sub_maxes.append(max_tri_recurse(sub_tri, op, base))

    return op(max(sub_maxes), triangle[0][0])


# --- Calculation ---
def main():
    # Read in data
    fp = easy_open(__file__, FILE, "r")
    triangle = [[int(n) for n in s.split(DELIM)] for s in fp.readlines()]
    fp.close()


    # --- Output ---
    print(max_tri_recurse(triangle, add, 0)) # 1,074
    return
