''' Exploration of patterns in Game of Life '''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from conway_basic import timeseries, plot_world

ALIVE = 1
DEAD = 0
cmap = colors.ListedColormap(['white', 'red'])

def init_fixed_world():
    world = np.zeros((10, 10), dtype=int)
    # block
    world[7,1] = world[7,2] = world[8,1] = world[8,2] = ALIVE

    # beehive
    world[7,5] = world[8,6] = world[8,7] = world[7,8] = world[6,7] = world[6,6] = ALIVE

    # tub
    world[3,2] = world[2,3] = world[2,1] = world[1,2] = ALIVE

    # boat
    world[3,6] = world[3,7] = world[2,6] = world[2,8] = world[1,7] = ALIVE

    return world

def plot_fixed_series():
    world = init_fixed_world()
    series = timeseries(world, 8)

    for i in range(0, 3):
        plt.subplot(1, 3, i + 1)
        plt.pcolor(series[i * 3], cmap=cmap, edgecolor="black")
        plt.axis('square')
        plt.title("t = " + str(i * 3))

    plt.show()


def init_glider_world():
    world = np.zeros((10, 10), dtype=int)
    # hardcode glider pattern
    world[9,1] = ALIVE
    world[8,2] = ALIVE
    world[7,0] = ALIVE
    world[7,1] = ALIVE
    world[7,2] = ALIVE
    return world

def plot_glider_series():
    world = init_glider_world()
    series = timeseries(world, 30)

    for i in range(0, 4):
        plt.subplot(2, 4, i + 1)
        plt.pcolor(series[i], cmap=cmap, edgecolor="black")
        plt.axis('square')
        plt.title("t = " + str(i))

        plt.subplot(2, 4, i + 5)
        plt.pcolor(series[(i + 1) * 5], cmap=cmap, edgecolor = "black")
        plt.axis('square')
        plt.title("t = " + str((i + 1) * 5))

    plt.show()


plot_fixed_series()


