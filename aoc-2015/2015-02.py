def read_input():
	lengths = []
	with open("day02.txt") as f:
		for line in f:
			lengths.append((int(l) for l in line.strip("\n").split("x")))

	return lengths

def area(dimensions):
	l, w, h = sorted(dimensions)
	return 3 * l * w + 2 * w * h + 2 * l * h

def part_one(lengths):
	return sum(area(l) for l in lengths)



lengths = read_input()
print(part_one(lengths))
