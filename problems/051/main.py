""" Prime Digit Replacements
https://projecteuler.net/problem=51
"""

__author__ = "Liam Anthian"

# --- Imports ---
from common.iters import permutation_generator, sublists
from common.primes import prime_sieve

# --- Conditions of the problem ---
FAMILY = 6


def equal_index(num: str, indices: list[int]) -> bool:
    """Takes a number in string form, checking if all `indices` specified are
    equal. Returns this check as a boolean."""
    base = num[indices[0]]
    for i in indices[1:]:
        if num[i] != base: return False
    return True


# --- Calculation ---
def main():
    # print(sublists([1,2,3]))


    digits = 0
    flag = True

    families = {}

    while(True):
        # Increment digit count
        digits += 1
        families[digits] = {}

        # Prepare index replacement sublists
        subs = sublists(list(range(digits)))[1:-1]
        print(subs)

        # Generate primes of length 'digits'
        lower_bound = 10**(digits-1)-1
        primes = [p for p in prime_sieve(10**digits) if p > lower_bound]
        print(primes)

        # Sort primes by valid index replacements
        for indices in subs:
            i_s = "".join([str(i) for i in indices])
            for p in primes:
                p_s = str(p)

                # print(i_s+'.'+p_s)

                # # Check if valid index replacement here
                # if equal_index(p_s, indices):
                #     # Create initial dict entry if unstored
                #     if p_s





        if digits == 3: break
        # prime_set = set(primes)
        
        # for p in primes:
        #     permutation_generator(p)


    # --- Output ---
    return
