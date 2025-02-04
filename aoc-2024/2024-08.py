from string import ascii_letters, digits
import numpy as np
from itertools import combinations

char_map = "." + ascii_letters + digits


with open("day08.txt") as f:
    grid = np.array(
        [[char_map.index(c) for c in line.strip()] for line in f.readlines()]
    )
symbols = np.unique(grid)


def in_bounds(p: tuple):
    y, x = p
    h, w = grid.shape
    return 0 <= x < w and 0 <= y < h

def get_all_aligned_points(a: np.ndarray, v: np.ndarray):
    pts = []
    p = a
    while True:
        pts.append(tuple(p))
        p = p + v
        if not in_bounds(p):
            break

    p = a
    while True:
        p = p - v
        if not in_bounds(p):
            break
        pts.append(tuple(p))

    return pts

def assign_antinodes(antinodes: np.ndarray, symbol: int, exact=True):
    antennae = np.argwhere(grid == symbol)
    # (N x 2)
    for a, b in combinations(antennae, r=2):
        v = a - b
        if exact:
            pts = [(symbol, *tuple(a + v)), (symbol, *tuple(b - v))]
        else:
            pts = [(symbol, *aligned_pts) for aligned_pts in get_all_aligned_points(a, v)]
        for pt in pts:
            if in_bounds(pt[-2:]):
                antinodes[pt] = 1

antinodes = np.zeros((len(char_map), *grid.shape))
for symbol in symbols:
    if not symbol: continue # ignore empty space
    assign_antinodes(antinodes, symbol, exact=True)
any_antinode = np.any(antinodes, axis=0).sum()
print(f"{any_antinode=}")

antinodes = np.zeros((len(char_map), *grid.shape))
for symbol in symbols:
    if not symbol: continue # ignore empty space
    assign_antinodes(antinodes, symbol, exact=False)
any_antinode = np.any(antinodes, axis=0).sum()
print(f"{any_antinode=}")


hashes = (np.where(antinodes.any(axis=0), "#", "."))
for line in hashes: print("".join(h for h in line))