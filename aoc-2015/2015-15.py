import numpy as np
from parse import parse

x = np.array([
	[1, 2],
	[3, 4]
])

y = np.array([5, 6])
print(x * y)
print(x.dot(y))


a = np.array([1, 1, 1])
b = np.array([
	[1, 2],
	[3, 4],
	[5, 6]
])
print(a.dot(b))

def read_input():
	with open("day15.txt") as f:
		lines = f.readlines()
		N = len(lines)
		ingr_values = np.zeros((5, N))
		for line in lines:
			p = parse("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}",
					  line.strip("\n"))



def part_one(ingr_values):
	"""Using Matrix algebra
	M . [a1, a2, ..., an] = [cap, dur, flav, texture], where a is the number of teaspoons
	To get the total score, [1, 1, 1, 1]T . [cap, dur, flav, texture]
	Therefore [1, 1, 1, 1]T .M . [a1, a2, ..., an] = total score
	Then apply constraint that a1 = 100 - (a2 + ... + an)"""

	# find constraints as all sum values must be positive
	