def read_input():
	with open("day01.txt") as f:
		puzz_input = f.read().strip("\n")

	return puzz_input

def part_one(s):
	return s.count("(") - s.count(")")

puzz_input = read_input()
print(part_one(puzz_input))