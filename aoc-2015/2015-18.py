import numpy as np

def read_input():
	with open("day18.txt") as f:
		lights = np.zeros((100, 100))
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				lights[y, x] = 1 if c =='#' else 0

	return lights

def num_adjacent(lights, y, x, value):
	x_1, x_2 = max(x-1, 0), x+2
	y_1, y_2 = max(y-1, 0), y+2
	return np.count_nonzero(lights[y_1:y_2, x_1:x_2]) - value

def animate(lights):
	new_lights = np.zeros_like(lights)
	for (y, x), value in np.ndenumerate(lights):
		n = num_adjacent(lights, y, x, value)
		if (value == 1 and n in (2, 3)) or (value == 0 and n == 3):
			new_lights[y, x] = 1
		else:
			new_lights[y, x] = 0
	return new_lights


def part_one(lights):
	for i in range(100):
		lights = animate(lights)
	return np.count_nonzero(lights)

lights = read_input()
print(part_one(lights))