""" Number Letter Counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
  then there are 3+3+5+4+4=19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
  words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 352 (three hundred and forty-
  two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
  letters. The use of "and" when writing out numbers is in compliance with 
  British usage.
https://projecteuler.net/problem=17
"""

__author__ = "Liam Anthian"

# --- Imports ---
import re

# --- Conditions of the problem ---
LIMIT = 1000            # Inclusive


def number_to_english(num: int) -> str:
    """Converts any int number `num` in range (-1E9,1E9) to English text. 
    Returns this string."""
    # Exception case
    if num == 0: return "zero"

    # Handle negatives
    neg = ""
    if num < 0:
        neg = "minus "
        num *= -1
    numstr = str(num)

    terms = ["", " thousand", " million", " billion", " trillion"]
    limit = 1 * 10 ** 15
    if num >= limit: return "out_of_range"

    outs = []
    while (len(numstr) != 0):
        n = hundred_to_english(int(numstr[-3:]))
        t = terms.pop(0)
        if n != "": outs.insert(0, n + t)
        numstr = numstr[:-3]

    return neg + " and ".join(outs)

def hundred_to_english(num: int) -> str:
    """Converts a number in range (0,1000) to English text. Returns this str."""
    # Conversion dictionaries
    DIGITS = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
              "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    TEENS = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", 
             "14": "fourteen", "15": "fifteen", "16": "sixteen", 
             "17": "seventeen", "18": "eighteen", "19": "nineteen"}
    TENS = {"0": "", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty",
            "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

    # Handle misuse / illegal input
    out = ""
    numstr = str(num)
    if len(numstr) > 3: return "out_of_range"
    
    # Handle hundreds
    elif len(numstr) == 3: 
        out += DIGITS[numstr[0]] + " hundred"

        # Break early if clean 'x' hundred.
        if int(numstr[1:]) == 0: return out

        # Otherwise append 'and' and trim hundred digit
        out += " and "
        numstr = numstr[1:]

    # Handle teens
    if int(numstr) == 0: return out
    elif 9 < int(numstr) < 20:
        out += TEENS[numstr]
        return out
    
    # Handle tens
    if len(numstr) == 2:
        out += TENS[numstr[0]]
        
        # Break early if clean tens digit.
        if int(numstr[1]) == 0: return out

        # Otherwise append '-' and trim tens digit
        elif int(numstr[0]) != 0: out += "-"
        numstr = numstr[1:]

    # Handle digit & return
    out += DIGITS[numstr[0]]
    return out


# --- Calculation ---
def main():
    count = 0
    for i in range(1, LIMIT+1):
        count += len(re.sub(r"[ -]", "", number_to_english(i)))


    # --- Output ---
    print(count) # 21,124


# --- Further improvements ---
"""
Could instead calculate based on patterns, e.g. how many characters in 0-100,
  characters in 1000, consequently characters in 100,000-1,000,000 in turn.
Would run much faster then the current approach of playing out (generating) all
  written forms.
"""
