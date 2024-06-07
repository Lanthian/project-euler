""" Reciprocal Cycles

A unit fractions contains 1  in the numerator. The decimal representation of the
  unit fractions with denominators 2 to 10 are given:
    1/2 = 0.5
    1/3 = 0.(3)
    1/4 = 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
  seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
  its decimal fraction part.
https://projecteuler.net/problem=26
"""

__author__ = "Liam Anthian"

# --- Imports ---
from re import sub

# --- Conditions of the problem ---
DIVIDEND = 1
LIMIT = 1000            # Exclusive


def long_div(dividend: float, divisor: float, decimals: int) -> str:
    """Calculates the division of number `dividend` by number `divisor` up to 
    decimal place `decimals`. Return this result as a string."""
    out = ""
    str_div = str(dividend)
    
    carry = 0
    decimal_flag = False

    while (len(str_div) != 0):
        # Check for segue to decimals
        if str_div[0] == ".": 
            out += str_div[0]
            decimal_flag = True
        
        else:
            # Count the number of decimal places calculated so far
            if decimal_flag:
                # Stop calculation if enough presented
                if decimals == 0: break
                decimals -= 1

            # Calculate division at current place
            cur_div = carry + int(str_div[0])
            out += str(cur_div // divisor)
            carry = 10 * (cur_div % divisor)
        
        # Step forward
        str_div = str_div[1:]
        if len(str_div) == 0 and decimals > 0:
            # Append decimal point if missing and extend dividend by a zero
            if decimal_flag == False: str_div += "."
            str_div += "0"

    # Return result, dropping leading and trailing 0s
    trimmed = out.strip("0")
    if trimmed[0] == ".": trimmed = "0" + trimmed   # reattach 0 before .
    if trimmed[-1] == ".": trimmed = trimmed[:-1]   # drop pointless .
    return trimmed

# def sub_reps(seq: str) -> list[str]:
#     """Finds and returns a sorted list of all repeated sub-patterns in a string 
#     sequence `seq`."""
#     subs = set()
#     for i in range(len(seq)):
#         for j in range(i+1, len(seq)+1):
#             if seq[i:j] in seq[j:]: subs.add(seq[i:j])
#    
#     out = list(subs)
#     out.sort()
#     return out

# def sub_suc_reps(seq: str) -> list[str]:
#     """Finds and returns a sorted list of all complete (max length) repeated, 
#     successive sub-patterns within string `sequence`."""
#     subs = set()
#
#     # Across each possible subsequence of the sequence `seq`;
#     for i in range(len(seq)):
#         for j in range(i+1, len(seq)+1):
#
#             # Check if successive subsequence is equal
#             if seq[i:j] == seq[j:2*j-i]:
#                 # And if no sub successive patterns within sequence, add to set
#                 if len(sub_suc_reps(seq[i:j])) == 0: subs.add(seq[i:j])
#    
#     out = list(subs)
#     out.sort()
#     return out

def sub_cycle(seq: str) -> str:
    """Finds and returns the first repeated, successive sub-pattern (cycle) 
    within string `sequence`. If no cycled pattern found, returns empty string. 
    
    Note: pattern is only checked to repeat once, strings such as "aab" will 
    wrongfully return "a" as a cycle.
    Would be more accurately named 'sub_successive_rep()'"""
    subs = set()

    # Across each possible subsequence of the sequence `seq`;
    for i in range(len(seq)):
        for j in range(i+1, len(seq)+1):

            # Check if successive subsequence is equal
            if seq[i:j] == seq[j:2*j-i]:
                # And if no repeats of cycle within sequence, add to set
                if len(sub_cycle(seq[i:j])) == 0: return seq[i:j]
    
    return ""


# --- Calculation ---
def main():
    MAX_LENGTH_CHECKED = 100

    max_cycle_divisor = None
    max_cycle_length = 0

    for i in range(1, LIMIT):
        # Find decimal places for division by `i`, and then maximum cycle length
        decimal = sub(r'\d+[.]', '', long_div(DIVIDEND, i, MAX_LENGTH_CHECKED))
        length = len(sub_cycle(decimal))

        # Update best divisor if new better divisor found
        if length > max_cycle_length:
            max_cycle_divisor = i
            max_cycle_length = length
            

    # --- Output ---
    print(max_cycle_divisor)
    return


# --- Future improvements ---
"""
Generate decimal places until a cycle is present (if divisor isn't even), rather 
than generating a fixed number of decimal places for every division and THEN 
checking if there is a cycle and of what length. This way, guaranteed to find 
max cycle length for any limit, rather than having to change max_length_checked.
"""
