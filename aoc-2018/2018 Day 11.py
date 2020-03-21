from math import inf
import numpy as np


def calc_fuel(x, y, serial):
	rack_ID = x + 10
	f = rack_ID * y
	f += serial
	f *= rack_ID
	# returns 100s digit
	f = (f % 1000) // 100
	f -= 5
	return f

def square_sum(left_x, top_y, r):
	return sum([cells[left_x + i, top_y + j] for i in range(r) for j in range(r)])

def find_greatest():
	max_coord = (0, 0)
	max_sum = -inf
	max_square_size = 0
	for square_size in range(1, 300):
		print(str(max_coord[1]) + "," + str(max_coord[0]) + "," + str(square_size - 1))
		for x in range(size - square_size + 1):
			for y in range(size - square_size + 1):
				this_sum = square_sum(x, y, square_size)
				if this_sum > max_sum:
					max_sum = this_sum
					max_coord = (x + 1, y + 1)
					max_square_size = square_size
	return max_coord, max_sum, max_square_size

"""
class Grid:
	def __init__(self, size, serial):
		self.size = size
		self.serial = serial
		self.cells = [[Cell(i + 1, j + 1, serial) for i in range(size)] for j in range(size)]
	def square_sum(self, left_x, top_y, r):
		return sum([self.cells[top_y + j][left_x + i].fuel for i in range(r) for j in range(r)])
	def find_greatest(self):
		max_coord = (0, 0)
		max_sum = -inf
		max_square_size = 0
		for square_size in range(1, 300):
			print(square_size)
			for x in range(self.size - square_size + 1):
				for y in range(self.size - square_size + 1):
					square_sum = self.square_sum(x, y, square_size)
					if square_sum > max_sum:
						max_sum = square_sum
						max_coord = (x + 1, y + 1)
						max_square_size = square_size
		print(max_coord, max_sum, max_square_size)"""

serial = 7672
size = 300
cells = np.array([[calc_fuel(x + 1, y + 1, serial) for x in range(size)] for y in range(size)])
print(find_greatest())
