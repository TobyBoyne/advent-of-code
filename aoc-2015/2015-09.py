import numpy as np
from itertools import permutations, tee

def pairwise(iterable):
	# taken from itertools docs
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)


def read_file():
	with open("day09.txt") as f:
		lines = f.readlines()
		# the (N-1)th triangle number is the number of lines in the file
		N = int(0.5 + np.sqrt(2 * len(lines) + 0.25))
		distances = np.zeros((N, N))
		locations = {}
		count = 0

		for line in lines:
			locs, d = line.strip("\n").split(" = ")
			loc_1, _, loc_2 = locs.split()
			for loc in (loc_1, loc_2):
				if loc not in locations:
					locations[loc] = count
					count += 1

			i, j = (locations[loc] for loc in (loc_1, loc_2))

			distances[i, j] = int(d)
			distances[j, i] = int(d)
	return distances, locations


def part_one(distances, locations):
	paths = []
	for p in permutations(locations.values()):
		if p[::-1] not in paths:
			paths.append(p)

	lengths = []
	for path in paths:
		path_length = 0
		for i, j in pairwise(path):
			path_length += distances[i, j]
		lengths.append((path_length, path))

	loc_from_num = {v: k for k, v in locations.items()}
	shortest_length, shortest_num_path = min(lengths, key=lambda x: x[0])
	print([loc_from_num[i] for i in shortest_num_path])
	return shortest_length


distances, locations = read_file()
print(part_one(distances, locations))