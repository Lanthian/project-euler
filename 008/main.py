""" Largest Product in a Series

The four adjacent digits in the 1000--digit number that have the greatest 
  product are 9x9x8x9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the 
  greatest product. What is the value of this product?
https://projecteuler.net/problem=8
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "number.txt"
DIGITS = 13


# First seen in 005 - Smallest Multiple
def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base


# --- Calculation ---
def main():
    # Read in data
    fp = easy_open(__file__, FILE, "r")
    NUMBER = fp.readline()
    fp.close()

    # Split number up into int sub-sequences of length >= DIGITS. Drop seqs w/ 0.
    subseqs = [[int(c) for c in s] for s in NUMBER.split("0") if len(s) >= DIGITS]

    max_prod = 0
    # For each subsequence, multiply terms all sequential slices of length DIGIT
    for s in subseqs:
        # Initial multiplication of first DIGIT-1 terms
        product = operate_list(1, s[0:DIGITS-1], mul)

        # Step forward along slice: multiply in new term, check, divide out old term
        for i in range(DIGITS-1, len(s)):
            product *= s[i]
            # Update max discovered if new max
            if product > max_prod: max_prod = product
            product //= s[i-DIGITS+1]


    # --- Output ---
    print(max_prod) # 23,514,624,000
