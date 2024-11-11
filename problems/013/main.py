""" Large Sum

Work out the first ten digits of the sum of the following one-hundred 50-digit 
  numbers.
    <numbers.txt>
https://projecteuler.net/problem=13
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.files import easy_open
from common.nums import sum_str_nums

# --- Conditions of the problem ---
FILE = "numbers.txt"
DIGITS = 10


# --- Calculation & Output ---
def main():
    # Read in data
    fp = easy_open(__file__, FILE, "r")
    numbers = [line.strip() for line in fp.readlines()]
    fp.close()

    print(sum_str_nums(numbers)[:DIGITS])
