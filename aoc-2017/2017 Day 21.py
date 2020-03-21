import numpy as np
from itertools import product
from time import perf_counter

def read_file():
	rules2, rules3 = {}, {}
	with open("day21.txt", 'r') as f:
		for line in f:
			inp, out = line.strip("\n").split(" => ")
			if len(inp) == 5:
				rules2[inp] = out
			else:
				rules3[inp] = out

	return rules2, rules3


def iterate(image, rules):
	if len(image) % 2 == 0:
		sub_size = 2
		scale_factor = 3 / 2
	else:
		sub_size = 3
		scale_factor = 4 / 3

	new_size = int(len(image) * scale_factor)
	new_sub_size = int(sub_size * scale_factor)
	new_image = np.full((new_size, new_size), '')

	for (x, y) in product(range(0, len(image), sub_size), repeat=2):
		sub = image[y:y+sub_size, x:x+sub_size]

		for rot in range(12):
			# all possible flips and rotations
			if rot == 4:
				sub = np.fliplr(sub)
			if rot == 8:
				sub = np.fliplr(sub)
				sub = np.flipud(sub)
			rot_sub = np.rot90(sub, rot)
			sub_string = "/".join("".join(rot_sub[i]) for i in range(len(rot_sub)))
			if sub_string in rules:
				new_sub_string = rules[sub_string]
				break
		else:
			raise ValueError("Could not find sub-array in rules")

		new_sub = np.array([list(line) for line in new_sub_string.split('/')])
		x_n, y_n = int(x * scale_factor), int(y * scale_factor)

		new_image[y_n:y_n+new_sub_size, x_n:x_n+new_sub_size] = new_sub

	return new_image



image = np.array([
	['.', '#', '.'],
	['.', '.', '#'],
	['#', '#', '#']
])

rules2, rules3 = read_file()
all_rules = {**rules2, **rules3}

t = perf_counter()
for i in range(18):
	image = iterate(image, all_rules)
	if i == 4: print("Part one:", sum(sum(image == '#')))

print("Part two:", sum(sum(image == '#')))
print(perf_counter() - t)