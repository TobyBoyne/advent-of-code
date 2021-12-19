import numpy as np

with open('day09.txt') as f:
    depth = np.array([[c for c in line.strip()] for line in f.readlines()], dtype=int)

def part_one():
    depth_bordered = 10 * np.ones((depth.shape[0] + 2, depth.shape[0] + 2))
    depth_bordered[1:-1, 1:-1] = depth

    diffx = np.diff(depth_bordered, axis=1)[1:, :]
    diffy = np.diff(depth_bordered, axis=0)[:, 1:]

    minx = np.logical_and(diffx < 0, np.roll(diffx, -1, axis=1) > 0)
    miny = np.logical_and(diffy < 0, np.roll(diffy, -1, axis=0) > 0)
    all_min = np.logical_and(minx, miny)

    low_points = depth[np.nonzero(all_min)]
    return (low_points + 1).sum()

print(part_one())