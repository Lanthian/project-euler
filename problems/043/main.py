""" Sub-string Divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
  each of the digits 0 to 9 in some order, but it also has a rather interesting 
  sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note 
  the following:
    * d2d3d4 = 406 is divisible by 2
    * d3d4d5 = 063 is divisible by 3
    * d4d5d6 = 635 is divisible by 5
    * d5d6d7 = 357 is divisible by 7
    * d6d7d8 = 572 is divisible by 11
    * d7d8d9 = 728 is divisible by 13
    * d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
https://projecteuler.net/problem=43
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import permutation_generator
from common.nums import pandigital
from common.primes import factor

# --- Conditions of the problem ---
def property(seq: str, valid: bool=True) -> bool:
    """Checks if a 0-9 pandigital number `seq` obeys the property rules laid out
    in projecteuler problem 43. Returns true if so, false if not."""
    # Quick pandigital check if not guaranteed valid
    if not valid:
        if not pandigital(seq, 9, True, 0): return False

    # Divisibility rules to check
    factors = [2,3,5,7,11,13,17]
    for i in range(0,len(factors)):
        # If any rules fail, break out early
        if not factor(int(seq[1+i:4+i]), factors[i]): return False
    else: return True


# --- Calculation ---
def main():
    total = 0
    for p in permutation_generator("0123456789"):
        if property(p): total += int(p)


    # --- Output ---
    print(total) # 16,695,334,890
    return
