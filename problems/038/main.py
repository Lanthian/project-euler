""" Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will 
  call 192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1,2,3,4, and 5, 
  giving the pandigital, 918273645, which is the concatenated product of 9 and
  (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
  concatenated product of an integer with (1,2,...,n) where n > 1?
https://projecteuler.net/problem=38
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen, pandigital

# --- Conditions of the problem ---
DIGITS = 9


# --- Calculation ---
def main():
    best = None

    # Work backwards through possible starts to pandigital
    for i in range(10**((DIGITS)//2)-1, 0, -1):
        concat = str(i)

        # Concatenate with later products
        for j in int_gen(2):
            concat += str(i*j)
            
            if len(concat) > DIGITS: break
            elif len(concat) == DIGITS: 
                # Set largest pandigital from pattern i * (1,2,...,n)
                if pandigital(concat, DIGITS, True): best = concat
                break
        
        # Stop searching if greatest satisfactory pandigital found
        if best != None: break
  

    # --- Output ---
    print(best) # 932,718,654
    return
