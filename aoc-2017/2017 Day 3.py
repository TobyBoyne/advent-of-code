from math import sqrt, floor
from itertools import product as prod

puzz_input = 347991

# PART ONE
def get_coords(num):
	n = floor(sqrt(num))
	# find the x, y coordinates of the biggest square nearest to than num

	# if n is a square number
	if num == n ** 2:
		x = ((n - 1) // 2) * (2 * (n % 2) - 1)
		y = (n // 2) * (1 - 2 * (n % 2))
	# if n is closer to the lower square number
	elif num - n ** 2 < (n + 1) ** 2 - num:
		x = ((n - 1) // 2 + 1) * (2 * (n % 2) - 1)
		y = (n // 2 - (num - n**2 - 1)) * (1 - 2 * (n % 2))
	# if n is closer to the greater square number
	else:
		n += 1
		x = ((n - 1) // 2 - (n ** 2 - num)) * (2 * (n % 2) - 1)
		y = (n // 2) * (1 - 2 * (n % 2))

	return x, y

def dist(x, y):
	return abs(x) + abs(y)

print(dist(*get_coords(puzz_input)))

# PART TWO
# finds the number of the square at coordinates x, y
def get_num(x, y):
	# if the number is a square along the diagonal (including 1)
	if x == -y and x > 0:
		return ((2 * x) + 1) ** 2

	# if the num is along a horizontal part of spiral
	elif abs(x) < abs(y):
		n = abs(y) * 2
		if y < 0: n += 1
		next_square = n ** 2

		return next_square - abs(x - get_coords(next_square)[0])
	# if the num is along a vertical part of spiral
	else:
		n = abs(x) * 2
		if x > 0: n -= 1
		prev_square = n ** 2
		return prev_square + abs(y - get_coords(prev_square)[1]) + 1


grid = [0 for i in range(200)]
grid[0] = 1
DIR = ([-1, 0, 1], [-1, 0, 1])

for i in range(len(grid)):
	x, y = get_coords(i + 1)
	for dx, dy in prod(*DIR):
		index = get_num(x + dx, y + dy) - 1
		if 0 <= index < len(grid) and not dx == dy == 0:
			grid[i] += grid[index]

	if max(grid) > puzz_input:
		break

print(grid[:i])
print("First value over puzzle input =", max(grid))
