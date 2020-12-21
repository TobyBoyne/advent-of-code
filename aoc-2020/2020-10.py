with open('day10.txt') as f:
	adaptors = list(sorted(int(l.rstrip()) for l in f.readlines()))
	adaptors_set = set([0] + adaptors)


def part_one():
	adaptors_inc_ends = [0] + adaptors + [max(adaptors) + 3]
	diffs = {i: 0 for i in (1, 2, 3)}
	for prev_ad, ad in zip(adaptors_inc_ends, adaptors_inc_ends[1:]):
		diffs[ad - prev_ad] += 1
	return diffs[1] * diffs[3]





def part_two():
	end = max(adaptors) + 3
	cache = {}
	def num_ways_to_reach(n):
		if n == 0: return 1
		total = 0
		for m in (n - 1, n - 2, n - 3):
			if m in adaptors_set:
				if m in cache:
					num_ways = cache[m]
				else:
					num_ways = num_ways_to_reach(m)
					cache[m] = num_ways
				total += num_ways

		return total
	return num_ways_to_reach(end)



print('Part one', part_one())
print('Part two', part_two())
