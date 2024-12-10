import networkx as nx
from util import *
import matplotlib.pyplot as plt


adj = [(0, 1), (1, 0)]
def part1(Lines):
    data = [[int(c) for c in i] for i in Lines]
    start_nodes = []
    end_nodes = []
    labeldict = {}
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            labeldict[(x, y)] = c
            match c:
                case 0:
                    start_nodes.append((x, y))
                case 9:
                    end_nodes.append((x,y))
            for dx, dy in adj:
                if inbounds(data, x+dx, y+dy) and abs(data[y+dy][x+dx] - c)==1:
                    if c < data[y+dy][x+dx]:
                        G.add_edge((x,y), (x+dx, y+dy))
                    else:
                        G.add_edge((x + dx, y + dy), (x, y))

    answer = 0
    answer2 = 0
    for node in start_nodes:
        paths = nx.all_simple_paths(G, node, end_nodes)
        found_end_node = set()
        for path in paths:
            if path[-1] not in found_end_node:
                answer += 1
                found_end_node.add(path[-1])
            else: answer2 += 1

    #nx.draw(G, with_labels=True, font_weight='bold', labels=labeldict)
    #plt.show()
    print(answer)
    print(answer + answer2)
    return answer, answer2+answer


if __name__ == '__main__':
    test(read_day(10, 1), part1, 1)
    test(read_day(10, 2), part1, (36, 81))
    part1(read_day(10))