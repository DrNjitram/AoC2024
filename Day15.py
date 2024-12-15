from util import *

keys = {
    '#': 1,
    'O': 2,
    '[': 3,
    ']': 4
}

def expanded_map(data):
    new_data = defaultdict(complex)
    for k,v in data.items():
        new_data[k.real*2+ k.imag*1j] = 3 if v == 2 else 1
        new_data[k.real*2+1+ k.imag*1j] = 4 if v == 2 else 1
    return new_data

def step_move(data, next_pos, move):
    move_list = [(next_pos, 0)]

    p_central = next_pos + inv_direction_dict[move]
    if data[next_pos] == 0.0:
        return []
    to_check = [p_central]

    if data[next_pos] == 3:
        p = next_pos + 1 + inv_direction_dict[move]
        if data[p] != 0.0:
            to_check.append(p)
        move_list += [(next_pos+1, 0), (p_central, 3), (p, 4)]
    elif data[next_pos] == 4:
        p = next_pos - 1 + inv_direction_dict[move]
        if data[p] != 0.0:
            to_check.append(p)
        move_list += [(next_pos-1, 0), (p_central, 4), (p, 3)]

    elems = [data[p] for p in to_check]
    if 1 in elems:
        return [None]
    elif elems.count(0.0) == len(elems):  # all dots, lets move
        return move_list
    else:
        return move_list + sum([step_move(data, p, move) for p in to_check], [])


def pushing_boxes(data, robot, move):
    next_pos = robot + inv_direction_dict[move]
    check_pos = next_pos
    while True:
        check_pos += inv_direction_dict[move]
        match data[check_pos]:
            case 0:
                if data[next_pos] == 2:
                    robot = next_pos
                    data[next_pos] = 0
                    data[check_pos] = 2
                else: # expanded map
                    if move in [">", "<"]:
                        robot = next_pos
                        data[next_pos] = 0
                        while next_pos != check_pos:
                            match move:
                                case "<":
                                    data[next_pos+inv_direction_dict[move]] = 4
                                    data[next_pos+2*inv_direction_dict[move]] = 3
                                case ">":
                                    data[next_pos + inv_direction_dict[move]] = 3
                                    data[next_pos + 2 * inv_direction_dict[move]] = 4
                            next_pos += 2*inv_direction_dict[move]
                    else:
                        move_list = step_move(data, next_pos, move)
                        if None not in move_list:
                            robot = next_pos
                            filtered_list = []
                            for p,v in move_list:
                                if v == 0:
                                    for p2,v2 in move_list:
                                        if p2 == p and v2 != 0:
                                            break
                                    else:
                                        filtered_list.append((p,v))
                                else:
                                    filtered_list.append((p,v))

                            for p, v in filtered_list[::-1]:
                                data[p] = v
                return data, robot
            case 1:
                return data, robot


def get_score(data):
    answer = 0
    for k, v in data.items():
        if v in [2, 3]:
            answer += int(k.imag*100+k.real)
    return answer

def step_state(data, robot, move):
    next_pos = robot+ inv_direction_dict[move]

    match data[next_pos]:
        case 0:
            robot = next_pos
        case 2 | 3 | 4:
            data, robot = pushing_boxes(data, robot, move)
    return data, robot

def parts(Lines: List[str], part2=False):
    data = Lines[:Lines.index('')]
    moves = "".join(Lines[Lines.index('')+1:])
    data, robot = sparse_map(data, keys, unique="@")
    if part2:
        robot = robot.real * 2 + robot.imag * 1j
        data = expanded_map(data)

    for move in moves:
        data, robot = step_state(data, robot, move)

    answer = get_score(data)
    print(answer)
    return answer

if __name__ == '__main__':
    test(read_day(15, 2), parts, 2028)
    test(read_day(15, 1), parts, 10092)
    test(read_day(15, 1), parts, 9021, part2=True)
    test(read_day(15), parts, 1414416)
    test(read_day(15), parts, 1386070, part2=True)