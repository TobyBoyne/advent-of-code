import numpy as np

def get_geologic_index(x, y, grid):
	if (x, y) in ((0, 0), TARGET):
		return 0
	if y == 0:
		return x * 16807
	if x == 0:
		return y * 48271
	return grid[y-1, x] * grid[y, x-1]

def get_erosion_level(geologic_index):
	return (geologic_index + DEPTH) % 20183

def part_one():
	w, h = (c + 1 for c in TARGET)
	erosion_levels = np.zeros((h, w))

	for y in range(h):
		for x in range(w):
			geo_index = get_geologic_index(x, y, erosion_levels)
			erosion = get_erosion_level(geo_index)
			erosion_levels[y, x] = erosion

	grid = erosion_levels % 3
	return np.sum(grid)

TARGET = (9, 751)
DEPTH = 11817
print(part_one())