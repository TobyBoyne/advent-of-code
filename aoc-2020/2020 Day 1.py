from itertools import combinations

with open('day1.txt') as f:
	entries = [int(l.rstrip()) for l in f.readlines()]


def part_one():
	for ent in entries:
		if 2020 - ent in entries:
			return ent * (2020 - ent)

def part_two():
	pair_sums = {a+b: (a, b) for a, b in combinations(entries, r=2)}
	for ent in entries:
		if (r := (2020 - ent)) in pair_sums:
			return ent * pair_sums[r][0] * pair_sums[r][1]


print('Part one', part_one())
print('Part two', part_two())