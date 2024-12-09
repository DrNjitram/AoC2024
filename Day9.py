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

def print_disk(all_data):
    all_data.sort(key=lambda a: a[0])
    disk_string = ""
    last_idx = 0
    for entry in all_data:
        if len(entry)>2:
            pos, length, file_id = entry
            if last_idx != pos:
                disk_string += "."*(pos - last_idx)
            disk_string += str(file_id)*length
            last_idx = pos+length
        else:
            _, length = entry
            disk_string += "."*length
    print(disk_string)

def fix_disk2(Line):
    file_index, empty_index = parse_disk(Line)
    gaps = [[], [], [], [], [], [], [], [], []]
    moved_files = []
    unmovable_files = []
    for empty_pos, empty_length in empty_index:
        if empty_length:
            gaps[empty_length-1].append(empty_pos)

    for idx, (file_pos, file_length, file_id) in enumerate(file_index[::-1]):
        options = [(i, g[0]) for i, g in enumerate(gaps[file_length-1:]) if g and g[0] < file_pos]
        if options:
            empty_length, empty_pos = min(options, key=lambda p: p[1])
            gaps[file_length+empty_length-1].pop(0)
            if empty_length:
                gaps[empty_length-1].insert(0, empty_pos+file_length)
                gaps[empty_length-1].sort()
            moved_files.append((empty_pos, file_length, file_id))
        else:
            unmovable_files.append((file_pos, file_length, file_id))

    return moved_files, unmovable_files


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
    moved_files, unmoved_files = fix_disk2(Lines[0])
    answer = get_score(moved_files+unmoved_files)

    print(answer)
    return answer

if __name__ == "__main__":
    #test(read_day(9, 2), part1, 60)
    #test(read_day(9, 1), part1, 1928)
    test(read_day(9, 1), part2, 2858)
    test(read_day(9), part1, 6279058075753)
    test(read_day(9), part2, 6301361958738)

