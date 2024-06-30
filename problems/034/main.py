""" Digit Factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their
  digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
https://projecteuler.net/problem=34
"""

__author__ = "Liam Anthian"

# --- Imports ---
from math import factorial
from common.nums import find_cap


# --- Calculation ---
def main():
    fac = {i: factorial(i) for i in range(0,10)}
    total = 0

    for num in range(10,find_cap(fac[9])):
        if num == sum([fac[int(n)] for n in str(num)]):
            total += num


    # --- Output ---
    print(total) # 40,730
    return
