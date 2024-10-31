""" Roman Numerals

For a number written in Roman numerals to be considered valid there are basic 
  rules which must be followed. Even though the rules allow some numbers to be 
  expressed in more than one way there is always a "best" way of writing a 
  particular number.
For example, it would appear that there are at least six ways of writing the 
  number sixteen:
    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI
However, according to the rules only XIIIIII and XVI are valid, and the last 
  example is considered to be the most efficient, as it uses the least number of 
  numerals.
The 11K text file, <roman.txt> contains one thousand numbers written in valid, 
  but not necessarily minimal, Roman numerals; 
  see https://projecteuler.net/about=roman_numerals for the definitive rules for 
  this problem.
Find the number of characters saved by writing each of these in their minimal 
  form.
Note: You can assume that all the Roman numerals in the file contain no more 
  than four consecutive identical units.

https://projecteuler.net/problem=89
"""

__author__ = "Liam Anthian"

# --- Imports ---
import time
from common.files import easy_open

# --- Conditions of the problem ---
FILE = "roman.txt"
NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
NUMBERS = [
    (1000,"M"),(900,"CM"),
    (500,"D"),(400,"CD"),
    (100,"C"),(90,"XC"),
    (50,"L"),(40,"XL"),
    (10,"X"),(9,"IX"),
    (5,"V"),(4,"IV"),
    (1,"I")
]

    
def roman_to_int(roman: str) -> int:
    """Translates a Roman numeral `roman` to an integer. Can read invalid Roman 
    numerals so long as they equate to natural numbers. Returns -1 if numeral is 
    overly invalid (illegal characters or <=0)."""
    LETTER, VALUE = (0,1)
    INVALID = -1
    # Try loop to catch any invalid numerals
    try:
        # Initial number
        value = NUMERALS[roman[0]]
        digit_list = [(value, value)]

        for i in range(1, len(roman)):
            value = NUMERALS[roman[i]]
            # If value is equal or decreasing, business as usual
            if value <= digit_list[-1][LETTER]: 
                digit_list.append((value,value))
                continue

            # Otherwise, backtrack to find how much needs to be adjusted
            subtract = 0
            for j in range(len(digit_list)-1,-1,-1):
                # Check against original letter, not potentially subtracted val
                if digit_list[j][LETTER] >= value: break
                subtract += digit_list[j][VALUE]
            # If reached index 0 in backtracking, clear digit_list (done to 
            # distinguish between last digit being <= value or > value)
            else: digit_list = []

            # # Safety check against non-natural number occurences
            # if subtract >= value: return INVALID

            # Trim digit list and append new number
            digit_list = digit_list[:j+1]
            digit_list.append((value, value-subtract))        

        # Output sum of digit outcomes
        total = 0
        for _,v in digit_list:
            total += v
        return total if total > 0 else INVALID

    except KeyError:
        # Invalid character or no characters present
        return INVALID
    
def int_to_roman(num: int) -> str:
    """Tranlates an integer `num` to a minimal Roman numeral string. Returns "N" 
    if number is not natural."""
    if num <= 0: return "N"

    roman = ""
    for value,letter in NUMBERS:
        # Find how many times `value` occurs in `num`
        n = num // value
        if n > 0:
            # Decrease num by this much and update string output
            num %= value
            roman += letter * n
        
        # Break early as necessary
        if num == 0: break

    return roman


# --- Calculation ---
def main():
    start = time.time()

    chars_saved = 0
    # Read in roman numerals from file
    with easy_open(__file__, FILE) as fp:
        for line in fp.readlines():
            line = line.strip()
            chars_saved += len(line) - len(int_to_roman(roman_to_int(line)))


    # --- Output ---
    print("Time:", time.time() - start)
    print(chars_saved) # 743
    return
