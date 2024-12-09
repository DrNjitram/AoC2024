from util import *

def parse_disk(Line):
    disk_map = [int(i) for i in Line]
    file = True
    empty_index = []
    file_index = []
    disk_len = 0
    for i in range(len(disk_map)):
        if file:
            file_index.append((disk_len, disk_map[i], i//2))
            file = False
        else:
            empty_index.append((disk_len, disk_map[i]))
            file = True
        disk_len += disk_map[i]
    return file_index, empty_index

def fix_disk(Line):
    file_index, empty_index = parse_disk(Line)
    moved_files = []
    while empty_index:
        empty_pos, empty_length = empty_index.pop(0)
        file_pos, file_length, file_id = file_index.pop()
        if file_length > empty_length:
            moved_files.append((empty_pos, empty_length, file_id))
            file_index.append((file_pos, file_length - empty_length, file_id))
        elif file_length < empty_length:
            moved_files.append((empty_pos, file_length, file_id))
            empty_index.insert(0, (empty_pos + file_length, empty_length - file_length))
        else:
            moved_files.append((empty_pos, file_length, file_id))

        final_index = file_index[-1][0]+file_index[-1][1]
        if empty_index and empty_index[-1][0] >= final_index:
            empty_index.pop()


    return file_index, moved_files

def fix_disk2(Line):
    file_index, empty_index = parse_disk(Line)
    moved_files = []
    unmovable_files = []
    num_files = len(file_index)
    for i in range(num_files):
        moved = False
        file_pos, file_length, file_id = file_index[num_files-i-1]
        for i, (empty_pos, empty_length) in enumerate(empty_index):
            if empty_pos > file_pos:
                continue
            if file_length <= empty_length:
                moved_files.append((empty_pos, file_length, file_id))
                if empty_length > file_length:
                    empty_index[i] = (empty_pos + file_length, empty_length - file_length)
                elif empty_length == file_length:
                    empty_index.pop(i)
                moved = True
                break
        file_index.pop()
        if not moved:
            unmovable_files.append((file_pos, file_length, file_id))

    return file_index, moved_files, unmovable_files

def get_sum_range(a,b):
    return ((b-a)*((b+a)+1))//2

def get_score(data):
    return sum(get_sum_range(file_pos-1, file_pos + file_length-1) * file_id for file_pos, file_length, file_id in data)

def part1(Lines):
    file_index, moved_files = fix_disk(Lines[0])
    answer = get_score(file_index + moved_files)

    print(answer)
    return answer


def part2(Lines):
    file_index, moved_files, unmoved_files = fix_disk2(Lines[0])
    answer = get_score(file_index + moved_files+unmoved_files)

    print(answer)
    return answer

if __name__ == "__main__":
    test(read_day(9, 2), part1, 60)
    test(read_day(9, 1), part1, 1928)
    test(read_day(9, 1), part2, 2858)
    test(read_day(9), part1, 6279058075753)
    test(read_day(9), part2, 6301361958738)

