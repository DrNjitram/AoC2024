import re

line = open("Inputs/Day3").read().strip()

matches =  re.findall(r"(mul\(-?[0-9]+,-?[0-9]+\)|do\(\)|don't\(\))", line)
print(line)
print(matches)
enable = True
mul_result = 0
for match in matches:
    if match == "do()":
        enable = True
    elif match == "don't()":
        enable = False
    elif enable:
        a,b = [int(i) for i in match[4:-1].split(",")]
        mul_result += a*b

print(mul_result)