import numpy as np

moves = (
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0)
)

def is_open(x, y):
	a = x*x + 3*x + 2*x*y + y + y*y + 1350
	num_ones = bin(a).count('1')
	return num_ones % 2 == 0

def adjacent_tiles(x, y, max_x, max_y):
	for (dx, dy) in moves:
		if max_x > (new_x := x + dx) >= 0 and max_y > (new_y := y + dy) >= 0:
			yield new_x, new_y

def distance_to_points(grid, start=(1, 1)):
	distance_grid = np.full_like(grid, -1, dtype=int)
	new_points = [start]
	num_steps = 0
	while new_points:
		num_steps += 1
		cur_points = new_points
		new_points = []
		for (x, y) in cur_points:
			for new_x, new_y in adjacent_tiles(x, y, 50, 50):
				if grid[new_y, new_x] and distance_grid[new_y, new_x] == -1:
					distance_grid[new_y, new_x] = num_steps
					new_points.append((new_x, new_y))

	return distance_grid

def part_one():
	grid = np.array([[is_open(x, y) for x in range(50)] for y in range(50)])
	distance_grid = distance_to_points(grid)
	return distance_grid[39, 31]

print(part_one())
