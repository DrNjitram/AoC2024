from util import *


check_directions = [
    [[-1, 0], [-2, 0], [-3, 0]],
    [[1, 0], [2, 0], [3, 0]],
    [[0, 1], [0, 2], [0, 3]],
    [[0, -1], [0, -2], [0, -3]],
    [[1, 1], [2, 2], [3, 3]],
    [[-1, 1], [-2, 2], [-3, 3]],
    [[-1, -1], [-2, -2], [-3, -3]],
    [[1, -1], [2, -2], [3, -3]]
]


def part1(data: List[str]):
    XMASs = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if "X" == data[y][x]:
                for direction in check_directions:
                    XMAS = "X" + "".join(data[y+dy][x+dx] for dx, dy in direction if inbounds(data, x + dx, y + dy))
                    if XMAS == "XMAS":
                        XMASs += 1
    print(XMASs)
    return XMASs

def part2(data: List[str]):
    XMASs = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if "A" == data[y][x]:

                directions = [
                    [[-1, -1], [1, 1]],
                    [[-1, 1], [1, -1]]
                ]
                found =  True
                for direction in directions:
                    bit = "A".join(data[y + dy][x + dx] for dx, dy in direction if inbounds(data, x + dx, y + dy))
                    bit = list(bit)
                    bit.sort()
                    if not bit == ['A', 'M', 'S']:
                        found = False
                if found:
                    XMASs += 1
    print(XMASs)
    return XMASs


test(read_day(4, 1), part1, 4)
test(read_day(4, 2), part1, 18)
part1(read_day(4, 0))
test(read_day(4, 3), part2, 1)
test(read_day(4, 2), part2, 9)
part2(read_day(4, 0))