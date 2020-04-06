def next_code(prev_code):
	return (prev_code * 252533) % 33554393

def part_one(code, r, c):
	# (row + column - 2)th triangle number + column
	n = (1 / 2) * (r + c - 2) * (r + c - 1) + c
	for i in range(int(n) - 1):
		code = next_code(code)
	print(code)

initial_code = 20151125
row, column = 2981, 3075
print(part_one(initial_code, row, column))