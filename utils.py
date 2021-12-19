"""Utility functions used across challenges"""
import numpy as np
import os
from pathlib import Path

# File reading
def read_grid(fname, **kwargs):
    """Read an input file with characters"""
    with open(fname, 'r') as f:
        return np.array([[c for c in line.strip()] for line in f.readlines()], **kwargs)


# Array handling
DIRS = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
])

DIRS_DIAGS = np.array([
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
])
def adjacent_idxs(grid, idx, include_diagonals=False):
    """Return the indexes of the adjecent elements (in bounds)"""
    dir_vectors = DIRS_DIAGS if include_diagonals else DIRS
    pts = dir_vectors + idx
    bounds_y = np.logical_and(0 <= pts[:, 0], pts[:, 0] < grid.shape[0])
    bounds_x = np.logical_and(0 <= pts[:, 1], pts[:, 1] < grid.shape[1])
    in_bounds = pts[np.logical_and(bounds_x, bounds_y)]
    return (in_bounds[:, 0], in_bounds[:, 1])