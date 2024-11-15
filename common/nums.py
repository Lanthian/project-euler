"""nums.py: Miscellaneous functions for handling number problems."""

__author__ = "Liam Anthian"


# First seen in 025 - 1000-digit Fibonacci Number
def fibonacci_generator(a1: int=1, a2: int=1) :
    """A generator for numbers in a fibonacci sequence starting from a1 & a2."""
    while(True):
        yield a1
        temp = a2
        a2 = a2 + a1
        a1 = temp

# First seen in 025 - 1000-digit Fibonacci Number
def str_fibonacci_generator(a1: int=1, a2: int=1) :
    """A generator for numbers in a fibonacci sequence starting from a1 & a2.
    Slower than standard fibonacci_generator() as it works with strings directly 
    to avoid errors later converting large numbers into strings - does so with
    the function `sum_str_nums()`."""
    a1, a2 = str(a1), str(a2)
    while(True):
        yield a1
        temp = a2
        a2 = sum_str_nums([a2,a1])
        a1 = temp


# First seen in 012 - Highly Divisible Triangular Number
def triangle(num: int) -> int:
    """Returns the `num`th triangle number."""
    return (num * (num+1)) // 2

# First seen in 012 - Highly Divisible Triangular Number
def triangle_generator():
    """A generator for triangle numbers."""
    num = 1
    i = 1
    while(True):
        yield num
        i += 1
        num += i

# First seen in 066 - Diophantine Equation
def square_generator():
    """A generator for square numbers."""
    num = 1
    i = 1
    while(True):
        yield num
        i += 2
        num += i

# First seen in 044 - Pentagon Numbers
def pentagonal(num: int) -> int:
    """Returns the `num`th pentagonal number."""
    return (num * (3*num-1)) // 2

# First seen in 078 - Coin Partitions
def pentagonal_alt(num: int) -> int:
    """Returns the 'num'th pentagonal number of an alt pentagonal sequence."""
    return (num * (3*num+1)) // 2

# First seen in 044 - Pentagon Numbers
def pentagon_generator():
    """A generator for pentagonal numbers."""
    num = 1
    i = 0
    while(True):
        yield num
        i += 1
        num += 5*i - (2*i-1)

# First seen in 045 - Triangular, Pentagonal and Hexagonal
def hexagonal(num: int) -> int:
    """Returns the `num`th hexagonal number. Works by splitting n_gons up into 
    triangles."""
    return num * (2*num-1)

# First seen in 061 - Cyclical Figurate Numbers
def n_gonal(n: int, num: int) -> int:
    """Returns the `num`th n-gonal number. Works by splitting n_gons up into 
    triangles, using the `triangle_generator()` function."""
    return num + (n-2) * triangle(num-1)

# First seen in 061 - Cyclical Figurate Numbers
def n_gonal_generator(n: int):
    """A generator for n-gonal numbers."""
    i = 1
    yield i

    for t in triangle_generator():
        i += 1
        yield (n-2) * t + i


# First seen in 013 - Large Sum
def sum_str_nums(nums: list[str]) -> str:
    """Iteratively adds elements in a list of integers (in string form) `nums`. 
    Done to work around arithmetic errors with large numbers in python. Returns
    sum as a string. Avoids recursion so no limit on number length."""
    # Base case - no number supplied
    if len(nums) == 0: return ""

    summed = ""

    while len(nums):
        prior = []
        current_sum = 0

        # Sum up current digit index
        for num in nums:
            if len(num) == 0: continue
            # If number is longer than 1 digit, add front digits to prior
            if len(num) > 1: prior.append(num[:-1])
            current_sum += int(num[-1])

        # If sum is longer than a single digit, add tens, hundreds, etc to prior
        current_sum = str(current_sum)
        if len(current_sum) > 1: prior.append(current_sum[:-1])

        # Prepare next digit index
        nums = prior 
        summed = current_sum[-1] + summed 
    
    return summed

# First seen in 016 - Power Digit Sum
def digit_sum(num: int) -> int:
    """Takes a number `num` and returns the sum of it's digits as an int."""
    return sum([int(c) for c in str(num)])

# First seen in 92 - Square Digit Chains
def digit_sum_op(num: int, op=lambda x: x) -> int:
    """Takes a number `num` and returns the sum of it's digits as an int, 
    applying operation `op` to each digit before summing."""
    return sum([op(int(c)) for c in str(num)])

# First seen in 022 - Names Scores
def value_word(word, zero=ord('A')-1) -> int:
    """Takes in any character iterable `word` and returns the sum of all it's 
    characters, treating `zero` as the base for 0 in character conversion.
    Takes '@' (A-1) as 0 by default."""
    return sum([ord(letter)-zero for letter in word])

# First seen in 027 - Quadratic Primes
def int_gen(start: int, step: int=1):
    """A generator for integer numbers - starts at `start` (incls) and steps by
    `step` (+1 by default)."""
    while(True):
        yield start
        start += step

# First seen in 030 - Digit Fifth Powers
def find_cap(digit_cost: int) -> int:
    """Taking `digit_cost` as the maximum cost of a digit in a linear problem, 
    finds and returns the int value at which no greater solutions will be found.
    """
    x = 0
    while(digit_cost * x >= 10**x - 1): x+=1
    return(digit_cost * x)

# First seen in 032 - Pandigital Products
def pandigital(seq: str, n: int, strict: bool=True, start: int=1) -> bool:
    """Returns if a string sequence `seq` is n-pandigital or not as a boolean. 
    Pandigital if digits `start` through to `n` inclusive are present once and 
    only once in `seq`. Boolean `strict` can be set to enforce that ONLY digits
    in range are present."""
    RANGE = [str(n) for n in range(start, n+1)]

    # If strict, only allow singular digits in the above range
    if strict:
        seen = set()

        if len(seq) != len(RANGE): return False

        # Check characters in sequence
        for d in seq:
            # If already observed or invalid, return false
            if d in seen or d not in RANGE: return False
            seen.add(d)
        return True

    # Otherwise allow digits and characters outside of range
    else:
        seen = {}

        # Count characters in sequence
        for d in seq:
            if d not in seen: seen[d] = 0
            seen[d] += 1

        # Check digit frequency
        for x in RANGE:
            if x not in seen: return False
            elif seen[x] != 1: return False
        
    return True


# First seen in 043 - Sub-string Divisibility
def charlist_to_int(char_list: list) -> int:
    """Helper function to convert character lists into concatenated integers:
    ['1', '2', '3'] -> 123"""
    return int("".join(char_list))