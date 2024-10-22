"""nums.py: Miscellaneous functions for handling number problems."""

__author__ = "Liam Anthian"


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


# First seen in 016 - Power Digit Sum
def digit_sum(num: int) -> int:
    """Takes a number `num` and returns the sum of it's digits as an int."""
    return sum([int(c) for c in str(num)])

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
