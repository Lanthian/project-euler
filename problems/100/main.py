""" Arranged Probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and 
  six red discs, and two discs were taken at random, it can be seen that the 
  probability of taking two blue discs, P(BB) = (15/21) x (14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two 
  blue discs at random, is a box containing eighty-five blue discs and 
  thirty-five red discs.
By finding the first arrangement to contain over 10^12 = 1 000 000 000 000 discs 
  in total, determine the number of blue discs that the box would contain.

https://projecteuler.net/problem=100
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from math import sqrt

# --- Conditions of the problem ---
LOWER_BOUND = 10**12


def quadratic_formula(a: int, b: int, c: int) -> tuple[float, float]:
    """Solves roots for an equation of the form 'ax^2 + bx + c = 0'. Returns
    roots as a 2-tuple of floats."""
    root = sqrt(b**2 - 4*a*c)
    denom = 2*a
    return ((-b - root)/denom, (-b + root)/denom)


# --- Calculation & Output ---
def main():
    start = time.time()

    # Iterate through denominator until valid perfect Pr(BB) = 1/2 found.
    denom = LOWER_BOUND + 1
    while (True):
        c = -denom*(denom-1)//2
        blue = quadratic_formula(1,-1,c)[1]

        # Check if root is integer, print denom and solution if so
        if (blue.is_integer()):
            print("Time:", time.time() - start)
            print(int(blue)) # 707106783028
            return

        denom += 1
