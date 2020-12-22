import numpy as np

with open('day13.txt') as f:
	earliest_timestamp = int(f.readline().rstrip())
	bus_ids = f.readline().rstrip().split(',')

def part_one():
	running_bus_ids = [int(bus) for bus in bus_ids if bus != 'x']
	# return min(bus - earliest_timestamp % bus for bus in running_bus_ids)
	min_wait = min([(bus, bus - earliest_timestamp % bus) for bus in running_bus_ids], key=lambda x: x[1])
	return min_wait[0] * min_wait[1]

def part_two():
	# t === bus_id - idx (mod bus_id)
	# note that all bus_ids are prime
	# use Chinese Remainder Theorem, m is all coprime
	# https://math.stackexchange.com/questions/1346511/system-of-modular-equations
	bus_info = np.array([[idx, int(bus)] for idx, bus in enumerate(bus_ids) if bus != 'x'], dtype=int)
	m = bus_info[:, 1]
	b = (bus_info[:, 1] - bus_info[:, 0]) % m
	M = 1
	for m_i in m:
		# use int() to prevent overflow
		M *= int(m_i)
	n = M // m
	# get multiplicative inverse
	n_bar = np.array([pow(int(n[i]), -1, int(m[i])) for i in range(len(n))])
	t = (b * n * n_bar).sum()
	return t % M

print('Part one', part_one())
print('Part two', part_two())