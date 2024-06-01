""" Factorial Digit Sum

n! means n x (n-1) x ... x 3 x 2 x 1
For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27.
Find the sum of the digits in the number 100!.
https://projecteuler.net/problem=20
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial

# --- Conditions of the problem ---
NUMBER = 100


# --- Calculation & Output ---
def main():
    print(sum([int(c) for c in str(factorial(NUMBER))])) # 648
