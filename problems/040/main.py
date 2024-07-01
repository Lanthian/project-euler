""" Champernowne's Constant

An irrational decimal fraction is created by concatenating the positive 
  integers:
    0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the 
  following expression.
    d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
https://projecteuler.net/problem=40
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen

# --- Conditions of the problem ---
SELECTION = [1, 10, 100, 1000, 10000, 100000, 1000000]


def champernowne(n: int) -> str:
    """Generates the decimal places of champernowne's constant up to place `n`.
    Returns decimal places as a string."""
    out = ""
    for i in int_gen(1):
        if len(out) >= n: return out[:n]
        else: out += str(i)


# --- Calculation ---
def main():
    prod = 1
    for i,v in enumerate(champernowne(SELECTION[-1]),1):
        if i in SELECTION: prod *= int(v)


    # --- Output ---
    print(prod) # 210
    return
