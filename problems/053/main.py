""" Combinatoric Selections

There are exactly ten ways of selecting three from five, 12345:
    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, nCr(5,3) = 10.
In general, nCr(n,r) = n!/(r!*(n-r)!), where r <= n, n! = n*(n-1)*...*3*2*1, and
  0! = 1.
It is not until n = 23, that a value exceeds one-million: nCr(23,10) = 1144066.
How many, not necessarily distinct, values of nCr(n,r) for 1 <= n <= 100, are 
  greater than one-million?
https://projecteuler.net/problem=53
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial

# --- Conditions of the problem ---
N = 100                 # Inclusive
THRESHOLD = 10**6


def combinations(n: int, r: int, facs: dict[int, int]) -> int:
    """Returns the nCr (n choose r) of `n` and `r` using precalculated 
    factorials in `facs`. facs must be filled out appropriately."""
    return facs[n] // (facs[r] * facs[n-r])


# --- Calculation ---
def main():
    # Precalculate factorials to reduce double ups
    facs = {i: factorial(i) for i in range(0,N+1)}

    total = 0
    for n in range(1,N+1):
        for r in range(n//2+1):

            if combinations(n,r,facs) > THRESHOLD:
                # Count remaining r's that will work with n to pass threshold
                total += 2*(n//2 - r) + 2
                # Only 1 combination for n = 2r
                if n%2 == 0: total -= 1
                break


    # --- Output ---
    print(total) # 4,075
    return
