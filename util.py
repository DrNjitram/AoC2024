from typing import List


def read_lines(filename: str) -> List[str]:
    lines = [line.strip() for line in open(filename).readlines()]
    return lines
