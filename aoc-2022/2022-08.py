# cython -a day11.pyx

import numpy as np
import cython

import pyximport
pyximport.install(setup_args=dict(include_dirs=[np.get_include()]), language_level=3)
import day08 #type: ignore

with open("day08.txt") as f:
    grid_lst = [[*l.strip()] for l in f.readlines()]
    grid = np.array(grid_lst, dtype=int)

pad = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2)) - 1
pad[1:-1, 1:-1] = grid

left = np.maximum.accumulate(pad[1:-1, :-2], axis=1)
right = np.maximum.accumulate(pad[1:-1, :1:-1], axis=1)[:, ::-1]

top = np.maximum.accumulate(pad[:-2, 1:-1], axis=0)
bot = np.maximum.accumulate(pad[:1:-1, 1:-1], axis=0)[::-1, :]

visible = (grid > left) | (grid > right) | (grid > top) | (grid > bot)
print(visible.sum())

scores = day08.best_view(grid)
print(scores.max())