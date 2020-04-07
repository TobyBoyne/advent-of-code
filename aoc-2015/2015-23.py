def read_input():
	instructions = []
	with open("day23.txt") as f:
		for line in f:
			op, *args = line.strip("\n").replace(',', '').split()
			instructions.append((op, args))
	return instructions

def run(instructions, initial_registers):
	i = 0
	registers = initial_registers
	while 0 <= i < len(instructions):
		op, args = instructions[i]
		if op == 'hlf':
			registers[args[0]] /= 2
		elif op == 'tpl':
			registers[args[0]] *= 3
		elif op == 'inc':
			registers[args[0]] += 1
		elif op == 'jmp':
			i += int(args[0]) - 1
		elif op == 'jie':
			if registers[args[0]] % 2 == 0:
				i += int(args[1]) - 1
		elif op == 'jio':
			if registers[args[0]] == 1:
				i += int(args[1]) - 1

		i += 1
	return registers

def part_one(instructions):
	registers = run(instructions, {'a': 0, 'b': 0})
	return registers['b']

def part_two(instructions):
	registers = run(instructions, {'a': 1, 'b': 0})
	return registers['b']


instructions = read_input()
print(part_one(instructions))
print(part_two(instructions))