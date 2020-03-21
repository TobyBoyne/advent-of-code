from itertools import product

HALT = 99

def read_file():
	with open("day2.txt") as f:
		program = [int(x) for x in f.read().split(",")]

	return program

def part_one(intcode, noun=12, verb=2):
	intcode[1] = noun
	intcode[2] = verb

	pos = 0
	while intcode[pos] != HALT:
		addr1, addr2, store = intcode[pos+1:pos+4]
		a, b = intcode[addr1], intcode[addr2]
		if intcode[pos] == 1:
			intcode[store] = a + b
		elif intcode[pos] == 2:
			intcode[store] = a * b
		pos += 4

	return intcode

program = read_file()
print(part_one(list(program)))

# Part two:
TARGET = 19690720
for a, b in product(range(100), repeat=2):
	output = part_one(list(program), noun=a, verb=b)
	if output[0] == TARGET:
		print("Part two:", 100 * a + b)