def dragon(a):
	b = a[::-1]
	b_inv = "".join('0' if c=='1' else '1' for c in b)
	return a + '0' + b_inv


def grouper(it):
	args = [iter(it)] * 2
	return zip(*args)

def checksum(data):
	if len(data) % 2 == 1:
		return data
	else:
		return checksum("".join('1' if a==b else '0' for (a, b) in grouper(data)))

def part_one(initial_state, disk_size):
	data = initial_state
	while len(data) < disk_size:
		data = dragon(data)


	data = data[:disk_size]
	return checksum(data)

puzz_input = "01110110101001000"
print(part_one(puzz_input, 272))
print(part_one(puzz_input, 35651584))