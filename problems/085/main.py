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
import time
from common.nums import triangle

# --- Conditions of the problem ---
GOAL = 2*10**6
STOPPING_MARGIN = 25    # After this many increases in X, stop if no improvement


def rectangles(x: int, y: int) -> int:
    """Counts and returns the number of possible rectangles inside a grid of 
    size `x` by `y`."""
    return triangle(x) * triangle(y) 


# --- Calculation ---
def main():
    start = time.time()

    best_dif = GOAL
    best_val = (0,0)
    for x in range(1, GOAL):
        # Lazy stopping condition if no improvement after STOPPING_MARGIN tests
        if x - STOPPING_MARGIN > best_val[0]: break
        
        # # Accurate stopping condition
        # if triangle(x) > GOAL: break

        for y in range(x, 0, -1):
            r = rectangles(x,y)
            dif = abs(GOAL-r)
            # Break early to reduce processing time
            if dif > best_dif and r < GOAL: break

            # Update known best as necessary
            if dif < best_dif:
                best_dif = dif
                best_val =  (x,y)


    # --- Output ---
    print("Time:", time.time() - start)
    x,y = best_val
    print(x*y) # 2772
    return
