from parse import parse
import numpy as np
import matplotlib.pyplot as plt

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

def get_final_display(instructions):
	screen = np.zeros((6, 50))
	for command, A, B in instructions:
		if command == "rect":
			screen[:B, :A] = 1
		elif command == "column":
			screen[:, A] = np.roll(screen[:, A], B)
		elif command == "row":
			screen[A, :] = np.roll(screen[A, :], B)
	return screen

def part_one(screen):
	return np.count_nonzero(screen)

def part_two(screen):
	plt.imshow(screen)
	plt.show()


instructions = read_input()
screen = get_final_display(instructions)
print(part_one(screen))
part_two(screen)