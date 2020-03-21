from time import perf_counter

puzz_input = (703, 516)

factor_a = 16807
factor_b = 48271

DIV = 2147483647

t = perf_counter()

def A1(a0, num_pairs):
	value = a0
	for i in range(num_pairs):
		yield value
		value = (value * 16807) % DIV
def B1(b0, num_pairs):
	value = b0
	for i in range(num_pairs):
		yield value
		value = (value * 48271) % DIV

def part_one(a0, b0, num_pairs):
	judge_count = 0
	for (a, b) in zip(A1(a0, int(num_pairs)), B1(b0, int(num_pairs))):
		judge_count += a & 0b1111111111111111 == b & 0b1111111111111111
	return judge_count



def A2(a0, num_pairs):
	value = a0
	count = 0
	while count < num_pairs:
		if not value % 4:
			yield value
			count += 1
		value = (value * 16807) % DIV

		if not count % 100000:
			print(100 * count / num_pairs, "% done")

def B2(b0, num_pairs):
	value = b0
	count = 0
	while count < num_pairs:
		if not value % 8:
			yield value
			count += 1
		value = (value * 48271) % DIV

def part_two(a0, b0, num_pairs):
	judge_count = 0
	for (a, b) in zip(A2(a0, int(num_pairs)), B2(b0, int(num_pairs))):
		judge_count += a & 0b1111111111111111 == b & 0b1111111111111111
	return judge_count


#print("Part one:", part_one(*puzz_input, int(4e7))
print("Part two:", part_two(*puzz_input, int(5e6)))
print("TIME:", perf_counter() - t)
