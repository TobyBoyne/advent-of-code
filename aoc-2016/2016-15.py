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

def part_two(discs):
	ts = []
	t = 0
	new_disc = (len(discs) + 1, 11)
	new_disc_pos = []
	while len(ts) < 2:
		if lines_up(discs, t):
			ts.append(t)
			new_disc_pos.append((new_disc[0] + t) % new_disc[1])
		t += 1

	# treat the configuration as two discs: the combination of all previous discs, and the new disc
	# simplify the phase difference between these and use it to find when they are next equal at pos=0
	dt = ts[1] - ts[0]
	dp = new_disc_pos[1] - new_disc_pos[0]
	i = 0
	while (new_disc_pos[0] + i * dp) % new_disc[1] != 0:
		i += 1

	T = ts[0] + i * dt
	return T

discs = read_input()
print(part_one(discs))
print(part_two(discs))