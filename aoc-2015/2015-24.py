from itertools import combinations
from operator import mul
from functools import reduce

def read_input():
	weights = []
	with open("day24.txt") as f:
		for line in f:
			weights.append(int(line.strip("\n")))
	return weights


def find_lowest_qe(weights, num_groups):
	target_weight = sum(weights) / num_groups
	for r in range(10):
		qe_values = []
		for ws in combinations(weights, r):
			if sum(ws) == target_weight:
				qe_values.append(reduce(mul, ws, 1))
		if qe_values:
			break
	return min(qe_values)

def part_one(weights):
	return find_lowest_qe(weights, num_groups=3)

def part_two(weights):
	return find_lowest_qe(weights, num_groups=4)


weights = read_input()
print(part_one(weights))
print(part_two(weights))