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
from common.nums import triangle

# --- Conditions of the problem ---
GOAL = 2*10**6
STOPPING_MARGIN = 25    # After this many increases in X, stop in no improvement


def rectangles(x: int, y: int) -> int:
    """Counts and returns the number of possible rectangles inside a grid of 
    size `x` by `y`."""
    return triangle(x) * triangle(y) 


# --- Calculation ---
def main():
    best_dif = GOAL
    best_val = (0,0)
    for x in range(1, GOAL):
        # Lazy stopping condition if no improvement after STOPPING_MARGIN tests
        if x - STOPPING_MARGIN > best_val[0]: break

        for y in range(1, x+1):
            dif = abs(GOAL-rectangles(x,y))
            if dif < best_dif:
                best_dif = dif
                best_val =  (x,y)


    # --- Output ---
    x,y = best_val
    print(x*y) # 2772
    return
