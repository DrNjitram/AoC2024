from util import *

data = {}

def find_combos(pattern, towels):
    if not pattern:
        return 1
    poss = 0
    for towel in towels:
        if pattern.startswith(towel):
            next_pattern = pattern[len(towel):]

            if next_pattern not in data:
                data[next_pattern] = find_combos(pattern[len(towel):], towels)
            poss += data[next_pattern]

    data[pattern] = poss
    return poss

def parts(lines):
    global data
    data = {}
    towels = lines[0].split(", ")
    combinations = []
    for pattern in lines[2:]:
        combinations.append(find_combos(pattern, towels))

    print(len([c for c in combinations if c]), sum(combinations))

    return len([c for c in combinations if c]), sum(combinations)

if __name__ == '__main__':
    test(read_day(19, 1), parts, (6, 16))
    test(read_day(19), parts, (293, 623924810770264))