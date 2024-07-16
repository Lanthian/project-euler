""" Square Root Convergents

It is possible to show that the square root of two can be expressed as an 
  infinite continued fraction.
    <expression>
By expanding this for the first four iterations, we get:
    1 + 1/2 = 3/2 = 1.5
    1 + 1/(2+1/2) = 7/5 = 1.4
    1 + 1/(2+1/(2+1/2)) = 17/12 = 1.41666...
    1 + 1/(2+1/(2+1/(2+1/2))) = 41/29 = 1.41379...
The next expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
  1393/985, is the first example where the number of digits in the numerator 
  exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator 
  with more digits than the denominator?
https://projecteuler.net/problem=57
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.fraction import Fraction, fr_add, fr_flip

# --- Conditions of the problem ---
LIMIT = 1000


# --- Calculation ---
def main():
    # Reused fraction form of one
    one = Fraction(1,1)
    # Base case
    f = fr_add(one, Fraction(1,2))

    tally = 0
    for _ in range(LIMIT):
        if len(str(f.numer)) > len(str(f.denom)): tally += 1
        f = fr_add(one,fr_flip(fr_add(one,f,simplify=False)),simplify=False)


    # --- Output ---
    print(tally) # 153
    return
