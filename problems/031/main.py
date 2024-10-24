""" Coin Sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There 
  are eight coins in general circulation:
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

# # Failed attempt to shorthand solution
# def dict_sum_to(goal: int, options: list[int]) -> int:
#     paths = {0:1}
#
#     for i in range(1, goal+1):
#         paths[i] = 0
#
#         for d in options:
#             if d > i: break
#             else: 
#                 if (i-d) % d == 0: paths[i] += paths[i-d]
#
#     return paths[goal]

def sum_from(goal: int, options: list[int], stored: dict[(int,int): int]={}
             ) -> int:
    """Via recursion, returns an integer of the number of possible path 
    permutations to a `goal` integer value, built from combinations of possible 
    addends listed in `options`. Recursions are stored in `stored` to avoid
    repeat calculation."""
    # Attempt to retrieve sum from `stored`
    best = options[-1]
    tup = (goal,best)
    if tup in stored: return stored[tup]

    # Terminating conditions
    if goal == 0: return 1
    elif len(options) <= 1: return 1

    # Recursive steps & `stored` update
    output = 0 if best > goal else sum_from(goal - best, options, stored)
    stored[tup] = output + sum_from(goal, options[:-1], stored)
    return stored[tup]


# --- Calculation & Output ---
def main():
    # print(len(sum_to(0,GOAL,DENOMS))) # 73,682
    # print(simpler_sum_to(0,GOAL,DENOMS)) # 73,682
    print(sum_from(GOAL,DENOMS)) # 73,682
    return
