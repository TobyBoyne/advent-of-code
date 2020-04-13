import numpy as np
from time import perf_counter


moves = (
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0)
)


def read_input():
	with open("day24.txt") as f:
		grid = []
		locations = {}
		start = None
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				if c in '1234567':
					locations[(x, y)] = int(c)
				elif c == '0':
					start = (y, x)
			grid.append([c!='#' for c in line.strip("\n")])
	return np.array(grid), locations, start


def adjacent_tiles(x, y, max_x, max_y):
	for (dx, dy) in moves:
		if max_x > (new_x := x + dx) >= 0 and max_y > (new_y := y + dy) >= 0:
			yield new_x, new_y



def distance_to_points(grid, locations, start=(1, 1)):
	distance_grid = np.full_like(grid, np.inf, dtype=float)
	distance_grid[start] = 0
	new_points = [start]
	num_steps = 0
	locs_distance = {}

	# depends_on stores the last location that needs to be visited before that one can be reached
	depends_on = 0

	while new_points:
		num_steps += 1
		cur_points = new_points
		new_points = []
		for (x, y) in cur_points:
			for new_x, new_y in adjacent_tiles(x, y, 50, 50):
				depends_on = distance_grid[y, x]
				if grid[new_y, new_x] and distance_grid[new_y, new_x] == np.inf:
					# if the point is a key location, add to locations and change depends_on
					if (new_x, new_y) in locations:
						loc = locations[(new_x, new_y)]
						locs_distance[loc] = (num_steps, depends_on)
						depends_on = loc
					distance_grid[new_y, new_x] = depends_on
					new_points.append((new_x, new_y))

	return distance_grid, locs_distance


grid, locations, start = read_input()
print(start)
print(distance_to_points(grid, locations, start))