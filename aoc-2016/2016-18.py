import numpy as np

def read_input():
	with open("day18.txt") as f:
		line = f.read().strip("\n")

	return np.array([c == '^' for c in line])


def next_line(prev_line):
	next_row = np.zeros_like(prev_line)
	for i in range(1, len(next_row) - 1):
		# centre trap has no effect - return left XOR right
		left, right = prev_line[i - 1], prev_line[i + 1]
		next_row[i] = left != right
	return next_row

def part_one(first_row, n=40):
	grid = np.zeros((n, len(first_row) + 2))
	cur_row = np.concatenate(([False], first_row, [False]))
	for i in range(n):
		grid[i, :] = cur_row
		cur_row = next_line(cur_row)
	return np.count_nonzero(grid[:, 1:-1] == False)


first_row = read_input()
print(part_one(first_row))