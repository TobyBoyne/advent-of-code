with open('day03.txt') as f:
	tree_map = [[1 if c=='#' else 0 for c in l.rstrip()] for l in f.readlines()]

def count_trees(dx, dy):
	x, y = 0, 0

	tree_count = 0
	while y < len(tree_map):
		tree_count += tree_map[y][x % len(tree_map[0])]
		x += dx
		y += dy

	return tree_count

def part_two():
	slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
	prod = 1
	for (dx, dy) in slopes:
		prod *= count_trees(dx, dy)

	return prod


print('Part one', count_trees(3, 1))
print('Part two', part_two())