""" Powerful Digit Sum

A googol (10^100) is a massive number: one followed by one-hundred zeroes; 
  100^100 is almost unimaginably large: one followed by two-hundred zeroes. 
  Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a,b<100, what is the maximum
  digital sum?
https://projecteuler.net/problem=56
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import digit_sum

# --- Conditions of the problem ---
LIMIT = 100             # Exclusive


# --- Calculation ---
def main():
    best = 0
    for a in range(1,LIMIT):
        for b in range(1,LIMIT):
            s = digit_sum(a**b)
            if s > best: best = s


    # --- Output ---
    print(best) # 972
    return
