import itertools
from util import *

def parts(lines):
    keys = []
    locks = []
    for i in range(0, len(lines), 8):
        item = [l.count("#")-1 for l in zip(*lines[i:i+7])]
        if lines[i].startswith("#"):
            locks.append(item)
        else:
            keys.append(item)
    fits = 0
    for k,l in itertools.product(locks, keys):
        if all([a+b<6 for a,b in zip(k,l)]):
            fits += 1
    print(fits)
    return fits

if __name__ == '__main__':
    test(read_day(25, 1), parts, 3)
    test(read_day(25), parts, 3077)