from functools import reduce
from operator import mul

from util import *

def print_map(data, x_max, y_max):
    for y in range(y_max):
        line = ""
        for x in range(x_max):
            if (x,y) in data:
                robots = len(data[(x,y)])
                line += str(robots)
            else:
                line += "."
        print(line)
    print("")

def step_robots(data, x_max, y_max, seconds=1):
    new_data = defaultdict(list)
    for (x,y), robots in data.items():
        if robots:
            for vx,vy in robots:
                new_data[((x+seconds*vx)%x_max,(y+seconds*vy)%y_max)].append((vx,vy))

    return new_data

def part1_and2(Lines):
    data = defaultdict(list)
    for x,y,vx,vy in Lines:
        data[(x,y)] += [(vx,vy)]
    x_max, y_max = map(max, zip(*[(p[0]+1, p[1]+1) for p in data.keys()]))

    new_data = step_robots(data, x_max, y_max, 100)
    Q = [0, 0, 0, 0]
    for (x, y), robots in new_data.items():
        if x < x_max // 2:
            if y < y_max // 2:
                Q[0] += len(robots)
            elif y > y_max // 2:
                Q[1] += len(robots)
        elif x > x_max // 2:
            if y < y_max // 2:
                Q[2] += len(robots)
            elif y > y_max // 2:
                Q[3] += len(robots)
    answer = reduce(mul, Q)
    print(answer)

    i = 0
    while True:
        data = step_robots(data, x_max, y_max)

        found = 0
        for (x, y) in data.keys():
            for dx, dy in adj8:
                if (x+dx, y+dy) not in data:
                    break
            else:
                found=i+1

        if found:
            break
        i += 1


    print(found)
    return answer, found

if __name__ == '__main__':
    #test(read_day(14, 1, regex=r'-?\d+', cast=int), part1_and2, 12)
    test(read_day(14, regex=r'-?\d+', cast=int), part1_and2, (226548000, 7753))