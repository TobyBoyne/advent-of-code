from itertools import groupby

def S(n):
	return "".join([str(len(list(g))) + k for k, g in groupby(n)])

def part_one(n):
	for i in range(40):
		n = S(n)

	return len(n)

def part_two(n):
	for i in range(50):
		n = S(n)

	return len(n)

puzz_input = "1113122113"
print(part_one(puzz_input))
print(part_two(puzz_input))