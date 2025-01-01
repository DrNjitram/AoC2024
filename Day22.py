import numpy as np
from util import *


e24 = 1 << 24

def next_secret(secret: int) -> int:
    secret = (secret ^ (secret << 6)) % e24
    secret = (secret ^ (secret >> 5)) % e24
    secret = (secret ^ (secret << 11)) % e24
    return secret

def get_secret(secret: int):
    secrets = [secret]
    seq_dict = dict()
    for _ in range(2000):
        secrets.append(next_secret(secrets[-1]))

    prices = [s%10 for s in secrets]
    d_prices = [int(i) for i in np.ediff1d(prices)]

    for i in range(0, len(d_prices)-3):
        seq = tuple(d_prices[i:i+4])
        if seq not in seq_dict:
            seq_dict[seq] = prices[i+4]

    return secrets[-1], seq_dict


def parts(lines):
    ans = [get_secret(l) for l in tqdm(lines)]
    p1 = 0
    all_changes = set()
    all_dicts = []
    for s, seq_dict in tqdm(ans):
        p1 += s
        all_dicts.append(seq_dict)
        all_changes |= set(seq_dict.keys())

    p2 = []
    for seq in tqdm(all_changes):
        p2.append(sum([d.get(seq, 0) for d in all_dicts]))

    p2 = max(p2)

    print(p1, p2)
    return p1, p2

if __name__ == '__main__':
    test(read_day(22, 1, cast=int), parts, (37327623, 24))
    test(read_day(22, 2, cast=int), parts, (37990510, 23))
    test(read_day(22, cast=int), parts, (17724064040, 1998))

