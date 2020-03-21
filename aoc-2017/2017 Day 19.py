SIZE = 205

class V:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		return V(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return V(self.x - other.x, self.y - other.y)
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def index_grid(self, grid):
		return grid[self.y][self.x]

	def __repr__(self):
		return 'V(' + str(self.x) + ', ' + str(self.y) + ')'


DIR = {
	'up':	V(0, -1),
	'down':	V(0, 1),
	'left':	V(-1, 0),
	'right':V(1, 0)
}

def read_file():
	grid = [[' ' for i in range(SIZE)] for j in range(SIZE)]
	with open("day19.txt", 'r') as f:
		for y, line in enumerate(f):
			for x, c in enumerate(line.strip("\n")):
				grid[y][x] = c
	return grid

def move_through(grid):
	start_x = max(range(len(grid[0])), key=lambda x: grid[0][x])
	cur = V(start_x, 0)
	d = DIR['down']

	steps = 0
	letters = []
	on_track = True
	while on_track:
		new_pos = cur + d
		steps += 1
		if new_pos.index_grid(grid) in map(chr, range(65, 91)) and new_pos.index_grid(grid) not in letters:
			letters.append(new_pos.index_grid(grid))
		elif new_pos.index_grid(grid) == '+':
			for next_pos in map(lambda x: new_pos + x, [DIR[direction] for direction in DIR]):
				if next_pos != cur and next_pos.index_grid(grid) != ' ':
					d = next_pos - new_pos

		elif new_pos.index_grid(grid) == ' ':
			on_track = False

		cur = new_pos

	return letters, steps


def print_grid(grid):
	output = ""
	for row in grid:
		if not all(c == ' ' for c in row):
			output += "".join(c for c in row) + "\n"
	print(output)


grid = read_file()
print_grid(grid)

letters, steps = move_through(grid)
print("Part one:", "".join(letters))
print("Part two:", steps)