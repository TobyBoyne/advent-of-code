puzz_input = 380

def after_n(n):
	buffer = []
	cur = 0
	for i in range(n + 1):
		buffer.insert(cur, i)
		cur += puzz_input + 1
		cur %= len(buffer)

	i = buffer.index(n)
	print(buffer)
	return buffer[i + 1]

def after_zero(count):
	cur = 0
	buffer_len = 0
	max_value = 0
	for i in range(count):
		buffer_len += 1
		cur = (cur + puzz_input + 1) % buffer_len
		if cur == 0:
			max_value = i + 1

	return max_value



print("Part one:", after_n(2017))

print("Part two:", after_zero(50000000))