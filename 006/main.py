""" Sum Square Difference

The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is,
    (1+2+...+10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural 
  numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred 
  natural numbers and the square of the sum.
https://projecteuler.net/problem=6
"""

__author__ = "Liam Anthian"

# --- Conditions of the problem ---
RANGE = (1,100)         # inclusive


# --- Calculation ---
def main():
    sum_of_sqrs = sum([x**2 for x in range(RANGE[0],RANGE[1]+1)])
    sqr_of_sums = sum(range(RANGE[0], RANGE[1]+1)) ** 2


    # --- Output ---
    print(sqr_of_sums-sum_of_sqrs) # 25,164,150


# --- Further explored ---
"""
# https://planetmath.org/squareofsum#:~:text=The%20square%20of%20a%20sum,jaiaj.
# sqr_of_sums = sum_of_sqrs + "sum of all double products of summands in twos"

n = RANGE[1]
sum_of_sqrs = (n*(n+1)*(2*n+1)//6)

sum_of_biprods = 0
for i in range(RANGE[0],RANGE[1]+1):
    for j in range(RANGE[0],i):
        sum_of_biprods += i * j
sum_of_biprods *= 2

sqr_of_sums = sum_of_sqrs + sum_of_biprods

print(sum_of_biprods) # 25,164,150
"""
