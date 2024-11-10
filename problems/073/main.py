""" Counting Fractions in a Range

Consider the fraction, n/d, where n and d are positive integers. If n < d and 
  HCF(n,d) = 1, it is called a reduced proper fraction.
If we list the set of reduced fractions for d <= 8 in ascending order of size, 
  we get:
    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
  fractions for d <= 12 000?
https://projecteuler.net/problem=73
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.fractions import *

# --- Conditions of the problem ---
DENOM_LIMIT = 12000


# --- Calculation ---
def main():
    start = time.time()

    bounds = [Fraction(1,3), Fraction(1,2)]
    seen = {*bounds}
    for d in range(4,DENOM_LIMIT+1):
        for n in range(d//3 + 1, d//2 + (2-1)):
            f = Fraction(n,d)
            # Skip if above boundary
            if f > bounds[1]: break
            
            # Simplify to HCF and drop duplicates
            f.simplify()
            if f in seen: continue

            # Otherwise, store and count
            seen.add(f)


    # --- Output ---
    print("Time:", time.time() - start)
    print(len(seen) - 2)
    return
