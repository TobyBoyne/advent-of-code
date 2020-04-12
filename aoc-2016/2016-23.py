from math import factorial

toggle = {
	'inc': 'dec',
	'dec': 'inc',
	'tgl': 'inc',
	'cpy': 'jnz',
	'jnz': 'cpy'
}

def read_input():
	with open("day23.txt") as f:
		instructions = []
		for line in f:
			op, *values = line.strip("\n").split()
			instructions.append([op, *values])
	return instructions

def as_value(registers, value):
	# converts value to either integer or register value
	try:
		out = int(value)
	except ValueError:
		out = registers[value]
	return out


def run_instructions(instructions, initial_reg, print_at_zero=False):
	registers = initial_reg
	i = 0
	while i < len(instructions):
		if print_at_zero and i == 9 and registers['d'] == 0 and registers['a'] and registers['b'] > 1:
			registers['b'] -= 1
			registers['a'] *= registers['b']
			print(i, registers)
			continue
		op, x, *y = instructions[i]
		if op == 'tgl':
			x = as_value(registers, x)
			if 0 <= i + x < len(instructions):
				instructions[i+x][0] = toggle[instructions[i+x][0]]

		elif op in ('inc', 'dec'):
			registers[x] += 1 if op == 'inc' else -1
		else:
			x = as_value(registers, x)
			y = y[0]

			if op == 'cpy':
				if y in 'abcd':
					registers[y] = x
			elif op == 'jnz':
				y = as_value(registers, y)
				i += y if x != 0 else 1
				i -= 1
		i += 1
	return registers

def part_one(instructions):
	initial_reg = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
	return run_instructions(instructions, initial_reg)['a']

def part_two_slow(instructions):
	"""Too slow to find answer. Shows that each time d = 0, a = a * b, and b decreases by one
	Therefore finds 12!
	To find the extra constant, just use part_one - 7!
	constant = 12703 - 5040"""
	initial_reg = {'a':12, 'b':0, 'c':0, 'd':0}
	return run_instructions(instructions, initial_reg, print_at_zero=True)

def part_two():
	return factorial(12) + 7663

instructions = read_input()
print(part_one(instructions))
# print(part_two_slow(instructions))
print(part_two())