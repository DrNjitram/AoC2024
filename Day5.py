from collections import defaultdict

from util import *

def is_valid(pages, rules):
    for idx, page in enumerate(pages[:-1]):
        rule = rules[page]
        if not (rule and set(pages[idx + 1:]).issubset(rule)):
            return False
    return True

def make_valid(pages, rules) -> list:
    new_pages = [pages[0]]
    for page in pages[1:]:
        for idx in range(len(new_pages)+1):
            test = new_pages[:]
            test.insert(idx, page)
            if is_valid(test, rules):
                new_pages = test
                break
    return new_pages

def part1_and2(lines):
    i = 0
    rules = defaultdict(set)
    while lines[i] != "":
        before, after = map(int, lines[i].split("|"))
        rules[before].add(after)
        i += 1
    i+= 1

    answer = 0
    answer2 = 0
    while i < len(lines):
        pages = list(map(int, lines[i].split(",")))
        valid = is_valid(pages, rules)
        if valid:
            answer += pages[len(pages)//2]

        else:
            pages = make_valid(pages, rules)
            answer2 += pages[len(pages)//2]
        i += 1
    print(answer, answer2)
    return answer, answer2

test(read_day(5, 1), part1_and2, (143, 123))
part1_and2(read_day(5, 0))