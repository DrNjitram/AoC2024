import concurrent.futures
from multiprocessing import Pool, freeze_support
from tqdm import tqdm
import threading
from util import *

class Route_finder():
    def __init__(self, data, guard):
        self.data = data
        self.guard = guard

    def run_route(self, edit=False) -> set:
        guard_p, guard_d = self.guard
        visited = {guard_p}
        while True:
            coord = cast_ray(self.data, (guard_p, guard_d))
            if coord is None:
                while True:
                    guard_p += guard_d
                    if not inbounds_c(self.data, guard_p):
                        break
                    visited.add(guard_p)
                    if edit:
                        self.data[guard_p] = 2
                break
            else:
                for i in range(int(coord.real) - 1):
                    guard_p += guard_d
                    visited.add(guard_p)
                    if edit:
                        self.data[guard_p] = 2
                guard_d *= 1j

        return visited

    def modify_and_find_loop(self, modification: complex) -> bool:
        guard_p, guard_d = self.guard
        visited = {self.guard}
        new_data = self.data.copy()
        new_data[modification] = 1
        while True:
            coord = cast_ray(new_data, (guard_p, guard_d))
            if coord is None:
                return False

            guard_p += (coord-1) * guard_d
            if (guard_p, guard_d) in visited:

                return True
            visited.add((guard_p, guard_d))

            guard_d *= 1j



def part1_and_2(Lines):
    data, guard = sparse_map(Lines, keys, unique="^", direction=complex(0, -1))
    route = Route_finder(data, guard)
    visited = route.run_route()
    answer = len(visited)

    if multiprocess:
        with Pool() as pool:
                results = list(
                    tqdm(
                        pool.imap_unordered(
                            route.modify_and_find_loop,
                            visited
                        ),
                    total=len(visited)))
    else:
        with concurrent.futures.ThreadPoolExecutor() as pool:
            results = list(tqdm(pool.map(route.modify_and_find_loop, visited), total=len(visited)))


    answer2 = sum(results)-1
    print(answer, answer2)
    return answer, answer2

if __name__ == '__main__':
    multiprocess = True
    keys = defaultdict(int, {"#": 1, "X": 2})
    test(read_day(6, 1), part1_and_2, (41, 6))
    test(read_day(6, 0), part1_and_2, (4967, 1789))