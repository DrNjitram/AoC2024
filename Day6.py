from util import *

def run_route(internal_data: dict, guard: Tuple[complex, complex], edit=False) -> set:
    guard_p, guard_d = guard
    visited = {guard_p}
    while True:
        coord = cast_ray(internal_data, (guard_p, guard_d))
        if coord is None:
            while True:
                guard_p += guard_d
                if not inbounds_c(internal_data, guard_p):
                    break
                visited.add(guard_p)
                if edit:
                    internal_data[guard_p] = 2
            break
        else:
            for i in range(int(coord.real)-1):
                guard_p += guard_d
                visited.add(guard_p)
                if edit:
                    internal_data[guard_p] = 2
            guard_d *= 1j
            #print_sparse_map(internal_data, keys, unique=((guard_p, guard_d), None))

        #print_sparse_map(data, keys, unique=((guard_p, guard_d), None))

    return visited

def find_loop(internal_data: dict, guard: Tuple[complex, complex]) -> bool:
    guard_p, guard_d = guard
    visited = {guard}
    while True:
        coord = cast_ray(internal_data, (guard_p, guard_d))
        if coord is None:
            return False
        else:
            for i in range(int(coord.real) - 1):
                guard_p += guard_d
                if (guard_p, guard_d) in visited:
                    return True
                visited.add((guard_p, guard_d))

                #data[guard_p] = 2

            guard_d *= 1j

        #print_sparse_map(data, keys, unique=((guard_p, guard_d), None))


def part1_and_2(Lines):
    data, guard = sparse_map(Lines, keys, unique="^", direction=complex(0, -1))
    visited = run_route(data, guard)
    print(len(visited))
    answer = 0
    for p in visited:

        print(p)

        if p != guard[0]:
            new_data = data.copy()
            new_data[p] = 1

            result = find_loop(new_data, guard)
            answer +=  result


    print(answer)
    return len(visited), answer

def part1(Lines):
    data, guard = sparse_map(Lines, keys, unique="^", direction=complex(0, -1))
    #print_sparse_map(data, keys, unique=(guard, "^"))

    visited = run_route(data, guard)

    print(len(visited))
    return len(visited)


keys = defaultdict(int, {"#": 1, "X": 2})
test(read_day(6, 1), part1_and_2, (41, 6))
part1_and_2(read_day(6, 0))