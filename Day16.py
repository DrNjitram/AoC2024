from util import *
import networkx as nx

def part1_and_2(Lines):
    G = nx.Graph()
    S = E = None
    pos = {}
    for y in range(1, len(Lines)-1):
        for x in range(1, len(Lines[y])-1):
            if Lines[y][x] != '#':
                pos[(x,y,0)] = (x,-y)
                pos[(x,y,1)] = (x,-y)
                if Lines[y][x] == 'S':
                    S = (x,y, 0)
                    G.add_edge((x, y, 0), (x, y, 1), weight=1000)
                elif Lines[y][x] == 'E':
                    E = (x,y, 0)
                    G.add_edge((x, y, 0), (x, y, 1), weight=0)
                A = B = False
                for dx, dy in [(-1, 0), (1, 0)]:
                    if Lines[y+dy][x+dx] != '#':
                        A = True
                        G.add_edge((x,y,0), (x+dx, y+dy, 0), weight=1)
                for dx, dy in [(0, -1), (0, 1)]:
                    if Lines[y+dy][x+dx] != '#':
                        B = True
                        G.add_edge((x,y,1), (x+dx, y+dy, 1), weight=1)
                if A and B and Lines[y][x] != 'E':
                    G.add_edge((x,y,0), (x,y,1), weight=1000)
    path = nx.shortest_path(G, S, E, weight='weight')
    weight = nx.path_weight(G, path, weight='weight')

    seats = set()
    for path in nx.all_shortest_paths(G, S, E, weight='weight'):
            seats |= set([(p[0], p[1]) for p in path])
    print(weight, len(seats))
    return weight, len(seats)


if __name__ == '__main__':
    test(read_day(16, 1), part1_and_2, (7036, 45))
    test(read_day(16, 2), part1_and_2, (11048, 64))
    test(read_day(16), part1_and_2, (99488, 516))
