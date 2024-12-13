import re
import time
from collections import defaultdict
from multiprocessing import Pool
from typing import List, Callable, Any, Tuple, Iterable

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

direction_dict = {
    -1j: "^",
    1j: "v",
    1: ">",
    -1: "<"
}

adj4 = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1]
]
adj8 = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1],
    [-1, -1],
    [1, 1],
    [-1, 1],
    [1, -1]
]

def print_garden(edges, plot):
    xy, uv = zip(*edges)
    plt.scatter(*zip(*plot))
    plt.quiver(*zip(*xy), *zip(*uv), scale_units="xy", scale=1)
    plt.title(f"{len(edges)}, {len(plot)},{len(plot) * len(edges)}")
    plt.show()

def cast_ray(internal_data: dict[complex, int], p: tuple[complex, complex]) -> int | None:
    p_pos, p_dir = p
    coords = [k for k,v in internal_data.items() if v == 1 and k.imag == p_pos.imag or k.real == p_pos.real]
    deltas = []

    if not coords:
        return None

    for coord in coords:
        delta = (coord-p_pos)/p_dir
        if delta.imag == 0 and delta.real >0:
            deltas.append(int(delta.real))

    if len(deltas) > 0:
        return min(deltas)

def is_int(x):
    return np.mod(x+0.0001, 1) < 0.001

def read_day(day: int, test_part=0, **kwargs) -> List[str]:
    return read_lines(rf"Inputs\Day{day}" + (f"_Test{test_part}" if test_part else ""), **kwargs)


def read_lines(filename: str, split=False, cast=None, delim=None, regex=None) -> List[str]:
    lines = [line.strip() for line in open(filename).readlines() if line.strip() != ""]
    if split and cast:
        lines = [[cast(i) for i in line.split(sep=delim)] for line in lines]
    elif split:
        lines = [line.split(sep=delim) for line in lines]
    elif regex:
        if cast:
            lines = [[cast(i) for i in re.findall(regex, line)] for line in lines]
        else:
            lines = [re.findall(regex, line) for line in lines]
    elif cast:
        lines = [cast(line) for line in lines]

    return lines

def print_map(data: List[str]):
    for line in data:
        print(line)
    print("")

def print_sparse_map(data: dict[Any, Any], keys=None, unique=None, background = ".") -> None:
    complex_map = False
    if type([type(k) for k in data.keys()][0]) == complex:
        complex_map = True
        x_s, y_s = zip(*[(int(p.real), int(p.imag)) for p in data.keys()])
    else:
        x_s, y_s = zip(*[p for p in data.keys()])
    if keys is not None:
        print_keys = {v: k for k, v in keys.items()}
    else:
        print_keys = {v: v for k, v in data.items()}
    pos_p = None

    if unique is not None:
        (pos_p, pos_d), icon = unique
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            if complex_map:
                pos = complex(x,y)
            else:
                pos = (x,y)
            if unique is not None and pos == pos_p:
                if pos_d is not None:
                    line += direction_dict[pos_d]
                else:
                    line += icon
            else:
                line += print_keys.get(data[pos], background)
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
    start_time = time.perf_counter_ns()

    print(fn(data) == result)
    print(f"Time: {(time.perf_counter_ns() - start_time)/1E6:.2f}ms")

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

def run_multiprocessing(fn: Callable, args: Iterable) -> list:
    with Pool() as pool:
        results = list(
            tqdm(
                pool.imap_unordered(
                    fn,
                    args
                ),
                total=len(args)))
    return results