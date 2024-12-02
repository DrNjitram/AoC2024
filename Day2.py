import numpy as np

from util import read_lines

def safety(report):
    grad = np.ediff1d(report)
    return np.all(np.abs(grad)>0) and np.all(np.abs(grad)<4) and (np.all(grad<0) or np.all(grad>0))

answer = 0
answer2 = 0
for report in read_lines("Inputs/Day2", split=True, cast=int):
    safe = safety(report)
    answer += safe
    answer2 += safe
    if not safe:
        for i in range(len(report)):
            rep2 = report[:]
            rep2.pop(i)
            if safety(rep2):
                answer2+=1
                break

print(answer)
print(answer2)

