""" Cubic Permutations

The cube, 41063625 (345^3), can be permuted to produce two others cubes: 
  56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
  which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are 
  cube.
https://projecteuler.net/problem=62
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.nums import int_gen
from common.valwrap import ValWrap

# --- Conditions of the problem ---
COUNT = 5


def sort_digits(num: int, reverse: bool=False) -> str:
    """Takes a number `num` and sorts it's digits ascending, or descending if 
    specified by a bool `reverse`, returning this value as a string."""
    ls = list(str(num))
    ls.sort(reverse=reverse)
    return "".join(ls)


# --- Calculation & Output ---
def main():
    cubes = {}
    length = 0

    for i in int_gen(1):
        cube = i**3
        c_s = sort_digits(cube)
        
        # Check current stored values
        if len(c_s) > length:
            length = len(c_s)

            for wrap in cubes.values():
                # If cube permutations match requirement, answer found
                if wrap.val == COUNT: 
                    print(wrap.item) # 127,035,954,683
                    return

            # Reset dictionary store if no matches
            cubes.clear()

        # Populate / update dictionary with new cube values entry
        if c_s not in cubes: cubes[c_s] = ValWrap(1, cube)
        else: cubes[c_s].increment()


    # --- Output ---
    print(cubes[c_s].item)
    return
