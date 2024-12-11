from util import *

memory = {}

def step_stone(stone):
    if stone == 0:
        return [1]
    elif len((string_stone:=str(stone)))%2==0:
        return [int(string_stone[:len(string_stone)//2]), int(string_stone[len(string_stone)//2:])]
    else:
        return [stone*2024]

def part1(Lines):
    answer = 0
    stones = Lines[0]
    while len(stones)>0:
        stone = stones.pop(0)
        for step in range(2):
            print(stone)
            if (stone, step) in memory:
                print("found stone", memory[stone])
            else:
                next_stones = step_stone(stone)
                stone = next_stones.pop(0)
                if len(next_stones)>0:
                    stones.append(next_stones.pop(0))
                #memory[(stone, step)] = step_stone(stone)

                print(f"{stone} -> {step_stone(stone)}")

    print(answer)
    return answer

if __name__ == '__main__':
    test(read_day(11, 1, split=True, cast=int), part1, 55312)