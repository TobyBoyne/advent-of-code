import numpy as np
from parse import parse
from itertools import permutations

def read_file():
	names = {}
	count = 0
	with open("day13.txt") as f:
		lines = f.readlines()
		N = int(0.5 + np.sqrt(len(lines) + 0.25))
		happiness_matrix = np.zeros((N, N))
		for line in lines:
			p = parse("{} would {} {:d} happiness units by sitting next to {}.", line.strip("\n"))
			i_name, gain, value, j_name = p.fixed
			for name in (i_name, j_name):
				if name not in names:
					names[name] = count
					count += 1

			i, j = names[i_name], names[j_name]
			value *= 1 if gain == "gain" else -1
			happiness_matrix[i, j] = value

	return happiness_matrix

def pairings(arrangement):
	# yield all pairings of adjacent seats (including [0] -> [-1])
	for i in range(len(arrangement)):
		yield (arrangement[i - 1], arrangement[i])
		yield (arrangement[i], arrangement[i - 1])


def part_one(happiness_matrix):
	arrangements = []
	for perm in permutations(range(happiness_matrix.shape[0])):
		# only add if Alice is the first; removes repeats of cycle as order does not matter
		if perm[0] == 0 and perm[::-1] not in arrangements:
			arrangements.append(perm)

	all_happiness = []
	for arrangement in arrangements:
		total_happiness = 0
		for pair in pairings(arrangement):
			total_happiness += happiness_matrix[pair]

		all_happiness.append(total_happiness)

	return max(all_happiness)

def part_two(happiness_matrix):
	N = happiness_matrix.shape[0]
	new_matrix = np.zeros((N+1, N+1))
	new_matrix[:N, :N] = happiness_matrix

	return part_one(new_matrix)

happiness_matrix = read_file()
print(part_one(happiness_matrix))
print(part_two(happiness_matrix))