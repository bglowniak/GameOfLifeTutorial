''' Exploration of patterns in Game of Life '''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from conway_basic import timeseries, plot_world
from pattern_worlds import init_fixed_world, init_oscillator_world, init_glider_world, init_pulsar_world, init_glider_gun

cmap = colors.ListedColormap(['white', 'red'])

def plot_series(world, steps):
    series = timeseries(world, steps)

    fig, ax = plt.subplots(1, steps)

    for i in range(0, steps):
        ax[i].pcolor(series[i], cmap=cmap, edgecolor="black")
        ax[i].axis('square')
        if not i == 0:
            ax[i].yaxis.set_visible(False)
        ax[i].set_title("t = " + str(i))

    plt.show()

def plot_glider_series():
    world = init_glider_world()
    series = timeseries(world, 25)

    fig, ax = plt.subplots(2, 4)

    for i in range(0, 4):
        ax[0, i].pcolor(series[i], cmap=cmap, edgecolor="black")
        ax[0, i].axis('square')
        ax[0, i].set_title("t = " + str(i))

        ax[1, i].pcolor(series[(i + 1) * 5], cmap=cmap, edgecolor="black")
        ax[1, i].axis('square')
        ax[1, i].set_title("t = " + str((i + 1) * 5))

        if not i == 0:
            ax[0, i].yaxis.set_visible(False)
            ax[1, i].yaxis.set_visible(False)

    plt.show()

def plot_gun_series():
    world = init_glider_gun()
    series = timeseries(world, 100)

    fig, ax = plt.subplots(2, 2)

    for i in range(0, 2):
        for j in range(0, 2):
            ax[i, j].pcolor(series[(i + j) * 25], cmap=cmap, edgecolor="black")
            ax[i, j].set_title("t = " + str((i + j) * 25))

            if not j == 0:
                ax[i, j].yaxis.set_visible(False)

    plt.show()