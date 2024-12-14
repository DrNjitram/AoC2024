import numpy as np
from matplotlib import pyplot as plt


def is_int(x):
    return np.mod(x+0.0001, 1) < 0.001

def print_garden(edges, plot):
    xy, uv = zip(*edges)
    plt.scatter(*zip(*plot))
    plt.quiver(*zip(*xy), *zip(*uv), scale_units="xy", scale=1)
    plt.title(f"{len(edges)}, {len(plot)},{len(plot) * len(edges)}")
    plt.show()