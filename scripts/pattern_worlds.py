import numpy as np
ALIVE = 1

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

def init_pulsar_world():
    world = np.zeros((17, 17), dtype=int)
    world[2,4] = world[2,5] = world[2,6] = world[2,10] = world[2,11] = world[2,12] = ALIVE
    world[7,4] = world[7,5] = world[7,6] = world[7,10] = world[7,11] = world[7,12] = ALIVE
    world[9,4] = world[9,5] = world[9,6] = world[9,10] = world[9,11] = world[9,12] = ALIVE
    world[14,4] = world[14,5] = world[14,6] = world[14,10] = world[14,11] = world[14,12] = ALIVE

    world[4,2] = world[5,2] = world[6,2] = world[10,2] = world[11,2] = world[12,2] = ALIVE
    world[4,7] = world[5,7] = world[6,7] = world[10,7] = world[11,7] = world[12,7] = ALIVE
    world[4,9] = world[5,9] = world[6,9] = world[10,9] = world[11,9] = world[12,9] = ALIVE
    world[4,14] = world[5,14] = world[6,14] = world[10,14] = world[11,14] = world[12,14] = ALIVE

    return world

def init_glider_world():
    world = np.zeros((10, 10), dtype=int)
    # hardcode glider pattern
    world[9,1] = world[8,2] = world[7,0] = world[7,1] = world[7,2] = ALIVE
    return world

def init_glider_gun():
    world = np.zeros((20, 40), dtype=int)
    world[14, 1] = world[14, 2] = world[13, 1] = world[13, 2] = ALIVE
    world[16, 36] = world[16, 35] = world[15, 36] = world[15, 35] = ALIVE

    world[14, 11] = world[13, 11] = world[12, 11] = world[15, 12] = world[11, 12] = ALIVE
    world[10, 13] = world[10, 14] = world[16, 13] = world[16, 14] = world[13, 15] = ALIVE
    world[15, 16] = world[14, 17] = world[13, 17] = world[13, 18] = world[12, 17] = world[11, 16] = ALIVE

    world[14, 21] = world[14, 22] = world[15, 21] = world[15, 22] = world[16, 21] = world[16, 22] = ALIVE
    world[17, 23] = world[17, 25] = world[18, 25] = world[13, 23] = world[13, 25] = world[12, 25] = ALIVE


    return world


