from typing import List


def read_lines(filename: str, split=False, cast=None) -> List[str]:
    lines = [line.strip() for line in open(filename).readlines()]
    if split and cast:
        lines = [[cast(i) for i in line.split()] for line in lines]
    elif split:
        lines = [line.split() for line in lines]
    elif cast:
        lines = [cast(line) for line in lines]
    return lines
