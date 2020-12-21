from parse import parse

with open('day08.txt') as f:
	instrs = [parse('{} {:d}', l.rstrip()).fixed for l in f.readlines()]


def run(instructions):
	instr_count = [0 for _ in instructions] + [0]
	next_instr_idx = 0
	acc = 0
	while instr_count[next_instr_idx] < 1:
		if next_instr_idx == len(instructions):
			return acc, True
		instr_count[next_instr_idx] += 1
		opcode, arg = instructions[next_instr_idx]
		if opcode == 'acc':
			acc += arg
		elif opcode == 'jmp':
			next_instr_idx += arg - 1

		next_instr_idx += 1

	return acc, False


def part_one():
	return run(instrs)[0]

def part_two():
	nop_jmp_idxs = [i for i, (opcode, _) in enumerate(instrs) if opcode in ('jmp', 'nop')]
	switch = {'jmp': 'nop', 'nop': 'jmp'}
	for switch_idx in nop_jmp_idxs:
		instructions = [(switch[opcode] if i == switch_idx else opcode, arg) for i, (opcode, arg) in enumerate(instrs)]
		acc, terminate = run(instructions)
		if terminate:
			return acc
	print(nop_jmp_idxs)


print('Part one', part_one())
print('Part two', part_two())