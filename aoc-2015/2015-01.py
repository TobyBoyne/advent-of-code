def read_input():
	with open("day01.txt") as f:
		puzz_input = f.read().strip("\n")

	return puzz_input

def part_one(s):
	return s.count("(") - s.count(")")

def part_two(s):
	floor = 0
	for idx, c in enumerate(s):
		floor += 1 if c == "(" else -1
		if floor == -1:
			break

	return idx + 1

puzz_input = read_input()
print(part_one(puzz_input))
print(part_two(puzz_input))