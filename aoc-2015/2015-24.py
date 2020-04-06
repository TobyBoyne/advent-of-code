from itertools import combinations
import numpy as np
from operator import mul
from functools import reduce

def read_input():
	weights = []
	with open("day24.txt") as f:
		for line in f:
			weights.append(int(line.strip("\n")))
	return weights


def part_one(weights):
	target_weight = sum(weights) / 3
	for r in range(10):
		qe_values = []
		for ws in combinations(weights, r):
			if sum(ws) == target_weight:
				qe_values.append(reduce(mul, ws, 1))
		if qe_values:
			break
	return min(qe_values)


weights = read_input()
print(part_one(weights))