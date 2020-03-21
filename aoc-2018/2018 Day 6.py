from math import inf

def generate_grid():
	with open("day6.txt", 'r') as f:
		grid = [[-1 for i in range(360)] for j in range(360)]
		loc_id = 0
		coords = []
		for line in f:
			x, y = [int(value) for value in line.strip("\n").split(", ")]
			coords.append([x, y, loc_id])
			grid[x][y] = loc_id
			loc_id += 1
	return grid, coords

# -- PART ONE --
def largest_finite_area():
	grid, coords = generate_grid()

	for grid_x in range(350):
		for grid_y in range(360):
			shortest_d, closest_id = inf, -1
			for x, y, loc_id in coords:
				d = abs(grid_x - x) + abs(grid_y - y)
				if d == shortest_d:
					closest_id = -1
				elif d < shortest_d:
					shortest_d = d
					closest_id = loc_id
			grid[grid_x][grid_y] = closest_id

	edge_coords = []
	for i in range(360):
		edge_coords += [grid[i][0]]
		edge_coords += [grid[i][359]]
		edge_coords += [grid[0][i]]
		edge_coords += [grid[359][i]]

	loc_areas = {}
	for *_, loc_id in coords:
		if not loc_id in edge_coords:
			loc_area = sum([row.count(loc_id) for row in grid])
			loc_areas[loc_id] = loc_area

	print(loc_areas[max(loc_areas, key=loc_areas.get)])

# -- PART TWO --
def size_of_safe_region(r):
	grid, coords = generate_grid()
	safe_coords = 0
	for grid_x in range(350):
		for grid_y in range(360):
			total_distance = sum([abs(grid_x - x) + abs(grid_y - y) for x, y, _ in coords])
			if total_distance < r:
				safe_coords += 1
	print(safe_coords)

#largest_finite_area()
size_of_safe_region(10000)