from util import *
from itertools import combinations

def part1_and2(Lines):
    xlim = len(Lines[0])
    ylim = len(Lines)

    antennae = set()
    data = defaultdict(list)
    data_map = defaultdict(int)
    for y in range(len(Lines)):
        for x in range(len(Lines[y])):
            c = Lines[y][x]
            if c != ".":
                antennae.add(c)
                data[c].append((x,y))
                data_map[(x,y)] = c


    anti_nodes1 = set()
    anti_nodes2 = set()
    for antenna in antennae:
        for (x1, y1), (x2,y2) in combinations(data[antenna], 2):
            dx = x1-x2
            dy = y1-y2

            if 0 <= x1+dx < xlim and 0 <= y1+dy < ylim:
                anti_nodes1.add((x1+dx, y1+dy))
            if 0 <= x2-dx < xlim and 0 <= y2-dy < ylim:
                anti_nodes1.add((x2-dx, y2-dy))

            i = 0
            while 0 <= x1 + i * dx < xlim and 0 <= y1 + i * dy < ylim:
                anti_nodes2.add((x1 + i * dx, y1 + i * dy))
                i += 1
            i = 0
            while 0 <= x2 - i * dx < xlim and 0 <= y2 - i * dy < ylim:
                anti_nodes2.add((x2 - i * dx, y2 - i * dy))
                i += 1

    print(len(anti_nodes1), len(anti_nodes2))
    return len(anti_nodes1), len(anti_nodes2)

if __name__ == "__main__":
    test(read_day(8, 1), part1_and2, (14, 34))
    test(read_day(8), part1_and2, (348, 1221))
