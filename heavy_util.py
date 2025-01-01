import math

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def draw_path(G, path, pos=None):
    nx.draw(G, pos=pos, node_size=1)
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(path, path[1:])), edge_color='r', width=5)
    plt.show()

def is_int(x):
    return np.mod(x+0.0001, 1) < 0.001

def print_garden(edges, plot):
    xy, uv = zip(*edges)
    plt.scatter(*zip(*plot))
    plt.quiver(*zip(*xy), *zip(*uv), scale_units="xy", scale=1)
    plt.title(f"{len(edges)}, {len(plot)},{len(plot) * len(edges)}")
    plt.show()

