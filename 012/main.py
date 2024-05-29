""" Highly Divisible Triangular Number

The sequence of triangle numbers is generated by adding the natural numbers. So 
  the 7th triangle number would be 1+2+3+4+5+6+7=28. The first ten terms would 
  be:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
    1: 1
    3: 1, 3
    6: 1, 2, 3, 6
    10: 1, 2, 5, 10
    15: 1, 3, 5, 15
    21: 1, 3, 7, 21
    28: 1, 2, 4, 7, 14, 28
We can see that 28  is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred 
  divisors?
https://projecteuler.net/problem=12
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import sqrt
from primes import factor

# --- Conditions of the problem ---
DIVISORS = 500


def triangle(num: int) -> int:
    """Returns the `num`th triangle number."""
    return (num * (num+1)) // 2

def triangle_generator():
    """A generator for triangle numbers."""
    num = 1
    i = 1
    while(True):
        yield num
        i += 1
        num += i

def factor_count(num: int) -> int:
    """Returns the count of divisors in a number `num`. Includes 1 and num."""
    count = 0
    for i in range(1, num+1):
        # Only check up until sqrt(num) to reduce computation
        if i >= sqrt(num): break
        if factor(num, i): count += 2

    # Don't forget +1 if number is a square
    if factor(num, sqrt(num)): count += 1
    return count


# --- Calculation & Output ---
for i in triangle_generator():
    factors = factor_count(i)
    if factors > DIVISORS: 
        # print(f"{i}: {factor_count(i)}") 
        print(i) # 76,576,500
        break
