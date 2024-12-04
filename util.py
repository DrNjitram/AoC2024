from typing import List, Callable, Any

def read_day(day: int, test: int, split=False, cast=None) -> List[str]:
    return read_lines(rf"Inputs\Day{day}" + (f"_Test{test}" if test else ""), split=split, cast=cast)


def read_lines(filename: str, split=False, cast=None) -> List[str]:
    lines = [line.strip() for line in open(filename).readlines()]
    if split and cast:
        lines = [[cast(i) for i in line.split()] for line in lines]
    elif split:
        lines = [line.split() for line in lines]
    elif cast:
        lines = [cast(line) for line in lines]
    return lines

def print_map(data: List[str]):
    for line in data:
        print(line)

def inbounds(data: List, x:int, y:int) -> bool:
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def test(data, fn: Callable, result: Any):
    print(fn(data) == result)