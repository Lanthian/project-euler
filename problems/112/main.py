""" Bouncy Numbers

Working from left-to-right if no digit is exceeded by the digit to its left it 
  is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a 
  decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a 
  "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half
  of the numbers below one-thousand (525) are bouncy. In fact, the least number 
  for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we 
  reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
https://projecteuler.net/problem=112
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.fractions import Fraction
from common.nums import int_gen

# --- Conditions of the problem ---
PROPORTION = Fraction(99,100)


def bouncy(n: int) -> bool:
    """Returns a boolean True if number `n` is bouncy (digits both increase and
    decrease in relation to each other), False if otherwise."""
    asc, desc = (False, False)

    # Convert to string and observe increases and decreases
    n = str(n)
    prev = n[0]
    for c in n[1:]:
        if c > prev: asc = True
        elif c < prev: desc = True

        # If both an ascent and descent has been observed, bouncy
        if asc and desc: return True
        prev = c
    
    # Otherwise not bouncy
    return False


# --- Calculation ---
def main():
    start = time.time()
    
    bouncy_count = 0
    for n in int_gen(1):
        # On non bouncy number discovery (less often than bouncy), update count
        if bouncy(n): 
            bouncy_count += 1

            # Check if needed proportion is obtained exactly
            f = Fraction(bouncy_count, n)
            if f == PROPORTION: break


    # --- Output ---
    print("Time:", time.time() - start)
    print(n)
    return
