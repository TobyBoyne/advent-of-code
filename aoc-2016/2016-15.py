from parse import parse
import numpy as np

def read_input():
	with open("day15.txt") as f:
		lines = f.readlines()
		N = len(lines)
		discs = np.zeros((N, 2))
		for line in lines:
			p = parse("Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.",
					  line.strip("\n"))
			i, num_pos, initial_pos = p.fixed
			discs[i-1, :] = [initial_pos + i, num_pos]

	return discs

def lines_up(discs, t):
	positions = (discs[:, 0] + t) % discs[:, 1]
	return np.all(positions == 0)

def part_one(discs):
	t = 0
	while not lines_up(discs, t):
		t += 1
	return t

discs = read_input()
print(discs)
print(part_one(discs))