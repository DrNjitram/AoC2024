from networkx.exception import NetworkXNoPath
import networkx as nx
from util import *

def parts(Lines, size = 70, limit=1024):
    G = nx.grid_2d_graph(size+1, size+1)

    for x,y in Lines[:limit]:
        G.remove_node((x, y))

    S = (0,0)
    E = (size, size)
    path = nx.shortest_path(G, S, E)
    answer1 = len(path)-1
    for x,y in Lines[limit:]:
        G.remove_node((x, y))
        if (x,y) in path:
            try:
                path = nx.shortest_path(G, S, E)
            except NetworkXNoPath:
                break

    print(f"{answer1}, {x},{y}")
    return answer1, (x, y)

if __name__ == '__main__':
    test(read_day(18, 1, split=True, delim=",", cast=int), parts, (22, (6,1)), size=6, limit=12)
    test(read_day(18, split=True, delim=",", cast=int), parts, (348, (54,44)))