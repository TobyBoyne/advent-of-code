from parse import parse
import numpy as np

def read_input():
	with open("day08.txt") as f:
		instr = []
		for line in f:
			if "rect" in line:
				p = parse("rect {:d}x{:d}", line.strip("\n"))
				A, B = p.fixed
				instr.append(('rect', A, B))
			else:
				p = parse("rotate {} {}={:d} by {:d}", line.strip("\n"))
				row_or_column, _, A, B = p.fixed
				instr.append((row_or_column, A, B))

	return instr

def part_one(instructions):
	screen = np.zeros((6, 50))
	for command, A, B in instructions:
		if command == "rect":
			screen[:B, :A] = 1
		elif command == "column":
			screen[:, A] = np.roll(screen[:, A], B)
		elif command == "row":
			screen[A, :] = np.roll(screen[A, :], B)
	return np.count_nonzero(screen)


instructions = read_input()
print(part_one(instructions))