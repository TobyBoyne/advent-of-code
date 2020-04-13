"""
https://www.educative.io/edpresso/how-to-implement-dijkstras-algorithm-in-python
https://networkx.github.io/documentation/stable/index.html
"""


import numpy as np
import networkx as nx

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

def make_grid(size):
	w, h = (c + 1 for c in size)
	erosion_levels = np.zeros((h, w))

	for y in range(h):
		for x in range(w):
			geo_index = get_geologic_index(x, y, erosion_levels)
			erosion = get_erosion_level(geo_index)
			erosion_levels[y, x] = erosion

	grid = erosion_levels % 3
	return grid

def part_one():
	grid = make_grid(TARGET)
	return np.sum(grid)

TARGET = (9, 751)
DEPTH = 11817
print(part_one())