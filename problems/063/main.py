""" Powerful Digit Counts

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit 
  number, 134217728 = 8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
https://projecteuler.net/problem=63
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen


# --- Calculation ---
def main():
    count = 0

    # Iterate through possible bases (for base 10 and up, digits always > power)
    for base in range(1,10):
        # Try increasing the power until power exceeds digits
        for power in int_gen(1):
            # If digit count match, increment tally
            digits = len(str(base**power))
            if digits == power: count += 1
            # Otherwise, power exceeds digit count
            else: break


    # --- Output ---
    print(count) # 49
    return
