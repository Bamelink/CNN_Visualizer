import numpy as np

LEFT_VERTICAL_LINE_KERNEL = np.array([
    [-1,0,1],
    [-1,0,1],
    [-1,0,1]
])

RIGHT_VERTICAL_LINE_KERNEL = np.array([
    [1,0,-1],
    [1,0,-1],
    [1,0,-1],
])

HORIZONTAL_LINE_KERNEL = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
])

EDGE_KERNEL = np.array([
    [-1,0,1],
    [1,-1,0],
    [0,1,-1]
])

TEST_KERNEL1 = np.array([
    [0,1,0],
    [1,0,1],
    [0,1,0]
])