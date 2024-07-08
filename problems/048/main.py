""" Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
https://projecteuler.net/problem=48
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
DIGITS = 10
LIMIT = 1000            # Inclusive


def digit_powers(base: int, power: int, digits: int) -> int:
    """Finds the last `digits` digits of base ** power."""
    m = 1
    for _ in range(0,power):
        m *= base
        m_s = str(m)

        # Keep trimming calculation to length `digits`
        if len(m_s) > digits: 
            n = int(m_s[-digits:])

            # Break early if recursion found
            if n == m: break
            else: m = n

    return m


# --- Calculation & Output ---
def main():
    total = sum([digit_powers(i,i,DIGITS) for i in range(1, LIMIT+1)])
    print(str(total)[-DIGITS:]) # 9,110,846,700
    return
