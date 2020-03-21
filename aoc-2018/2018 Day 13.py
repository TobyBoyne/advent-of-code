import numpy as np

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

class Cart:
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.dir = direction
		self.next_turn = "anti-clockwise"
		self.alive = True
	def coords(self):
		return	self.x, self.y
	def move(self, direction):
		self.dir = direction
		if direction == UP:
			dx, dy = 0, -1
		elif direction == DOWN:
			dx, dy = 0, 1
		elif direction == RIGHT:
			dx, dy = 1, 0
		elif direction == LEFT:
			dx, dy = -1, 0
		self.x += dx
		self.y += dy
	def next_inter(self, next_turn):
		self.next_turn = next_turn
	def __eq__(self, other):
		if isinstance(other, Cart):
			return	other.x == self.x and other.y == self.y and other.alive and self.alive
		elif isinstance(other, tuple):
			return	other[0] == self.x and other[1] == self.y
		elif isinstance(other, str):
			return	other == self.dir
		else:
			return	False

	def __str__(self):
		return self.dir


class Track:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return ' '
	def get_move(self, *args):
		print("Error - the cart has fallen off the track!")
		return 0, 0, UP


# All straight tracks are modelled as intersections
# (Assuming that no tracks are dead ends)
class Straight(Track):
	def __init__(self, x, y, char):
		super().__init__(x, y)
		self.type = 0 if char == '-' else 1
	def get_move(self, cart):
		return cart.dir

	def __str__(self):
		return	['-', '|'][self.type]

class Curve(Track):
	def __init__(self, x, y, char):
		super().__init__(x, y)
		self.type = 0 if char == '/' else 1
	def get_move(self, cart):
		if cart == UP:
			return [RIGHT, LEFT][self.type]
		elif cart == DOWN:
			return [LEFT, RIGHT][self.type]
		elif cart == RIGHT:
			return [UP, DOWN][self.type]
		elif cart == LEFT:
			return [DOWN, UP][self.type]

	def __str__(self):
		return	['/', '\\'][self.type]

class Inter(Track):
	def __init__(self, x, y):
		super().__init__(x, y)
	def get_move(self, cart):
		directions = [UP, RIGHT, DOWN, LEFT]
		if cart.next_turn == "anti-clockwise":
			cart.next_turn = "straight"
			return	directions[directions.index(cart.dir) - 1]
		if cart.next_turn == "straight":
			cart.next_turn = "clockwise"
			return	cart.dir
		if cart.next_turn == "clockwise":
			cart.next_turn = "anti-clockwise"
			return	directions[(directions.index(cart.dir) + 1) % 4]

	def __str__(self):
		return '+'

class Map:
	def __init__(self, width, height):
		self.w = width
		self.h = height
		self.tracks = [[Track(i, j) for i in range(self.w)] for j in range(self.h)]
		self.carts = []
		self.collision = False
		self.done = False
		# index tracks with self.tracks[y][x]
		self.read()
		self.display()

	def read(self):
		with open("day13.txt", 'r') as f:
			for y, line in enumerate(f):
				for x, char in enumerate(line):
					if char in "|-":
						self.tracks[y][x] = Straight(x, y, char)
					elif char in "\/":
						self.tracks[y][x] = Curve(x, y, char)
					elif char == '+':
						self.tracks[y][x] = Inter(x, y)
					elif char in "<>^v":
						self.tracks[y][x] = Straight(x, y, ['-', '|'][char in "<>"])
						self.carts.append(Cart(x, y, char))

	def step(self):
		for cart in [c for c in self.carts if c.alive == True]:
			x, y = cart.x, cart.y
			new_dir = self.tracks[y][x].get_move(cart)
			cart.move(new_dir)
			self.check_collision()
		#self.display()

	def check_collision(self):
		for i in range(len(self.carts)):
			for j in range(len(self.carts)):
				if i != j and self.carts[i] == self.carts[j]:
					pos = self.carts[i].coords()
					if not self.collision:
						print("First collision at", pos)
						self.collision = True
					self.carts[i].alive = False
					self.carts[j].alive = False
					self.check_continue()

	def check_continue(self):
		alive_carts = [cart for cart in self.carts if cart.alive == True]
		if len(alive_carts) == 1:
			pos = alive_carts[0].coords()
			print("Last remaining cart at", pos)
			self.done = True

	def display(self):
		output = [[' ' for i in range(self.w)] for j in range(self.h)]
		for x in range(self.w):
			for y in range(self.h):
				if self.collision == (x, y):
					output[y][x] = 'X'
				elif (x, y) in self.carts:
					for cart in self.carts:
						if (x, y) == cart:
							output[y][x] = str(cart)
				else:
					output[y][x] = str(self.tracks[y][x])
		print("\n".join([" ".join([x for x in y]) for y in output]))
		print("_" * 20)

my_map = Map(160,160)
while not my_map.done:
	my_map.step()

