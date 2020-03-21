DIRECTIONS = {
	'n':	(0, 1),
	'ne':	(1, 0.5),
	'nw':	(-1, 0.5),
	's':	(0, -1),
	'se':	(1, -0.5),
	'sw':	(-1, -0.5),
}

x, y = 0, 0
greatest_dist = 0

def distance(x, y):
	x, y = abs(x), abs(y)
	d = x
	if x / 2 <= y:
		y -= x / 2
		d += y
	return int(d)

with open("day11.txt", 'r') as f:
	moves = f.read().strip("\n").split(",")
	for move in moves:
		dx, dy = DIRECTIONS[move]
		x += dx
		y += dy
		if greatest_dist < distance(x, y):
			greatest_dist = distance(x, y)

print("Part one:", distance(x, y))
print("Part two:", greatest_dist)