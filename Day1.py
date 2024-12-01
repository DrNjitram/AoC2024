from util import read_lines

l1 = []
l2 = []

for line in read_lines("Inputs/Day1"):
    a, b = [int(i) for i in line.split()]
    l1.append(a)
    l2.append(b)

l1.sort()
l2.sort()

answer = 0
answer2 = 0
for a,b in zip(l1, l2):
    answer2 += a*l2.count(a)
    answer += abs(a-b)

print(answer)
print(answer2)