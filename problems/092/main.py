""" Square Digit Chains

A number chain is created by continuously adding the square of the digits in a
  number to form a new number until it has been seen before.
For example,
    44 -> 32 -> 13 -> 10 -> 1 -> 1
    85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
  loop. What is most amazing is that EVERY starting number will eventually 
  arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?

https://projecteuler.net/problem=92
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.nums import digit_sum_op

# --- Conditions of the problem ---
LIMIT = 10**7


# --- Calculation ---
def main():
    start = time.time()
    
    # Helper function for square digit sums
    func = lambda x: digit_sum_op(x, lambda y: y**2)
    
    # Iterate through all numbers, tracking the 89s
    nums = [0]*(LIMIT+1)
    count = 0
    for n,val in enumerate(nums[1:], 1):
        # Skip already seen numbers
        if val: continue

        path = [n]
        while(n != 1 and n != 89):
            n = func(n)
            # Break early if encountering past chain
            if nums[n]: 
                n = nums[n]
                break
            path.append(n)
        
        # Backpropagate chain end value through path
        for i in path: nums[i] = n
        if n == 89: count += len(path)    
    

    # --- Output ---
    print("Time:", time.time() - start)
    print(count)
    return
