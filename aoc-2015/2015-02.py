def read_input():
	lengths = []
	with open("day02.txt") as f:
		for line in f:
			dimensions = [int(l) for l in sorted(line.strip("\n").split("x"))]
			lengths.append(sorted(dimensions))

	return lengths

def area(dimensions):
	l, w, h = dimensions
	return 3 * l * w + 2 * w * h + 2 * l * h

def ribbon(dimensions):
	l, w, h = dimensions
	return 2 * (l + w) + l * w * h


def part_one(lengths):
	return sum(area(l) for l in lengths)

def part_two(lengths):
	return sum(ribbon(l) for l in lengths)


lengths = read_input()
print(part_one(lengths))
print(part_two(lengths))