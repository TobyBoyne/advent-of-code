from math import atan2
from itertools import cycle

def read_input():
	asteroids = []
	with open("day10.txt") as f:
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				if c == '#':
					asteroids.append((x, y))
	return asteroids

def num_detected(station, all_asteroids):
	in_sight = {}
	stat_x, stat_y = station
	for ast_x, ast_y in all_asteroids:
		if (ast_x, ast_y) != station:
			dy, dx = stat_y - ast_y, ast_x - stat_x
			# rotate by 90 deg
			dx, dy = -dy, dx
			angle = - atan2(dy, dx)
			d = abs(dx) + abs(dy)
			in_sight[angle] = in_sight.get(angle, []) + [(d, ast_x, ast_y)]

	return in_sight


def find_station(asteroids):
	num_detections = {}
	for asteroid in asteroids:
		num_detections[asteroid] = (len(num_detected(asteroid, asteroids)))

	station = max(num_detections, key=num_detections.get)
	return station, num_detections[station]



def part_two(asteroids, station):
	asteroids_dict = num_detected(station, asteroids)
	# sort all asteroids by angle and distance
	all_angles = list(sorted(asteroids_dict.keys()))
	for key, value in asteroids_dict.items():
		asteroids_dict[key] = sorted(value, key=lambda x: x[0])

	destroyed = 0
	for angle in cycle(all_angles):
		if details := asteroids_dict[angle]:
			cur_asteroid = details.pop(0)
			destroyed += 1
			if destroyed == 200:
				return cur_asteroid


asteroids = read_input()
station, n = find_station(asteroids)

print("Part one:", n)
print("Station is at", station)
print(part_two(asteroids, station))
