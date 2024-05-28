""" Large Sum

Work out the first ten digits of the sum of the following one-hundred 50-digit 
  numbers.
    <numbers.txt>
https://projecteuler.net/problem=13
"""

__author__ = "Liam Anthian"

# --- Imports ---
from operator import mul

# --- Conditions of the problem ---
fp = open("numbers.txt","r")
NUMBERS = [line.strip() for line in fp.readlines()]
print(NUMBERS)


def sum_str_nums(nums: list[str]) -> str:
    if len(nums) == 0: return ""

    pre = []
    sum = 0
    for num in nums:
        if len(num) == 0: continue
        
        pre.append(num[:-1])
        sum += int(num[-1])
    sum = str(sum)
    
    pre.append(sum[:-1])
    return sum_str_nums(pre) + sum[-1]
    


# --- Calculation ---
#


x = "1234"
y = "5678"
print(sum_str_nums([x,y]))

#