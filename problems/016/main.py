""" Power Digit Sum

2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
What is the sum of the digits of the number 2^1000?
https://projecteuler.net/problem=16
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import digit_sum

# --- Conditions of the problem ---
NUM = 2 ** (10**3)


# --- Calculation & Output ---
def main():
    print(digit_sum(NUM)) # 1,366
