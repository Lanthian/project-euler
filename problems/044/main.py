""" Pentagon Numbers

Pentagonal numbers are generated by the formula, Pn = n(3n-1)/2. The first ten 
pentagonal numbers are:
    1,5,12,22,35,51,70,92,117,145,...
It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 
  22 = 48, is not pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
  difference are pentagonal and D = |Pk-Pj| is minimised; what is the value of 
  D?
https://projecteuler.net/problem=44
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import pentagon_generator


# --- Calculation & Output ---
def main():
    shape_nums = []
    shape_set = set()

    # Working our way up through pentagonal numbers
    for i in pentagon_generator():
        # And checking for each new possible sum from lower pentagonal numbers
        for n1 in shape_nums[::-1]:

            # Larger of Pk & Pj must be in the higher half
            if n1 < i//2: break

            # Check valid sum
            n2 = i-n1
            if n2 in shape_set:
                # Check valid difference
                dif = n1-n2
                if dif in shape_set:

                    # First valid difference found will be guaranteed lowest,
                    #   given the distance pentagonal numbers only grows as the
                    #   numbers get larger.
                    print(dif) # 5,482,660
                    return

        # Store new pentagonal number
        shape_nums.append(i)
        shape_set.add(i)
