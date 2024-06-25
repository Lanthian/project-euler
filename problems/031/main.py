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


# def sum3_to(goal: int, options: list[int]) -> int:
#     # Terminating conditions
#     if goal == 0: return 1
#     elif len(options) == 0: return 1


# --- Calculation & Output ---
def main():
    # print(len(sum_to(0,GOAL,DENOMS))) # 73,682
    # print(simpler_sum_to(0,GOAL,DENOMS)) # 73,682

    print(DENOMS)
    for i in range(1, 21):
        # print(i, ":", dict_sum_to(i, DENOMS), "->", simpler_sum_to(0,i,DENOMS))
        print(i, ":->", [simpler_sum_to(0,i,DENOMS[:d]) for d in range(1, len(DENOMS))])

    return


# 10(17) = 5(7) + 5(17)
#        = 2(2) + 2(7) + 2(2) + 2(17)
#        = 1(0) + 1(2) + 1(1) + 1(7) + 1(0) + 1(2) + 1(1) + 1(17)


"""
[1, 2, 5, 10, 20, 50, 100, 200]
1 :-> [1, 1, 1, 1, 1, 1, 1]
2 :-> [1, 2, 2, 2, 2, 2, 2]
3 :-> [1, 2, 2, 2, 2, 2, 2]
4 :-> [1, 3, 3, 3, 3, 3, 3]
5 :-> [1, 3, 4, 4, 4, 4, 4]
6 :-> [1, 4, 5, 5, 5, 5, 5]
7 :-> [1, 4, 6, 6, 6, 6, 6]
8 :-> [1, 5, 7, 7, 7, 7, 7]
9 :-> [1, 5, 8, 8, 8, 8, 8]
10 :-> [1, 6, 10, 11, 11, 11, 11]
11 :-> [1, 6, 11, 12, 12, 12, 12]
12 :-> [1, 7, 13, 15, 15, 15, 15]
13 :-> [1, 7, 14, 16, 16, 16, 16]
14 :-> [1, 8, 16, 19, 19, 19, 19]
15 :-> [1, 8, 18, 22, 22, 22, 22]
16 :-> [1, 9, 20, 25, 25, 25, 25]
17 :-> [1, 9, 22, 28, 28, 28, 28]
18 :-> [1, 10, 24, 31, 31, 31, 31]
19 :-> [1, 10, 26, 34, 34, 34, 34]
20 :-> [1, 11, 29, 40, 41, 41, 41]

"""