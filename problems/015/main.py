""" Lattice Paths

Starting in the top left corner of a 2x2 grid, and only being able to move to 
  the right and down, there are exactly 6 routes to the bottom right corner.
    <image>
How many such routes are there through a 20x20 grid?
https://projecteuler.net/problem=15
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial as fac
from operator import mul
from common.iters import operate_list

# --- Conditions of the problem ---
DOMAIN = [20,20]


# --- Testing/Research ---
# start = [0] * len(DOMAIN)
#
# def lattice_step(current: list[int], end: list[int]) -> int:
#     if current == end: return 1
#
#     count = 0
#     for i in range(len(current)):
#         # If at axis end, no further possible steps
#         if current[i] == end[i]: continue
#
#         count += lattice_step(current[:i]+[current[i]+1]+current[i+1:], end)
#     return count
#
# print(lattice_step(start, DOMAIN))
# # IMPROVEMENT NEEDED: Working through paths is not feasible with large domains 


# """
# num: 1x1, 2x2, 3x3, 4x4, 5x5, 6x6
# out:   2,   6,  20,  70, 252, 924
# Central Binomial Coefficients!
# """
# SQUARE = 20
#
# def central_binom_coef(num: int) -> int:
#     """Returns the central binomial coefficient of number `num`."""
#     return fac(2*num) // (fac(num) ** 2)
#
# print(central_binom_coef(SQUARE)) # 137,846,528,820
# # IMPROVEMENT NEEDED: Doesn't work with domains with more or less than 2 axes


"""
Derived from investigation into binomial coefficients:
    <binomial coefficient.png>
"""

def path(axes: list[int]) -> int:
    """Finds the number of paths through a rectangular prism of any number of 
    axes, with lengths of axes defined in `axes` list. Returns this count."""
    return fac(sum(axes))//operate_list(1, [fac(i) for i in axes], mul)


# --- Calculation & Output ---
def main():
    print(path(DOMAIN)) # 137,846,528,820
