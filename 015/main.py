# 15 -- too inefficient at the moment, just a brainstorm. Try breaking up into
#       subsets of squares


DOMAIN = [6,6]


start = [0] * len(DOMAIN)

def lattice_step(current: list[int], end: list[int]) -> int:
    if current == end: return 1

    count = 0
    for i in range(len(current)):
        # If at axis end, no further possible steps
        if current[i] == end[i]: continue

        count += lattice_step(current[:i] + [current[i]+1] + current[i+1:], end)

    return count


print(lattice_step(start, DOMAIN))

# 1, 2, 3, 4, 5, 6
# 2, 6, 20, 70, 252, 924
