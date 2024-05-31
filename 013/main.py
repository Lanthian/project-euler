""" Large Sum

Work out the first ten digits of the sum of the following one-hundred 50-digit 
  numbers.
    <numbers.txt>
https://projecteuler.net/problem=13
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
fp = open("numbers.txt","r")
NUMBERS = [line.strip() for line in fp.readlines()]
DIGITS = 10


def sum_str_nums(nums: list[str]) -> str:
    """Recursively adds elements in a list of integers (in string form) `nums`. 
    Done to work around arithmetic errors with large numbers in python. Returns
    sum as a string."""
    # Base case - no further recursion needed
    if len(nums) == 0: return ""

    prior = []
    sum = 0

    for num in nums:
        if len(num) == 0: continue
        # If number is longer than 1 digit, add front digits to prior
        if len(num) > 1: prior.append(num[:-1])
        sum += int(num[-1])

    # If sum is longer than a single digit, add tens, hundreds, etc to prior
    sum = str(sum)
    if len(sum) > 1: prior.append(sum[:-1])

    # Recursive step
    return sum_str_nums(prior) + sum[-1]


# --- Calculation & Output ---
def main():
    print(sum_str_nums(NUMBERS)[:DIGITS])
