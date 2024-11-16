""" Non-bouncy Numbers

Working from left-to-right if no digit is exceeded by the digit to its left it 
  is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a 
  decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a 
  "bouncy" number; for example, 155349.
As n increases, the proportion of bouncy numbers below n increases such that 
  there are only 12951 numbers below one-million that are not bouncy and only 
  277032 non-bouncy numbers below 10^10.
How many numbers below a googol (10^100) are not bouncy?
https://projecteuler.net/problem=113
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.iters import ruled_combo_gen

# --- Conditions of the problem ---
DIGIT_LIMIT = 6
NUMBERS = list(range(0,10))

# --- Calculation ---
def main():
    start = time.time()

    # Rules for forming all decreasing numbers 
    # - can't start with 0
    rules = {1: [lambda x: x[0] != 0]}
    # - and can't be greater than predecessor
    rules.update({
        i: [lambda x, i=i: x[i-1] <= x[i-2]] for i in range(2,DIGIT_LIMIT+1)
    })

    # Generate all non-bouncy number combinations below the digit limit
    count = 0
    for i in ruled_combo_gen(NUMBERS, max_length=DIGIT_LIMIT, rules=rules):
        if not i:
            print("No valid combinations discovered.")
            break

        # print("".join([str(c) for c in i]))

        # If number neutral (both increasing and decreasing), only count once
        if len(set(i)) == 1: count += 1
        # Otherwise count twice to include the increasing numbers
        else: count += 2

    # --- Output ---
    print("Time:", time.time() - start)
    print(count)
    return
