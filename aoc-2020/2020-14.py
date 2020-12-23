from parse import parse
from itertools import product

instructions = []
with open('day14.txt') as f:
	for l in f.readlines():
		if 'mask' in l:
			instructions.append(parse('{} {} {}', l.rstrip()).fixed)
		else:
			instructions.append(parse('{}[{:d}] = {:d}', l.rstrip()).fixed)

def part_one():
	set_zeros = 0
	set_ones = 0
	memory = {}
	for cmd, idx, value in instructions:
		if cmd == 'mask':
			set_zeros = int(''.join('0' if c == '0' else '1' for c in value), 2)
			set_ones = int(''.join('1' if c == '1' else '0' for c in value), 2)
		else:
			memory[idx] = (value & set_zeros) | set_ones
	return sum(memory.values())

def part_two():
	set_ones = 0
	x_vals = []
	memory = {}
	for cmd, idx, value in instructions:
		if cmd == 'mask':
			set_ones = int(''.join('1' if c == '1' else '0' for c in value), 2)
			x_vals = [2 ** (35 - i) for i, c in enumerate(value) if c == 'X']
		else:
			address = idx | set_ones
			for fl in product((0, 1), repeat=len(x_vals)):
				float_mask = sum(a * b for a, b in zip(fl, x_vals))
				memory[address ^ float_mask] = value

	return sum(memory.values())


print('Part one', part_one())
print('Part two', part_two())
