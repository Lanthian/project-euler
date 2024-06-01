""" Counting Sundays

You are given the following information, but you may prefer to do some research 
  for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century 
  unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
  (1 Jan 1901 to 31 Dec 2000)?
https://projecteuler.net/problem=19
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.primes import factor

# --- Conditions of the problem ---
RANGE = (1901, 2000)    # Inclusive
TARGET_DAY = 6

DAYS_IN_WEEK = 7
MONTHS = 12
FEB = 1
START_YEAR = 1900
START_DAY = 0

DAYS_IN_MONTHS = {0: 31,        2: 31, 3: 30, 4: 31, 5: 30, 
                  6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}
DAYS_IN_FEB = {False: 28, True: 29}     # Varies if leap year or not


def leap_year(year: int) -> bool:
    """Returns true if `year` is a leap year, false if otherwise."""
    if factor(year, 400): return True
    elif factor(year, 100): return False
    elif factor(year, 4): return True
    return False


# --- Calculation ---
def main():
    day = START_DAY
    count = 0

    # From starting year, work up to and then through each month of given range
    for yr in range(START_YEAR, RANGE[1]+1):#RANGE[1]+1):
        # Only count within range - reset previous counting
        if yr == RANGE[0]: count = 0

        for m in range(MONTHS):
            if day == TARGET_DAY: count += 1

            if m == FEB: day += DAYS_IN_FEB[leap_year(yr)]
            else: day += DAYS_IN_MONTHS[m]

            # Update day of week 
            day %= DAYS_IN_WEEK


    # --- Output ---
    print(count) # 171
    return
