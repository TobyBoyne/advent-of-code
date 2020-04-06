from parse import parse
import numpy as np
from itertools import permutations

def read_input():
	grid = np.zeros((30, 32, 2))
	with open("day22.txt") as f:
		for line in f:
			p = parse("/dev/grid/node-x{:d}-y{:d}{:>d}T{:>d}T{:>d}T{:>d}%",
					  line.strip("\n"))
			x, y, _, used, avail, _ = p.fixed
			grid[y, x, :] = used, avail
	return grid

def viable_pair(A, B):
	return A[0] != 0 and A[0] <= B[1]

def part_one(grid):
	all_nodes = grid.reshape((-1, 2))
	num_viable = 0
	for A, B in permutations(all_nodes, 2):
		num_viable += viable_pair(A, B)
	return num_viable


grid = read_input()
print(part_one(grid))