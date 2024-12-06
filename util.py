from collections import defaultdict
from typing import List, Callable, Any, Tuple

direction_dict = {
    -1j: "^",
    1j: "v",
    1: ">",
    -1: "<"
}

def cast_ray(internal_data: dict[complex, int], p: tuple[complex, complex]) -> complex | None:
    p_pos, p_dir = p
    coords = [k for k,v in internal_data.items() if v == 1]
    deltas = []
    valid = [coord for coord in coords if coord.imag == p_pos.imag or coord.real == p_pos.real]
    for coord in valid:
        delta = (coord-p_pos)/p_dir
        if delta.imag == 0 and delta.real >0:
            deltas.append(delta.real)
    if len(deltas) > 0:
        return min(deltas)
    return None


def read_day(day: int, test: int, **kwargs) -> List[str]:
    return read_lines(rf"Inputs\Day{day}" + (f"_Test{test}" if test else ""), *kwargs)


def read_lines(filename: str, split=False, cast=None, delim=None) -> List[str]:
    lines = [line.strip() for line in open(filename).readlines()]
    if split and cast:
        lines = [[cast(i) for i in line.split(sep=delim)] for line in lines]
    elif split:
        lines = [line.split(sep=delim) for line in lines]
    elif cast:
        lines = [cast(line) for line in lines]
    return lines

def print_map(data: List[str]):
    for line in data:
        print(line)
    print("")

def print_sparse_map(data: dict[complex, Any], keys: dict, unique=None, background = ".") -> None:
    x_s, y_s = zip(*[(int(p.real), int(p.imag)) for p in data.keys()])
    print_keys = {v: k for k, v in keys.items()}
    if unique is not None:
        (pos_p, pos_d), icon = unique
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            if unique is not None and complex(x,y) == pos_p:
                if pos_d != None:
                    line += direction_dict[pos_d]
                else:
                    line += icon
            else:
                line += print_keys.get(data[complex(x,y)], background)
        print(line)
    print("")

def inbounds_c(data: [list|dict], p: complex) -> bool:
    return inbounds(data, int(p.real), int(p.imag))

def inbounds(data: [list|dict], x:int, y:int) -> bool:
    if type(data) in [dict, defaultdict]:
        x_s, y_s = zip(*[(int(p.real), int(p.imag)) for p,v in data.items() if v == 1])
        return min(x_s) <= x <= max(x_s) and min(y_s) <= y <= max(y_s)
    else:
        return 0 <= x < len(data[0]) and 0 <= y < len(data)

def test(data, fn: Callable, result: Any):
    print(fn(data) == result)

def sparse_map(data: List[str], keys: dict, background = ".", unique=None, direction = None) -> Tuple[dict, None|Tuple[int, int]]:
    result = defaultdict(complex)
    unique_position = None
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            if c == unique:
                unique_position = (complex(x, y), direction)
            elif c != background:
                result[complex(x, y)] = keys[c]
    return result, unique_position