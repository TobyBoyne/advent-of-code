def read_input():
	with open("day12.txt") as f:
		instructions = []
		for line in f:
			op, *values = line.strip("\n").split()
			instructions.append((op, *values))
	return instructions

def as_value(registers, value):
	# converts value to either integer or register value
	try:
		out = int(value)
	except ValueError:
		out = registers[value]
	return out


def run_instructions(instructions, initial_c=0):
	registers = {r: 0 for r in 'abcd'}
	registers['c'] = initial_c
	i = 0
	while i < len(instructions):
		op, x, *y = instructions[i]
		if op in ('inc', 'dec'):
			registers[x] += 1 if op == 'inc' else -1
		else:
			x = as_value(registers, x)
			y = y[0]

			if op == 'cpy':
				registers[y] = x
			elif op == 'jnz':
				y = as_value(registers, y)
				i += y if x != 0 else 1
				i -= 1
		i += 1
		print(registers)
	return registers

def part_one(instructions):
	return run_instructions(instructions)['a']

def part_two_slow(instructions):
	return run_instructions(instructions, initial_c=1)['a']

instructions = read_input()
print(part_one(instructions))
