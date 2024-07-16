""" Spiral Primes

Starting with 1 and spiralling anticlockwise in the following way, a square 
  spiral with side length 7 is formed.
    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49 
It is interesting to note that the odd squares lie along the bottom right 
  diagonal, but what is more interesting is that 8 out of the 13 numbers lying
  along both diagonals are prime; that is, a ratio of 8/13 ~= 62%.
If one complete new layer is wrapped around the spiral above, a square spiral 
  with side length 9 will be formed. If this process is continued, what is the 
  side length of the square spiral for which the ratio of primes along both 
  diagonals first falls below 10%?
https://projecteuler.net/problem=58
"""

__author__ = "Liam Anthian"

# --- Import ---
from common.primes import is_prime2

# --- Conditions of the problem ---
LIMIT = 0.1             # Exclusive


# --- Calculation ---
def main():
    num = 1
    i = 1       # current depth of spiral from centre
    
    primes = 0
    corners = 1
    
    # Spiral through numbers until ratio breaks limit, storing the diagonals
    while (True):
        # Check each corner of current spiral depth
        for _ in range(4):
            num += 2*i

            if is_prime2(num): primes += 1
            corners += 1

        # Check ratio
        if primes / corners < LIMIT: break
        i+=1


    # --- Output ---
    print(2*i+1) # 26,241
    return
