import numpy as np

with open('day09.txt') as f:
    depth = np.array([[c for c in line.strip()] for line in f.readlines()], dtype=int)

def find_minima():
    depth_bordered = 10 * np.ones((depth.shape[0] + 2, depth.shape[0] + 2))
    depth_bordered[1:-1, 1:-1] = depth

    diffx = np.diff(depth_bordered, axis=1)[1:, :]
    diffy = np.diff(depth_bordered, axis=0)[:, 1:]

    minx = np.logical_and(diffx < 0, np.roll(diffx, -1, axis=1) > 0)
    miny = np.logical_and(diffy < 0, np.roll(diffy, -1, axis=0) > 0)
    all_min = np.logical_and(minx, miny)

    return all_min

def part_one():
    minima = find_minima()
    low_points = depth[np.nonzero(minima)]
    return (low_points + 1).sum()

dirs = np.array([
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
])
def basin_size(basins, start_idx):
    to_explore = [start_idx]
    all_explored = set()
    total_size = 0
    while to_explore:
        prev_to_explore = to_explore
        to_explore = []

        for pt in prev_to_explore:
            # if out of bounds, a 9, or already explored
            if tuple(pt) in all_explored or \
                not (0 <= pt[0] < basins.shape[0]) or \
                not (0 <= pt[1] < basins.shape[0]) or \
                basins[tuple(pt)] == -1:

                continue

            all_explored.add(tuple(pt))

            total_size += 1
            next_pos = dirs + pt
            to_explore += list(next_pos)

    return total_size

def part_two():
    minima = find_minima()
    basins = np.zeros_like(depth)
    basins[np.nonzero(depth == 9)] = -1
    min_idxs = np.nonzero(minima)

    basin_sizes = []
    for x, y in zip(*min_idxs):
        start_idx = np.array([x, y])
        basin_sizes.append(basin_size(basins, start_idx))

    largest_basins = list(reversed(sorted(basin_sizes)))[:3]
    return np.prod(largest_basins)

print(part_one())
print(part_two())