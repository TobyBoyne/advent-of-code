import numpy as np
from math import atan2

def read_input():
	asteroids = []
	with open("day10.txt") as f:
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				if c == '#':
					asteroids.append((x, y))
	return asteroids

def num_detected(station, all_asteroids):
	in_sight = set()
	stat_x, stat_y = station
	for ast_x, ast_y in all_asteroids:
		if (ast_x, ast_y) != station:
			dy, dx = ast_y - stat_y, ast_x - stat_x
			in_sight.add(atan2(dy, dx))

	return len(in_sight)

def part_one(asteroids):
	num_detections = set()
	for asteroid in asteroids:
		num_detections.add(num_detected(asteroid, asteroids))
	return max(num_detections)



asteroids = read_input()
print(part_one(asteroids))
