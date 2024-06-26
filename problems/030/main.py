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

# --- Conditions of the problem ---
POWER = 5


def find_cap(power: int) -> int:
    x = 0
    digit_cost = 9**POWER
    while(digit_cost * x >= 10**x - 1): x+=1
    return(digit_cost * x)


# --- Calculation ---
def main():
    total = 0

    for num in range(10,find_cap(POWER)):
        if num == sum([int(n)**POWER for n in str(num)]):
            total += num


    # --- Output ---
    print(total) # 443,839
    return
