class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self, other):
		return Vector(other * self.x, other * self.y)
	def __rmul__(self, other):
		return self * other

	def __repr__(self):
		return str((self.x, self.y))

class Slice:
	def __init__(self, *springs):
		self.grid = []
		self.springs = springs
		self.done = False

		self.top_left = Vector(0, 0)
		self.btm_right = Vector(0, 0)

		self.create_grid()

		self.run()

		self.display()
		self.part_one()
		self.part_two()

	def create_grid(self):
		veins = []
		with open("day17.txt", 'r') as f:
			for line in f:
				inputs = line.strip("\n").split(", ")
				if inputs[0][0] == 'x':
					x = int(inputs[0][2:])
					spread = [int(n) for n in inputs[1][2:].split("..")]
					new_vein = [Vector(x, y) for y in range(spread[0], spread[1] + 1)]
				else:
					y = int(inputs[0][2:])
					spread = [int(n) for n in inputs[1][2:].split("..")]
					new_vein = [Vector(x, y) for x in range(spread[0], spread[1] + 1)]
				veins += new_vein

		max_x, max_y = max(veins, key=lambda v:v.x).x, max(veins, key=lambda v:v.y).y
		min_x, min_y = min(veins, key=lambda v:v.x).x, min(veins, key=lambda v:v.y).y

		self.grid = [['.' for i in range(max_x + 30)] for j in range(max_y + 30)]
		for vein in veins:
			self.set_coord(vein, '#')

		for spring in self.springs:
			self.set_coord(spring, '+')

		self.top_left = Vector(min_x, min_y)
		self.btm_right = Vector(max_x, max_y)

	def get_coord(self, coord):
		if isinstance(coord, Vector):
			return self.grid[coord.y][coord.x]
		else:
			return self.grid[coord[1]][coord[0]]

	def set_coord(self, coord, value):
		if isinstance(coord, Vector):
			self.grid[coord.y][coord.x] = value
		else:
			self.grid[coord[1]][coord[0]] = value


	def run(self):
		while not self.done:
			for spring in self.springs:
				spring.step(self)
				self.done = self.done or spring.done




	def part_one(self):
		total = 0
		for line in self.grid[self.top_left.y : self.btm_right.y + 1]:
			for c in line:
				total += c in '|/~'
		print("Part one", total)
		return total

	def part_two(self):
		total = 0
		for line in self.grid[self.top_left.y: self.btm_right.y + 1]:
			for c in line:
				total += c == '~'
		print("Part two:", total)
		return total

	def display(self):
		PAD = 5
		l, r = self.top_left.x - PAD, self.btm_right.x + PAD
		btm = self.btm_right.y + PAD
		[print("".join([c for c in line[l: r]])) for line in self.grid[:btm]]
		print('\n\n' + '_' * 50 + '\n\n')


class Spring(Vector):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.done = False

		# w stores the coordinates of the leading particle of water
		self.w = Vector(x, y + 1)
		# to_check stores coordinates of flowing water that may need to be re-evalutated later
		# system acts in two passes - top down, then bottom up
		self.to_check = []

	def step(self, grid):
		grid.set_coord(self.w, '|')
		if grid.get_coord(self.w + DOWN) == '.':
			#grid.set_coord(self.w, '|')
			if self.w.y > grid.btm_right.y:
				self.next_stream()
			else:
				self.to_check.append(self.w)
				self.w += DOWN

		elif grid.get_coord(self.w + DOWN) in '|/':
			self.next_stream()

		else:
			x_scan = self.w
			r_fall = False
			while grid.get_coord(x_scan + RIGHT) in '.|/' and not r_fall:
				x_scan += RIGHT
				if grid.get_coord(x_scan + DOWN) in '.|/':
					r_fall = True
			r_limit = x_scan.x

			x_scan = self.w
			l_fall = False
			while grid.get_coord(x_scan + LEFT) in '.|/' and not l_fall:
				x_scan += LEFT
				if grid.get_coord(x_scan + DOWN) in '.|/':
					l_fall = True
			l_limit = x_scan.x

			if not r_fall and not l_fall:
				[grid.set_coord(Vector(i, self.w.y), '~') for i in range(l_limit, r_limit + 1)]
			else:
				[grid.set_coord(Vector(i, self.w.y), '/') for i in range(l_limit, r_limit + 1)]
				if r_fall:
					self.to_check.append(Vector(r_limit, self.w.y))
				if l_fall:
					self.to_check.append(Vector(l_limit, self.w.y))

			# as this is the bottom of this particular stream, now evaluate a different stream
			self.next_stream()


	# evaluate the next stream (after a stream has been completely evaluated)
	def next_stream(self):
		if self.to_check:
			self.w = self.to_check.pop()
		else:
			self.done = True

UP = Vector(0, -1)
DOWN = Vector(0, 1)
LEFT = Vector(-1, 0)
RIGHT = Vector(1, 0)


SPRINGS = Spring(500, 0)

my_grid = Slice(SPRINGS)
