def valid_count(triangles):
	return sum(t[0] + t[1] > t[2] for t in map(sorted, triangles))

def part_one():
	with open("day3.txt", "r") as f:
		triangles = [[int(line[i:i + 5].strip()) for i in range(0, 11, 5)] for line in f]
	print("PART ONE:", valid_count(triangles))


def part_two():
	with open("day3.txt", "r") as f:
		rows = [[int(line[i:i + 5].strip()) for i in range(0, 11, 5)] for line in f]

	columns = zip(*rows)
	triangles = [column[i:i+3] for column in columns for i in range(0, len(rows), 3)]
	print("PART TWO:", valid_count(triangles))



part_one()
part_two()