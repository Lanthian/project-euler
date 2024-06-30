""" Digit Fifth Powers

Surprisingly there are only three numbers that can be written as the sum of 
  fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 
    1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers 
  of their digits.
https://projecteuler.net/problem=30
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import find_cap

# --- Conditions of the problem ---
POWER = 5


# --- Calculation ---
def main():
    total = 0

    for num in range(10,find_cap(9**POWER)):
        if num == sum([int(n)**POWER for n in str(num)]):
            total += num


    # --- Output ---
    print(total) # 443,839
    return
