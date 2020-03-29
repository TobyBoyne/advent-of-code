import numpy as np
from parse import parse

def read_input():
	with open("day14.txt") as f:
		lines = f.readlines()
		speeds = np.zeros((len(lines), 3))
		for i, line in enumerate(lines):
			p = parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.",
					  line.strip("\n"))
			_, speed, up_time, down_time = p.fixed
			speeds[i, :] = [speed, up_time, up_time+down_time]

	return speeds

def add_speeds(speeds, t):
	moves_this_turn = (t % speeds[:, 2]) < speeds[:, 1]
	distance_moved = speeds[:, 0] * moves_this_turn
	return distance_moved


def part_one(speeds, T):
	N = speeds.shape[0]
	distances = np.zeros(N)
	for t in range(T):
		distances += add_speeds(speeds, t)

	return max(distances)

def part_two(speeds, T):
	N = speeds.shape[0]
	distances = np.zeros(N)
	scores = np.zeros(N)
	for t in range(T):
		distances += add_speeds(speeds, t)
		winning_distance = np.amax(distances)
		first_places = np.argwhere(distances == winning_distance)
		scores[first_places] += 1

	return max(scores)

speeds = read_input()
T = 2503
print(part_one(speeds, T))
print(part_two(speeds, T))
