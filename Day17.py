import numpy as np

from util import *

class Computer:
    def __init__(self, A:int, B:int, C:int, program:list[int], p=False):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.ip = 0
        self.output = []
        self.p = p

    def combo_operand(self, operand:int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C
            case _:
                raise Exception("Invalid operand")

    def run(self):
        while self.ip < len(self.program):
            if self.p:
                print(f"ip:{self.ip} A:{self.A} B:{self.B} C:{self.C}")
            instruction = self.program[self.ip]
            operand = self.program[self.ip+1]
            match instruction:
                case 0: # adv
                    if self.p:
                        print(f"A = {self.A}//{np.power(2, self.combo_operand(operand))} op:{operand}")
                    self.A = self.A//np.power(2, self.combo_operand(operand))
                    self.ip += 2
                case 1: # bxl
                    if self.p:
                        print(f"B = B ^ op = {self.B} ^ {operand}")
                    self.B = np.bitwise_xor(self.B, operand)
                    self.ip += 2
                case 2: # bst
                    if self.p:
                        print(f"B = B % 8 = {self.combo_operand(operand)} % 8  op:{operand}")
                    self.B = self.combo_operand(operand) % 8
                    self.ip += 2
                case 3: # jnz
                    if self.A > 0:
                        if self.p:
                            print(f"jmp to {operand}")
                        self.ip = operand
                    else:
                        if self.p:
                            print(f"no jmp")
                        self.ip += 2
                case 4: # bxc
                    if self.p:
                        print(f"B = B ^ C = {self.B} ^ {self.C}")
                    self.B = np.bitwise_xor(self.B, self.C)
                    self.ip += 2
                case 5: # out
                    if self.p:
                        print(f"out {self.combo_operand(operand) % 8}  op:{operand}")
                    self.output.append(self.combo_operand(operand)%8)
                    self.ip += 2
                case 6:  # bdv
                    if self.p:
                        print(f"B  = {self.A}//{np.power(2, self.combo_operand(operand))}  op:{operand}")
                    self.B = self.A // np.power(2, self.combo_operand(operand))
                    self.ip += 2
                case 7:  # cdv
                    if self.p:
                        print(f"C = {self.A}//{np.power(2, self.combo_operand(operand))}  op:{operand}")
                    self.C = self.A // np.power(2, self.combo_operand(operand))
                    self.ip += 2

        if self.p:
            print(f"done {self.A} {self.B} {self.C} {self.ip} {self.program}")
        return self.output

def init_computer(Lines):
    A, B, C, _, program = Lines
    A = A[0]
    B = B[0]
    C = C[0]
    return [A, B, C, program]

def forward_calculate(A: int)-> int:
    C = A//(np.power(2, 7-A%8))
    B = np.bitwise_xor(A%8, C)
    return B % 8

def reverse_test(prev, target_out) -> [int]:
    correct = []
    for i in range(8):
        base = prev*8+i
        if forward_calculate(base) == target_out:
            correct.append(base)
    return correct

def part1(Lines):
    inputs = init_computer(Lines)

    computer = Computer(*inputs)
    answer = computer.run()
    answer = ",".join(map(str, answer))
    print(answer)
    return answer

def find_correct_A(base, prog):
    if not prog:
        return [base] # bingo
    options = reverse_test(base, prog[0])
    if not options:
        return [False] # dead end
    poss = []
    for option in options:
        res = [r for r in find_correct_A(option, prog[1:]) if r]
        poss += res
    return poss # collect results


def part2(Lines):
    inputs = init_computer(Lines)
    program = inputs[3][::-1]

    reverse_A = find_correct_A(program[0], program)

    print(min(reverse_A))
    return min(reverse_A)


if __name__ == '__main__':
    #test(read_day(17, 1, regex=r'\d+', cast=int), part1, "4,6,3,5,6,3,5,2,1,0")
    #test(read_day(17, regex=r'\d+', cast=int), part1, "2,0,4,2,7,0,1,0,3")
    #test(read_day(17, 2, regex=r'\d+', cast=int), part2, 117440)
    test(read_day(17, regex=r'\d+', cast=int), part2, 265601188299675)