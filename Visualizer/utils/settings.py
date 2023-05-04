import numpy as np

LEFT_VERTICAL_LINE_KERNEL = np.array([
    [-1,1]
])

RIGHT_VERTICAL_LINE_KERNEL = np.array([
    [1,-1]
])

TOP_HORIZONTAL_LINE_KERNEL = np.array([
    [-1],
    [1]
])

BOTTOM_HORIZONTAL_LINE_KERNEL = np.array([
    [1],
    [-1]
])

EDGE_KERNEL = np.array([
    [-1,0,1],
    [1,-1,0],
    [0,1,-1]
])

TEST_KERNEL1 = np.array([
    [-1,-2,-1],
    [2,1,2],
    [-1,-2,-1]
])