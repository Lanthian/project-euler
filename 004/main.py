""" Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from 
  the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
https://projecteuler.net/problem=4
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
RANGE = (100,999)           # inclusive


def palindrome(iterable) -> bool:
    """Returns a boolean for if an iterable `iterable` is palindromic or not. 
    Works on strings, arrays, tuples - any discrete iterables."""
    # Compare front to back
    for i in range(len(iterable)//2):
        if iterable[i] == iterable[-(i+1)]: continue
        
        # If not palindromic, return false
        else: return False
    return True


# --- Calculation ---
palindromes = []
max_j = RANGE[0]

# Work backwards through range to avoid time spent on lesser palindromes
for i in range(RANGE[-1], RANGE[0]-1, -1):
    # If I < greatest seen J, no possibly larger palindromes left
    if i < max_j: break

    for j in range(RANGE[-1], RANGE[0]-1, -1):
        k = i*j
        
        # Check if product is a palindrome
        if palindrome(str(k)): 
            # Store and update new highest j
            palindromes.append(k)
            if j > max_j: max_j = j

            # No greater palindromes possible from this point forth - break
            break


# --- Output ---
print(max(palindromes)) #906,609
