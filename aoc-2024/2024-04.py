import numpy as np

X, M, A, S = range(4)

with open("day04.txt") as f:
    grid = [["XMAS".index(c) for c in line.strip()] for line in f.readlines()]

grid = np.array(grid)
grid = np.pad(grid, 1, constant_values=9)

num_xmas = 0
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        grid_rolled = np.zeros((*grid.shape, 4))
        for r in range(4):
            grid_rolled[:, :, r] = np.roll(grid, (i*r, j*r), axis=(0, 1))

        grid_diff = np.diff(grid_rolled, axis=-1)
        xmas = (grid_diff == 1).all(axis=-1)
        num_xmas += xmas.sum()

print(num_xmas)

grid_rolled = np.zeros((*grid.shape, 6))
grid_rolled[:, :, 0] = grid
grid_rolled[:, :, 1] = np.roll(grid, (1, 1), axis=(0, 1))
grid_rolled[:, :, 2] = np.roll(grid, (-1, -1), axis=(0, 1))

grid_rolled[:, :, 3] = grid
grid_rolled[:, :, 4] = np.roll(grid, (-1, 1), axis=(0, 1))
grid_rolled[:, :, 5] = np.roll(grid, (1, -1), axis=(0, 1))

mas_ne = (grid_rolled[:, :, :3] == np.array([A, M, S])[None, None, :]).all(axis=-1) 
mas_sw = (grid_rolled[:, :, :3] == np.array([A, S, M])[None, None, :]).all(axis=-1)
mas_nw = (grid_rolled[:, :, 3:] == np.array([A, M, S])[None, None, :]).all(axis=-1)
mas_se = (grid_rolled[:, :, 3:] == np.array([A, S, M])[None, None, :]).all(axis=-1)

mas = (mas_ne | mas_sw) & (mas_nw | mas_se)
print(mas.sum())