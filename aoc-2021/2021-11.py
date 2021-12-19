import numpy as np

from utils import read_grid, adjacent_idxs

initial_levels = read_grid('aoc-2021/day11.txt', dtype=int)

def step(levels):
    levels += 1
    can_flash = np.ones_like(levels)
    flash_count = 0

    while (flashers := np.logical_and(levels > 9, can_flash)).sum() > 0:
        flashers_idx = np.nonzero(flashers)
        # be careful - repeated indexing of one element does not stack sums
        can_flash[flashers_idx] = 0
        flash_count += flashers.sum()
        for y, x in zip(*flashers_idx):
            pt = np.array([y, x])
            adj_pts = adjacent_idxs(levels, pt, include_diagonals=True)
            
            levels[tuple(adj_pts)] += 1
    levels *= (levels <= 9)
    return levels, flash_count

def run():
    levels = initial_levels
    total_flash_count = 0
    for i in range(1000):
        levels, flash_count = step(levels)
        total_flash_count += flash_count

        if i == 99:
            print('Flash at step 100', total_flash_count)
        if levels.sum() == 0:
            print('Sync at', i + 1)
            return

run()