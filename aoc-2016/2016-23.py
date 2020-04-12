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


def run_instructions(instructions, initial_reg):
	registers = initial_reg
	i = 0
	while i < len(instructions):
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


instructions = read_input()
print(part_one(instructions))
