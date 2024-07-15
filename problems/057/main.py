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
from fractions import Fraction

# --- Conditions of the problem ---
LIMIT = 1000


def sqrt_2_generator():
    num = 1 + 1/2
    while(True):
        yield num
        num = 1 + 1/(1+num)


# --- Calculation ---
def main():
    tally = 0
    for i,v in enumerate(sqrt_2_generator()):
        if i == LIMIT: break
        # Convert decimal into a fraction, and compare numer' and denom' length
        f = Fraction(v).limit_denominator()
        # print(i, f)
        if len(str(f.numerator)) > len(str(f.denominator)): tally += 1
 

    # --- Output ---
    print(tally)
    return
