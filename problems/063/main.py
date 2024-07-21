""" Powerful Digit Counts

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit 
  number, 134217728 = 8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
https://projecteuler.net/problem=63
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen

# --- Conditions of the problem ---


# --- Calculation ---
def main():
    count = 0

    # Iterate through possible powers until tipping point reached for digits
    power = 1
    while(len(str(4**power)) <= power):
        # print(power)
        for i in int_gen(1):
            p_s = str(i**power)
            # print(power, p_s)
            if len(p_s) > power: break
            elif len(p_s) == power: 
                print(power, f"{i}**{power}", p_s)
                count += 1

        power += 1

    print(count)

    # --- Output ---
    return
