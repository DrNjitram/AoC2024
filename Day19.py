from functools import cache
from util import *

towels = []

@cache
def find_combos(pattern):
    if not pattern:
        return 1
    poss = 0
    for towel in towels:
        if pattern.startswith(towel):
            poss += find_combos(pattern[len(towel):])
    return poss

def parts(lines):
    global towels
    find_combos.cache_clear()
    towels = lines[0].split(", ")
    combinations = [find_combos(pattern) for pattern in lines[2:]]

    print(len([c for c in combinations if c]), sum(combinations))
    return len([c for c in combinations if c]), sum(combinations)

if __name__ == '__main__':
    test(read_day(19, 1), parts, (6, 16))
    test(read_day(19), parts, (293, 623924810770264))