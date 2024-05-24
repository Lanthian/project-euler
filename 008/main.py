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

# --- Conditions of the problem ---
fp = open("number.txt","r")
NUMBER = fp.readline()
DIGITS = 13


# First seen in 005 - Smallest Multiple
def operate_list(base: ..., iterable, operator: 'function') -> ...:
    """Apply a binary function `operator` between item `base` and elements of 
    `iterable`."""
    for i in iterable: base = operator(base, i)
    return base


# --- Calculation ---
# Split number up into int sub=sequences of length >= DIGITS. Drop seqs w/ 0.
subseqs = [[int(c) for c in s] for s in NUMBER.split("0") if len(s) >= DIGITS]

max_prod = 0
for s in subseqs:
    for i in range(0, len(s)-DIGITS+1):
        product = operate_list(1, s[i:i+DIGITS], mul)
        # Update max discovered if new max
        if product > max_prod: max_prod = product


# --- Output ---
print(max_prod) # 23514624000
