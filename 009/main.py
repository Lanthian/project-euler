""" Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
    a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
https://projecteuler.net/problem=9
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul

# --- Conditions of the problem ---
SUM = 1000


def pythag_trip(a: int, b: int, c: int) -> bool:
    """Returns if three terms `a`, `b` and `c` are a pythagorean triplet."""
    return a**2 + b**2 == c**2


# --- Calculation & Output ---
# Flag to get out of double loop without using a function / quit()
found = False

for a in range(1, SUM//3):
    for b in range(a+1, (SUM-a)//2):
        c = SUM - a - b
        
        if pythag_trip(a,b,c): 
            print(a*b*c) # 31875000
            found = True
            break
    if found: break
