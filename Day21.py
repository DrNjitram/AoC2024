from functools import cache
from itertools import permutations
from util import *

numerical_positions = {             "0": (1, 2), "A": (2, 2),
                       "1": (0, 3), "2": (1, 3), "3": (2, 3),
                       "4": (0, 4), "5": (1, 4), "6": (2, 4),
                       "7": (0, 5), "8": (1, 5), "9": (2, 5)
                        }
directional_dict = {"<": (0, 0), "v": (1, 0), ">": (2, 0), "^": (1, 1), "A": (2, 1)}
delta_dict = {"<": (-1, 0), "v": (0, -1), ">": (1, 0), "^": (0, 1)}
forbidden = {(0, 1), (0, 2)}

@cache
def get_valid_paths(start: tuple[int, int], end: tuple[int, int]):
    if start == end:
        return ["A"]
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    opts = []
    opts += ([">"] if dx>0 else ["<"])*abs(dx)
    opts += (["^"] if dy>0 else ["v"])*abs(dy)
    paths = set(permutations(opts))
    valid_paths = set()

    for path in paths:
        x1, y1 = start
        for step in path:
            dx, dy = delta_dict[step]
            x1 += dx
            y1 += dy
            if (x1, y1) in forbidden:
                break
        else:
            valid_paths.add("".join(path) + "A")

    return list(valid_paths)


@cache
def get_path(inst: str, depth: int, start_depth: int) -> int:
    inst = "A" + inst
    length = 0
    for i in range(len(inst) - 1):
        a = numerical_positions[inst[i]] if depth == start_depth else directional_dict[inst[i]]
        b = numerical_positions[inst[i+1]] if depth == start_depth else directional_dict[inst[i+1]]
        if depth:
            length += min(get_path(p, depth-1, start_depth) for p in get_valid_paths(a, b))
        else:
            length += len(get_valid_paths(a, b)[0])
    return length


def parts(lines, depth=3):
    answer = 0
    for inst in lines:
        ans = get_path(inst, depth-1, depth-1)
        answer += ans*int(inst[:-1])

    print(answer)
    return answer

if __name__ == '__main__':
    test(read_day(21, 1), parts, 126384)
    test(read_day(21, 1), parts, 154115708116294, depth=26)
    test(read_day(21, 2), parts, 123246)
    test(read_day(21, 2), parts, 150206177445908, depth=26)
    test(read_day(21), parts, 231564)
    test(read_day(21), parts, 281212077733592, depth=26)
