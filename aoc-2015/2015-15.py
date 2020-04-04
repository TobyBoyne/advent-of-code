import numpy as np
from parse import parse

# x = np.array([
# 	[1, 2],
# 	[3, 4]
# ])
#
# y = np.array([5, 6])
# print(x * y)
# print(x.dot(y))
#
#
# a = np.array([1, 1, 1])
# b = np.array([
# 	[1, 2],
# 	[3, 4],
# 	[5, 6]
# ])
# print(a.dot(b))

MOVES = np.array([
	[1, 0, 0, -1],
	[0, 1, 0, -1],
	[0, 0, 1, -1]
])


def read_input():
	with open("day15.txt") as f:
		lines = f.readlines()
		N = len(lines)
		ingr_values = np.zeros((5, N))
		for i, line in enumerate(lines):
			p = parse("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}",
					  line.strip("\n"))
			_, *values = p.fixed
			ingr_values[:, i] = values
	return ingr_values

def gen_steps(amnts):
	for move in MOVES:
		for i in range(-10, 10):
			yield amnts + i * move


def score(M, amnts):
	scores = M.dot(amnts)
	if np.any(scores < 0):
		return 0
	return np.prod(scores)

def part_one(ingr_values):
	"""Using Matrix algebra
	M . [a1, a2, ..., an] = [cap, dur, flav, texture], where a is the number of teaspoons"""

	num_ingredients = ingr_values.shape[1]
	amnts = np.ones(num_ingredients) * 100 / num_ingredients
	M = ingr_values[:-1, :]

	print("Initial score", score(M, amnts))

	for i in range(100):
		highest_score = 0
		best_move = amnts
		for move in gen_steps(amnts):
			if (move_score := score(M, move)) > highest_score:
				highest_score = move_score
				best_move = move

		amnts = best_move
	print("Best score", score(M, amnts))
	return amnts

ingr_values = read_input()
print(part_one(ingr_values))