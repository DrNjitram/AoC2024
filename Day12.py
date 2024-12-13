from util import *


def get_edge(x,y,dx,dy):
    match (dx, dy):
        case (0, 1): return (x-0.5, y+0.5), (1, 0)
        case (0, -1): return (x+0.5, y-0.5), (-1, 0)
        case (1, 0): return (x+0.5, y+0.5), (0, -1)
        case (-1, 0): return (x-0.5, y-0.5), (0, 1)


def get_perimeter(plot):
    perimeter = 0
    for x, y in plot:
        for dx, dy in adj4:
            if (x+dx, y+dy) not in plot:
                perimeter += 1
    return perimeter


def get_sides(plot):
    edges = []
    for x, y in plot:
        for dx, dy in adj4:
            if (x+dx, y+dy) not in plot:
                edges.append(get_edge(x,y,dx,dy))

    changed = True
    while changed:
        new_edges = set()
        changed = False
        skip = []
        for (x,y), (dx, dy) in edges:
            if ((x,y), (dx, dy)) in skip:
                continue
            found = False
            for (x2,y2), (dx2, dy2) in edges:
                if ((x,y), (dx, dy)) != ((x2,y2), (dx2, dy2)) and ((x2,y2), (dx2, dy2)) not in skip:
                    if x+dx == x2 and y+dy == y2 and (dx2 == dx or dy2 == dy):
                        new_edges.add(((x,y), (dx+dx2, dy+dy2)))
                        if ((x2,y2), (dx2, dy2)) in new_edges:
                            new_edges.remove(((x2,y2), (dx2, dy2)))
                        skip.append(((x2,y2), (dx2, dy2)))
                        skip.append(((x,y), (dx, dy)))
                        changed = True
                        found = True
                        break
            if not found:
                new_edges.add(((x,y), (dx, dy)))
        edges = list(new_edges)

    return len(edges)


def part1(Lines):
    plots = defaultdict(list)

    for y in range(len(Lines)):
        for x in range(len(Lines[y])):
            garden = Lines[y][x]
            plots[garden] += [(x, y)]

    answer = 0
    answer2 = 0
    for garden, plot in plots.items():
        region = []
        for x,y in plot:
            found = False
            for reg in region:
                for dx, dy in adj4:
                    if (x+dx, y+dy) in reg:
                        reg.append((x,y))
                        found = True
                        break
                if found:
                    break
            if not found:
                region += [[(x,y)]]

        changed = True
        while changed:
            changed = False
            new_region = []
            skip = []
            for reg1 in region:
                if reg1 in skip:
                    continue
                found = False
                for reg2 in region:
                    if reg1 != reg2 and reg2 not in skip:
                        for x, y in reg1:
                            for dx, dy in adj4:
                                if (x + dx, y + dy) in reg2:

                                    new_region += [reg1 + reg2]
                                    skip += [reg1, reg2]
                                    found = True
                                    changed = True
                                    break
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
                if not found:
                    new_region += [reg1]
            region = new_region

        sub_ans = 0
        sub_ans2 = 0

        for reg in region:
            sub_ans += len(reg) * get_perimeter(reg)
            sub_ans2 += len(reg) * get_sides(reg)
        answer += sub_ans
        answer2 += sub_ans2

    print(answer, answer2)
    return answer, answer2

if __name__ == "__main__":
    test(read_day(12, 1), part1, (140, 80))
    test(read_day(12, 3), part1, (772, 436))
    test(read_day(12, 2), part1, (1930, 1206))
    test(read_day(12, 5), part1, (692, 236))
    test(read_day(12, 4), part1, (1184, 368))
    test(read_day(12), part1, (1473408, 886364))
