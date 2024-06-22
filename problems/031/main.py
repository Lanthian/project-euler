"""
https://projecteuler.net/problem=31
"""

__author__ = "Liam Anthian"

# --- Imports ---

# --- Conditions of the problem ---
GOAL = 200
DENOMS = [1,2,5,10,20,50,100,200]

def sum_to(curr: int, goal: int, options: list[int]) -> list[list[int]] | bool:
    result = []
    if curr == goal: return True

    else:
        # For each possible action added to 
        for i,n in enumerate(options):
            next_val = curr + n

            if next_val > goal: continue
            elif next_val == goal: result.append([n])
            
            else:
                # Check paths to goal from this next_val
                paths = sum_to(next_val, goal, options[i:])
                # If no paths possible, skip next_val
                if paths == False: continue

                # Otherwise, return end paths to goal from next_val
                result.extend([[n] + path for path in paths])
    
    if len(result) == 0: return False
    else: return result


# --- Calculation & Output ---
def main():
    print(len(sum_to(0,GOAL,DENOMS))) # 73,682
    return
