""" Coin Sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

https://projecteuler.net/problem=31
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
GOAL = 200
DENOMS = [1,2,5,10,20,50,100,200]


def sum_to(curr: int, goal: int, options: list[int]) -> list[list[int]] | bool:
    """Takes a current integer value `curr`, a `goal` integer value, and a list
    of possible addends `options` which can be permutated to reach this goal.
    Returns a boolean for if path is valid or not if at path end, otherwise via
    recursion returns an ordered list of all paths."""
    result = []
    if curr == goal: return True

    else:
        # For each possible action from current, check sub paths to goal
        for i,n in enumerate(options):
            next_val = curr + n

            if next_val > goal: continue
            elif next_val == goal: result.append([n])
            
            else:
                # todo: would like to fail earlier here, rather than sprouting 
                #       so many paths that can't possible be solved.

                # Check paths to goal from this next_val
                paths = sum_to(next_val, goal, options[i:])
                # If no paths possible, skip next_val
                if paths == False: continue

                # Otherwise, return end paths to goal from next_val
                result.extend([[n] + path for path in paths])
    
    if len(result) == 0: return False
    else: return result


def simpler_sum_to(curr: int, goal: int, options: list[int]) -> int:
    """Takes a current integer value `curr`, a `goal` integer value, and a list
    of possible addends `options` which can be permutated to reach this goal.
    Via recursion, returns an integer of the number of possible path 
    permutations to goal."""
    if curr == goal: return 1

    else:
        # For each possible action from current, check sum sub paths to goal
        result = 0
        for i,n in enumerate(options):
            next_val = curr + n

            if next_val > goal: continue
            
            else:
                # Add total (recursive) valid sub paths to result
                result += simpler_sum_to(next_val, goal, options[i:])
        
        return result


# --- Calculation & Output ---
def main():
    print((simpler_sum_to(0,GOAL,DENOMS))) # 73,682
    return
