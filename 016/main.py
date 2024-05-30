""" Power Digit Sum

2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
What is the sum of the digits of the number 2^1000?
https://projecteuler.net/problem=16
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
NUM = 2 ** (10**3)


# --- Calculation & Output ---
print(sum([int(d) for d in str(NUM)])) # 1,366
