from collections import Counter

def read_input():
	containers = []
	with open("day17.txt") as f:
		for line in f:
			containers.append(int(line.strip("\n")))
	return containers

def num_combinations(containers, L):
	# containers must be sorted
	if L == 0:
		return 1
	total = 0
	for i, c in enumerate(containers):
		if c <= L:
			remaining = containers[:i]
			total += num_combinations(remaining, L - c)

	return total

def part_one(containers):
	containers.sort()
	all_combinations = num_combinations(containers, 150)

	return all_combinations

containers = read_input()
print(part_one(containers))