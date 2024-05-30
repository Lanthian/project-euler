""" Lattice Paths

Starting in the top left corner of a 2x2 grid, and only being able to move to 
  the right and down, there are exactly 6 routes to the bottom right corner.
    <image>
How many such routes are there through a 20x20 grid?
https://projecteuler.net/problem=15
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial

# --- Conditions of the problem ---
# DOMAIN = [4,2]
SQUARE = 20


# --- Calculation ---
# start = [0] * len(DOMAIN)

# def lattice_step(current: list[int], end: list[int]) -> int:
#     if current == end: return 1

#     count = 0
#     for i in range(len(current)):
#         # If at axis end, no further possible steps
#         if current[i] == end[i]: continue

#         count += lattice_step(current[:i]+[current[i]+1]+current[i+1:], end)
#     return count

# print(lattice_step(start, DOMAIN))
# - Stepping through all paths is not feasible with larger domains -


# --- Research ---
"""
num: 1, 2,  3,  4,   5,   6
out: 2, 6, 20, 70, 252, 924
Central Binomial Coefficients!
"""

def central_binom_coef(num: int) -> int:
    """Returns the central binomial coefficient of number `num`."""
    return factorial(2*num) // (factorial(num) ** 2)


# --- Output ---
print(central_binom_coef(SQUARE)) # 137,846,528,820
