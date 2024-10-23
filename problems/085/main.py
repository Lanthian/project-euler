""" Counting Rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2
  contains eighteen rectangles:
    <graphic>
Although there exists no rectangular grid that contains exactly two million 
  rectangles, find the area of the grid with the nearest solution.
https://projecteuler.net/problem=85
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen

# --- Conditions of the problem ---
GOAL = 2*10**6


def rectangles(x: int, y: int) -> int:
    """Counts and returns the number of possible rectangles inside a grid of 
    size `x` by `y`."""
    count = 0
    for i in range(x):
        for j in range(y):
            count += (x-i) * (y-j)
    return count
            

# --- Calculation ---
def main():
    best_dif = GOAL
    best_val = None
    for x in range(1, GOAL):
        for y in range(1, x+1):
            r = rectangles(x,y)
            dif = abs(GOAL-r)
            if dif < best_dif:
                best_dif = dif
                best_val =  (x,y)
                print((x,y), ":", r) # 2772


    # --- Output ---
    x,y = best_val
    print(x*y)
    return
