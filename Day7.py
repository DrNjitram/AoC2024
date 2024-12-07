import itertools
from multiprocessing import Pool

import numpy as np
from tqdm import tqdm

from util import *

special_fn = False
base_functions = [np.add, np.multiply, lambda a,b:  int(str(a)+str(b))]

def try_combo(num: List[int], fns: List[Callable]) -> int:
    acc = num[0]
    for i, fn in enumerate(fns):
        acc = fn(acc, num[i+1])
    return acc

def test_equation(args) -> int:
    line, special_fn = args
    test_value, num = line.split(": ")
    test_value = int(test_value)
    num = [int(i) for i in num.split()]
    for perm in itertools.product(base_functions[:3 if special_fn else 2], repeat=len(num) - 1):
        if try_combo(num, perm) == test_value:
            return test_value
    return 0

def part1_and2(Lines):
    results1 = run_multiprocessing(test_equation, tuple((line, False) for line in  Lines))
    results2 = run_multiprocessing(test_equation, tuple((line, True) for line in  Lines))

    print(sum(results1), sum(results2))

    return sum(results1), sum(results2)


if __name__ == "__main__":
    test(read_day(7, 1), part1_and2, (3749 ,11387))
    test(read_day(7), part1_and2, (10741443549536, 500335179214836))