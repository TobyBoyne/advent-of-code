import numpy as np
hashes = __import__("2017 Day 10")
puzz_input = "ugkiagan"

DIRECTIONS = [
	(1, 0),
	(-1, 0),
	(0, 1),
	(0, -1)
]

grid = np.full((128, 128), 1)

for n in range(128):
	key_string = puzz_input + '-' + str(n)
	lengths = [ord(c) for c in key_string] + hashes.SUFFIX
	hash_string = hashes.dense_hash(hashes.knot_hash(lengths, 64))
	hex_values = [int(x, 16) for x in hash_string]
	bin_values = "".join(bin(x)[2:].rjust(4, '0') for x in hex_values)

	for i, c in enumerate(bin_values):
		grid[n, i] = int(c)

def print_grid():
	[print("".join(map(str, grid[y]))) for y in range(len(grid))]

def regions():
	r_number = 2
	for y in range(len(grid)):
		for x in range(len(grid)):
			if grid[y, x] == 1:
				fill_region(x, y, r_number)
				r_number += 1
	return r_number - 2

def fill_region(x0, y0, region):
	to_check = [(y0, x0)]
	grid[y0, x0] = region
	while to_check:
		new_to_check = []
		for (y, x) in to_check:
			for d in DIRECTIONS:
				coord = y + d[1], x + d[0]
				if all(0 <= c < len(grid) for c in coord) and grid[coord] == 1:
					grid[coord] = region
					new_to_check.append(coord)

		to_check = new_to_check


print_grid()
print("Part one:", sum(sum(grid)))
print("Part two:", regions())

