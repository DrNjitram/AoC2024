from util import *
import networkx as nx
from tqdm import tqdm

def parts(lines, limit=100, cheat=20):
    E = S = None
    G = nx.grid_2d_graph(len(lines[0]), len(lines))

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            c = lines[y][x]
            match c:
                case "E":
                    E = (x,y)
                case "S":
                    S = (x,y)
                case "#":
                    G.remove_node((x, y))

    base_path = nx.shortest_path(G, S, E)
    base_distance = {k: i for i, k in enumerate(base_path)}

    offsets = []

    for dx in range(-cheat, cheat + 1):
        for dy in range(-cheat, cheat + 1):
            if 0 < abs(dx) + abs(dy) <= cheat:
                offsets.append((dx,dy))


    nodes = set(G.nodes())

    counter = defaultdict(int)

    for x,y in tqdm(base_path):
        d = base_distance[(x,y)]
        for dx, dy in offsets:
            p = (x+dx, y+dy)
            if p in nodes:
                savings = base_distance[p]-d-(abs(dx) + abs(dy))
                if savings >= limit:
                    counter[savings] += 1

    answer = sum(counter.values())
    print(answer)
    return answer

if __name__ == '__main__':
    test(read_day(20, 1), parts, 44, limit=2, cheat=2)
    test(read_day(20, 1), parts, 285, limit=50, cheat=20)
    test(read_day(20), parts, 1296, limit=100, cheat=2)
    test(read_day(20), parts, 977665, limit=100, cheat=20)
