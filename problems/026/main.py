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

# --- Conditions of the problem ---
LIMIT = 1000


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


# --- Calculation ---
def main():
    print(1/7)
    print(long_div(1,7,20))
    # --- Output ---
    return
