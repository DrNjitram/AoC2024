from util import *

def get_coin(AB, prize):
    steps = np.linalg.solve(AB, prize)
    if is_int(steps).all():
        steps = np.round(steps).astype(int)
        return steps[0] * 3 + steps[1]
    return 0

def part1_and_2(Lines):
    coins = 0
    coins2 = 0
    for i in range(0, len(Lines), 3):
        A, B, prize = Lines[i:i+3]

        coins += get_coin(np.array([A, B]).T, np.array(prize))
        coins2 += get_coin(np.array([A, B]).T, np.array(prize) + 10000000000000)

    print(coins, coins2)
    return coins, coins2


if __name__ == '__main__':
    test(read_day(13, 1, regex = r'\d+', cast=int), part1_and_2, (480, 875318608908))
    test(read_day(13, regex=r'\d+', cast=int), part1_and_2, (29388, 99548032866004))