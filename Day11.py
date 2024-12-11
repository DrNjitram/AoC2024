from functools import reduce
from operator import add
from util import *

memory = {}

def step_stone(stone):
    if stone == 0:
        return [1]
    elif len((string_stone:=str(stone)))%2==0:
        return [int(string_stone[:len(string_stone)//2]), int(string_stone[len(string_stone)//2:])]
    else:
        return [stone*2024]

def get_num_stones(stones, step):
    if not step:
        return len(stones)
    length = 0
    for stone in stones:
        if (stone, step) in memory:
            ans = memory[(stone, step)]
        else:
            ans = get_num_stones(step_stone(stone), step - 1)
            memory[(stone, step)] = ans
        length += ans
    return length

def part1(Lines):
    stones = Lines[0]
    answer1 = get_num_stones(stones, 25)
    answer2 = get_num_stones(stones, 75)
    print(answer1, answer2)
    return answer1, answer2

if __name__ == '__main__':
    test(read_day(11, 1, split=True, cast=int), part1, (55312, 65601038650482))
    test(read_day(11, split=True, cast=int), part1, (216996, 257335372288947))