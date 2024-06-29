""" Double-base Palindromes

The decimal number, 585 - 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in 
  base 10 and base 2.
(Please note that the palindromic number, in either base, may not include 
  leading zeroes.)
https://projecteuler.net/problem=36
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import palindrome

# --- Conditions of the problem ---
LIMIT = 10**6


# --- Calculation ---
def main():
    total = 0
    for num in range(1, LIMIT):
        if palindrome(str(num)): 
            if palindrome(bin(num)[2:]): total += num

    
    # --- Output ---
    print(total) # 872,187
    return
