""" Permuted Multiples

It can be seen that the number, 125874, and its double 251748, contain exactly 
  the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
  the same digits.
https://projecteuler.net/problem=52
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import permutation
from common.nums import int_gen

# --- Conditions of the problem ---
MULTIPLES = [2,3,4,5,6]


# --- Calculation ---
def main():
    # Iterate through integers
    for i in int_gen(1):
        i_s = str(i)
        # Reverse multiples to make search faster (checking permutations)
        for m in reversed(MULTIPLES):
            if not permutation(i_s, str(m*i)): break
        # Answer found
        else: break


    # --- Output ---
    print(i) # 142,857
    return
