import numpy as np

def init_fixed_world():
    world = np.zeros((10, 10), dtype=int)
    world[7,1] = world[7,2] = world[8,1] = world[8,2] = ALIVE
    world[7,5] = world[8,6] = world[8,7] = world[7,8] = world[6,7] = world[6,6] = ALIVE
    world[3,2] = world[2,3] = world[2,1] = world[1,2] = ALIVE
    world[3,6] = world[3,7] = world[2,6] = world[2,8] = world[1,7] = ALIVE

    return world

def init_oscillator_world():
    world = np.zeros((11, 11), dtype=int)

    world[8,1] = world[8,2] = world[8,3] = ALIVE

    world[8,6] = world[9,6] = world[9,7] = ALIVE
    world[6,8] = world[6,9] = world[7,9] = ALIVE

    world[2,3] = world[2,4] = world[2,5] = ALIVE
    world[3,4] = world[3,5] = world[3,6] = ALIVE

    return world

def init_glider_world():
    world = np.zeros((10, 10), dtype=int)
    # hardcode glider pattern
    world[9,1] = world[8,2] = world[7,0] = world[7,1] = world[7,2] = ALIVE
    return world