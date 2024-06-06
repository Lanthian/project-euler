""" 1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000
  digits?
https://projecteuler.net/problem=25
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
LENGTH = 1000


def fibonacci_generator(a1: int, a2: int) :
    """A generator for numbers in a fibonacci sequence, starting from a1."""
    while(True):
        yield a1
        temp = a2
        a2 = a2 + a1
        a1 = temp


# --- Calculation & Output ---
def main():
    for i,fib in enumerate(fibonacci_generator(1,1),1):
        if len(str(fib)) >= LENGTH:
            print(i) # 4,782
            break
    return
