from collections import defaultdict

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def read_file():
	grid = defaultdict(lambda:'.')
	with open("day22.txt", 'r') as f:
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				grid[(x, y)] = c

	centre = y // 2
	return grid, centre


def infect(grid, centre, count):
	d = 0
	cur = (centre, centre)
	infected = 0
	for i in range(count):
		if grid[cur] == '#':
			d += 1
			grid[cur] = '.'
		else:
			d -= 1
			grid[cur] = '#'
			infected += 1

		d = d % len(DIRS)
		cur = (cur[0] + DIRS[d][0], cur[1] + DIRS[d][1])

	return infected


def evolved_infect(grid, centre, count):
	# increasing index == turning to the right
	d = 0
	infected = 0
	cur = (centre, centre)

	for i in range(count):
		if grid[cur] == '.':
			d -= 1
			grid[cur] = 'W'
		elif grid[cur] == 'W':
			grid[cur] = '#'
			infected += 1
		elif grid[cur] == '#':
			d += 1
			grid[cur] = 'F'
		else:
			d += 2
			grid[cur] = '.'

		d = d % len(DIRS)
		cur = (cur[0] + DIRS[d][0], cur[1] + DIRS[d][1])

	return infected


grid, centre = read_file()
print("Part one:", infect(grid, centre, 10000))

grid, centre = read_file()
print("Part two:", evolved_infect(grid, centre, 10000000))