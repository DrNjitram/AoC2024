import itertools
import networkx as nx
from util import *

def parts(lines):
    G = nx.Graph()
    G.add_edges_from(lines)

    counted_cycles = set()
    cliques = list(nx.find_cliques(G))
    for clique in cliques:
        if len(clique) >= 3 and any([c.startswith('t') for c in clique]):
                for c in itertools.combinations(clique, 3):
                    if any([c_.startswith('t') for c_ in c]) and (tc := tuple(sorted(c))) not in counted_cycles:
                            counted_cycles.add(tc)

    p1 = len(counted_cycles)
    p2 = ",".join(sorted(max(cliques, key=len)))
    print(p1, p2)
    return p1, p2

if __name__ == '__main__':
    test(read_day(23, 1, delim="-"), parts, (7, "co,de,ka,ta"))
    test(read_day(23, delim="-"), parts, (1043, "ai,bk,dc,dx,fo,gx,hk,kd,os,uz,xn,yk,zs"))