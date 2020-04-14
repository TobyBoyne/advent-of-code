import numpy as np
from parse import parse

def read_input():
	with open('day23.txt') as f:
		nanobots = []
		for line in f:
			p = parse('pos=<{:d},{:d},{:d}>, r={:d}',
					  line.strip("\n"))
			nanobots.append(p.fixed)
	return np.array(nanobots)

def part_one(nanobots):
	# find strongest nanobot
	strengths = nanobots[:, 3]
	idx = np.where(strengths == np.max(strengths))[0][0]
	strongest = nanobots[idx]

	in_range = 0
	for bot in nanobots:
		if np.sum(np.abs(strongest[:3] - bot[:3])) <= strongest[3]:
			in_range += 1
	return in_range


nanobots = read_input()

print(part_one(nanobots))