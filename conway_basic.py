import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import random
from itertools import product

ALIVE = 1
DEAD = 0

# Creates an n x n world with randomly generated clusters of living entities
# n: the size of the world
# cluster_n: the size of each cluster
# clusters: the number of clusters to generate
# threshold: the probability) of a living entity in each coordinate of a cluster
def init_world(n = 16, cluster_n = 4, clusters = 3, threshold = 0.25):
    world = np.zeros((n, n), dtype=int)

    for i in range(0, clusters):
        x = random.randint(0, n - cluster_n)
        y = random.randint(0, n - cluster_n)
        for world_x in range(x, x + cluster_n):
            for world_y in range(y, y + cluster_n):
                if random.uniform(0, 1) >= (1 - threshold):
                    world[world_x, world_y] = ALIVE

    return world

def update_cell(world, x, y):
    num_alive = 0
    current_state = world[x,y]

    #count neighbors
    x_range = range(max(x - 1, 0), min(x + 1, world.shape[0] - 1) + 1)
    y_range = range(max(y - 1, 0), min(y + 1, world.shape[1] - 1) + 1)

    for cell_x, cell_y in product(x_range, y_range):
        if (not (cell_x, cell_y) == (x, y) and world[cell_x, cell_y] == ALIVE):
            num_alive += 1

    if (current_state == DEAD and not num_alive == 3):
        return DEAD
    elif (current_state == ALIVE and (num_alive < 2 or num_alive > 3)):
        return DEAD
    else:
        return ALIVE

def count_alive(world):
    pass

def count_dead(world):
    pass

#brute force implementation for now, need to optimize
def timestep(world):
    rows = world.shape[0]
    cols = world.shape[1]

    new_state = np.zeros((rows, cols), dtype=int)
    for x in range(0, rows):
        for y in range(0, cols):
            new_state[x,y] = update_cell(world, x, y)

    return new_state

#def plot_world(world):
#    cmap = colors.ListedColormap(['white', 'red'])
#    plt.pcolor(world, cmap=cmap, edgecolor="black")
#    plt.axis('square')
#    #plt.show()

def timeseries(world, num_steps):
    simulation_steps = [world]
    for i in range(0, num_steps):
        world = timestep(world)
        simulation_steps.append(world)

    return simulation_steps

world = init_world(n = 64, cluster_n = 5, clusters = 8)
series = timeseries(world, 50)

# allows for scrolling through a timeseries using the left and right arrow keys
def key_event(e):
    global curr_pos

    if e.key == "right" and curr_pos < len(series) - 1:
        curr_pos = curr_pos + 1
    elif e.key == "left" and curr_pos > 0:
        curr_pos = curr_pos - 1
    else:
        return

    ax.cla()
    ax.pcolor(series[curr_pos], cmap=colors.ListedColormap(['white', 'red']), edgecolor='black')
    fig.canvas.draw()

curr_pos = 0
fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', key_event)
ax = fig.add_subplot(111)
ax.pcolor(series[curr_pos], cmap=colors.ListedColormap(['white', 'red']), edgecolor='black')
plt.show()