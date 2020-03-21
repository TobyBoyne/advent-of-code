import numpy as np

class Land:
	def __init__(self):
		self.size = 0
		self.counter = 0
		self.grid = np.array([])
		self.read()

		self.old_scores = []

	def read(self):
		with open("day18.txt", 'r') as f:
			self.size = len(f.readlines()[0]) - 1
			self.grid = np.chararray((self.size, self.size), unicode=True)
			self.grid[:] = 'X'

			f.seek(0)
			for y, line in enumerate(f):
				for x, c in enumerate(line.strip('\n')):
					self.grid[y, x] = c

	def run(self, n):
		repeat_flag = False
		first_repeat = 0
		repeat_index = 0

		for i in range(n):
			self.counter += 1
			self.step()
			#self.display()

			if not repeat_flag and self.calc_score() in self.old_scores:
				repeat_flag = True
				first_repeat = self.calc_score()
				repeat_index = self.counter
			elif repeat_flag and self.calc_score() == first_repeat:
				print("Loop found!", repeat_index, self.old_scores[repeat_index:])
				return self.old_scores[repeat_index:] + [self.calc_score()], repeat_index
			elif repeat_flag and self.calc_score() not in self.old_scores:
				repeat_flag = False

			self.old_scores.append(self.calc_score())

		print("After", n, "minutes, score =", self.calc_score())
		return [], 0

	def step(self):
		temp_grid = np.chararray((self.size, self.size), unicode=True)
		temp_grid[:] = 'X'
		for y in range(self.size):
			for x in range(self.size):
				L, R = x > 0, x < self.size - 1
				U, D = y > 0, y < self.size - 1
				sub_grid = self.grid[y-U:y+D+1, x-L:x+R+1]
				if self.grid[y, x] == '.':
					if (sub_grid == '|').sum() >= 3:
						temp_grid[y, x] = '|'
					else:
						temp_grid[y, x] = '.'
				elif self.grid[y, x] == '|':
					if (sub_grid == '#').sum() >= 3:
						temp_grid[y, x] = '#'
					else:
						temp_grid[y, x] = '|'
				else:
					if (sub_grid == '#').sum() >= 2 and (sub_grid == '|').sum() >= 1:
						temp_grid[y, x] = '#'
					else:
						temp_grid[y, x] = '.'

		self.grid = temp_grid

	def calc_score(self):
		return (self.grid == '#').sum() * (self.grid == '|').sum()

	def display(self):
		print(self.counter)
		print("\n".join(["".join([c for c in line]) for line in self.grid]))
		print()

time = 1000000000
land = Land()
land.display()
repeats, start_index = land.run(time)
if start_index:
	i = (time - start_index - 1) % len(repeats)
	print(repeats[i])
