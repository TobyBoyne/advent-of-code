from math import inf
from math import log10

# 				UP		 LEFT  	 RIGHT	  DOWN
DIRECTIONS = [(0, -1), (-1, 0), (1, 0), (0, 1)]


# --- CHARACTER CLASS ---

class Character:
	def __init__(self, x, y, race, cave, elf_atk=3):
		self.x = x
		self.y = y
		self.race = race
		self.cave = cave

		self.atk = 3 if race == 'G' else elf_atk
		self.hp = 200
		self.alive = True

	def step(self):
		self.move()
		self.attack()

	# MOVING LOGIC
	def move(self):
		new_x, new_y = self.calculate_move()
		self.x = new_x
		self.y = new_y

	def gen_distance_grid(self, *origin):
		if len(origin) == 1:
			x, y = origin[0]
		elif len(origin) == 2:
			x, y = origin
		else:
			x, y = self.x, self.y

		# each space in the grid has value distance
		made_move = True
		dist_grid = [[inf for i in range(self.cave.size)] for j in range(self.cave.size)]
		dist_grid[y][x] = 0
		visited_spaces = [[x, y]]
		exhausted_spaces = []
		dist = 1

		# create a grid showing the distance from self to each point on the grid
		# if it cannot reach a point, the distance is infinite
		while made_move:
			made_move = False
			for coord in [c for c in visited_spaces if c not in exhausted_spaces]:
				for d in DIRECTIONS:
					new_x, new_y = coord[0] + d[0], coord[1] + d[1]
					if self.cave.free_space(new_x, new_y) or (new_x, new_y) == (self.x, self.y):
						made_move = True
						if [new_x, new_y] not in visited_spaces:
							visited_spaces.append([new_x, new_y])
						if dist < dist_grid[new_y][new_x]:
							dist_grid[new_y][new_x] = dist
				exhausted_spaces.append(coord)

			dist += 1
		#[print([c if c != inf else 'X' for c in line]) for line in dist_grid]
		return	dist_grid

	def calculate_move(self):
		dist_grid = self.gen_distance_grid()
		# create a list of all coordinates in range of an enemy
		in_range = []
		for other in [char for char in self.cave.char_list if char.race != self.race]:
			for d in DIRECTIONS:
				check_x, check_y = other.x + d[0], other.y + d[1]
				if self.cave.free_space(check_x, check_y) or (check_x, check_y) == (self.x, self.y):
					in_range.append([check_x, check_y])

		# select the closest target position (in reading order)
		in_range.sort(key=lambda x: (-x[1], -x[0]))
		min_dist = inf
		target_x, target_y = self.x, self.y
		for coord in in_range:
			if dist_grid[coord[1]][coord[0]] <= min_dist:
				min_dist = dist_grid[coord[1]][coord[0]]
				target_x, target_y = coord

		# make a move in the direction of the target position
		# valid_moves is sorted in order of favourite to least (up, left, right, down)
		valid_moves = [[self.x + d[0], self.y + d[1]] for d in DIRECTIONS]
		target_dist_grid = self.gen_distance_grid(target_x, target_y)
		move_x, move_y = self.x, self.y
		for move in valid_moves:
			if target_dist_grid[move[1]][move[0]] < target_dist_grid[move_y][move_x]:
				move_x, move_y = move
		return	move_x, move_y

	# ATTACKING LOGIC
	def attack(self):
		has_target = False
		attack_race = 'G' if self.race == 'E' else 'E'
		for d in DIRECTIONS:
			target_char = self.cave.in_cave(self.x + d[0], self.y + d[1], attack_race)
			if target_char:
				if not has_target:
					has_target = True
					atk_char = target_char
				elif target_char.hp < atk_char.hp:
					atk_char = target_char

		if has_target:
			atk_char.damage(self.atk)

	def damage(self, dmg):
		self.hp -= dmg
		if self.hp <= 0:
			self.alive = False
			self.cave.clean_char_list()
			if self.race == 'E':
				self.cave.elves_lost = True

	def __str__(self):
		return	self.race
	def __repr__(self):
		return	self.race + "(" + str(self.x) + ", " + str(self.y) + ")"


# --- CAVE CLASS ---

class Cave:
	def __init__(self, size, elf_atk=3):
		self.grid = [['.' for i in range(size)] for j in range(size)]
		# self.grid[y][x]
		self.size = size
		self.char_list = []
		self.done = False
		self.score = 0
		self.round_count = 0

		self.elves_lost = False
		self.elf_atk = elf_atk

		self.read_file()
		self.display_map()

	def read_file(self):
		with open("day15.txt", 'r') as f:
			for y, line in enumerate(f):
				for x, c in enumerate(line):
					if c == '#':
						self.grid[y][x] = c
					elif c in 'EG':
						self.char_list.append(Character(x, y, c, self, self.elf_atk))

	def free_space(self, x, y):
		if 0 <= x <= self.size - 1 and 0 <= y <= self.size - 1:
			if not self.in_cave(x, y) and self.grid[y][x] == '.':
				return True
		return False

	def in_cave(self, x, y, race=''):
		for char in self.char_list:
			if x == char.x and y == char.y and char.alive and (race == char.race or race == ''):
				return char
		return False



	def step(self):
		self.clean_char_list()
		for char in self.char_list:
			if not self.done and char.alive:
				char.step()
				self.check_done()
			if char == self.char_list[-1]:
				self.round_count += 1

		print(self.round_count)
		#self.display_map()

	def clean_char_list(self):
		# remove dead items and sort list by reading order
		self.char_list = [char for char in self.char_list if char.alive]
		self.char_list.sort(key=lambda item:(item.y, item.x))

	def check_done(self):
		if self.elves_lost or len(set([char.race for char in self.char_list])) < 2:
			self.display_map()
			self.done = True
			self.score = self.round_count * sum([char.hp for char in self.char_list])
			print("Number of rounds:", self.round_count)
			print("Score:", self.score)

	def display_map(self):
		output = []
		for row in self.grid:
			output.append([c for c in row])
		for char in self.char_list:
			if char.alive:
				output[char.y][char.x] = char.race
				output[char.y].append("\t" + str(char.hp))

		print("Round:", self.round_count)
		[print("".join([c for c in line])) for line in output]
		print()

# -- PART ONE --
# my_cave = Cave(32)
# while not my_cave.done:
# 	my_cave.step()

# -- PART TWO --
elf_total_victory = False
atk = 10
while not elf_total_victory:
	my_cave = Cave(32, atk)
	while not my_cave.done:
		my_cave.step()
	if not my_cave.elves_lost:
		elf_total_victory = True
		print("Attack Power:", atk)
	atk += 1
