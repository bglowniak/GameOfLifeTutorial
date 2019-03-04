''' Exploration of patterns in Game of Life '''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from conway_basic import timeseries, plot_world
from pattern_worlds import init_fixed_world, init_oscillator_world, init_glider_world

ALIVE = 1
DEAD = 0
cmap = colors.ListedColormap(['white', 'red'])

def plot_fixed_series():
    world = init_fixed_world()
    series = timeseries(world, 8)

    for i in range(0, 3):
        plt.subplot(1, 3, i + 1)
        plt.pcolor(series[i * 3], cmap=cmap, edgecolor="black")
        plt.axis('square')
        plt.title("t = " + str(i * 3))

    plt.show()

def plot_oscillator_series():
    world = init_oscillator_world()
    series = timeseries(world, 3)

    for i in range(0, 3):
        plt.subplot(1, 3, i + 1)
        plt.pcolor(series[i], cmap=cmap, edgecolor="black")
        plt.axis('square')
        plt.title("t = " + str(i))

    plt.show()

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


