import numpy as np
from parse import parse
from itertools import combinations


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


def score(M, amnts):
	scores = M.dot(amnts)
	if np.any(scores < 0):
		return 0
	return np.prod(scores)


def find_best_scores(nigr_values, limit_calories=500):
	num_ingredients = ingr_values.shape[1]
	amnts = np.ones(num_ingredients) * 100 / num_ingredients
	M = ingr_values[:-1, :]
	calories = ingr_values[-1, :]
	calories_scores = set()

	print("Initial score", score(M, amnts))
	highest_score = 0
	highest_calories_score = 0
	for (a, b, c) in combinations(np.arange(101), 3):
		amnts = np.array([a, b - a, c - b, 100 - c])

		if (move_score := score(M, amnts)) > highest_score:
			highest_score = move_score
			best_move = amnts

		if limit_calories and calories.dot(amnts) == limit_calories:
			if (move_score := score(M, amnts)) > highest_calories_score:
				highest_calories_score = move_score

	return highest_score, highest_calories_score

ingr_values = read_input()
highest_score, highest_calories_score = find_best_scores(ingr_values, limit_calories=500)
print("Part one", highest_score)
print("Part two", highest_calories_score)