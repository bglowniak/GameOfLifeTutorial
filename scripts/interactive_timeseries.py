''' Create an interactive timeseries to view change over time '''

import matplotlib.pyplot as plt
import matplotlib.colors as colors

from conway_basic import init_world, timeseries

# mess with parameters here:
WORLD_SIZE = 64
CLUSTER_SIZE = 10
CLUSTERS = 20
TIMESTEPS = 100
# end parameters

world = init_world(n = WORLD_SIZE, cluster_n = CLUSTER_SIZE, clusters = CLUSTERS)
series = timeseries(world, TIMESTEPS)

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