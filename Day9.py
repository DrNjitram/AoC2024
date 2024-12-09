from util import *

def fix_disk(Line):
    disk_map = [int(i) for i in Line]
    i = 0
    file = True
    empty_index = []
    file_index = []
    moved_files = []
    disk_len = 0
    while i < len(disk_map):
        if file:
            file_index.append((disk_len, disk_map[i], i // 2))
            file = False
        else:
            empty_index.append((disk_len, disk_map[i]))
            file = True
        disk_len += disk_map[i]
        i += 1

    print_disk(file_index, moved_files, empty_index)

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
        print_disk(file_index, moved_files, empty_index)
        if empty_length + empty_pos == file_pos:
            break

    return file_index, moved_files

def print_disk(file_index: list, moved_files: list, empty_index: list):
    all_data = file_index+moved_files+empty_index
    all_data.sort(key=lambda a: a[0])
    disk_string = ""
    for entry in all_data:
        if len(entry)>2:
            _, length, file_id = entry
            disk_string += str(file_id)*length
        else:
            _, length = entry
            disk_string += "."*length
    print(disk_string)

def sum_range(n):
    return n * (n + 1) // 2

def get_sum_range(a,b):
    return sum_range(b-1)-sum_range(a-1)

def part1(Lines):

    file_index, moved_files = fix_disk(Lines[0])
    all_data = file_index + moved_files
    all_data.sort(key=lambda a: a[0])
    answer1 = 0
    answer2 = 0
    print(all_data)
    for file_pos, file_length, file_id in all_data:
        buff = 0
        buff2 = 0
        for i in range(file_length):
            # print(file_id*(file_pos+i))
            buff += file_id * (file_pos + i)
            buff2 += (file_pos + i)
        print(file_pos, file_length, file_id, buff2, buff)
        answer2 += buff
        if file_length == 1:
            print(file_pos, file_length, file_id, file_pos, file_id*file_pos)
            answer1 += file_id*file_pos
        else:
            print(file_pos, file_length, file_id, get_sum_range(file_pos, file_pos+file_length),get_sum_range(file_pos, file_pos+file_length)*file_id)
            answer1 += get_sum_range(file_pos, file_pos+file_length)*file_id
    print(answer1)
    print(answer2)







if __name__ == "__main__":
    test(read_day(9, 2), part1, 60)
    test(read_day(9, 1), part1, 1928)
