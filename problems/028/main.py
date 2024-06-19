""" Number Spiral Diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 
  by 5 spiral is formed as follows:
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
  in the same way?
https://projecteuler.net/problem=28
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
LIMIT = 1001 * 1001     # Inclusive


# --- Calculation ---
def main():
    sum = 1
    num = 1
    i = 1       # current depth of spiral from centre

    # Spiral through numbers until limit reached, summing the diagonals
    while (num < LIMIT):
        
        # Check each corner of current spiral depth
        for _ in range(4):
            num += 2*i
            # If limit passed, stop iteration
            if num > LIMIT: break
            sum += num
        i+=1


    # --- Output ---
    print(sum) # 669,171,001
    return
