from parse import parse
from itertools import tee

def read_input():
	ip_ranges = []
	with open("day20.txt") as f:
		for line in f:
			p = parse("{:d}-{:d}", line.strip("\n"))
			ip_ranges.append(p.fixed)
	return list(sorted(ip_ranges))

def pairwise(iterable):
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)


def merge_overlaps(ip_ranges):
	merged_ranges = []
	cur_range = []
	for r in ip_ranges:
		if cur_range:
			if r[0] <= cur_range[1] + 1:
				cur_range[1] = max(r[1], cur_range[1])
			else:
				merged_ranges.append(cur_range)
				cur_range = list(r)
		else:
			cur_range = list(r)
	merged_ranges.append(cur_range)
	return merged_ranges

def part_one(ip_ranges):
	merged_ranges = merge_overlaps(ip_ranges)
	# return first item outside of the first merged range (i.e. first item not covered by any original range)
	return merged_ranges[0][1] + 1

def part_two(ip_ranges):
	merged_ranges = merge_overlaps(ip_ranges)
	num_allowed = merged_ranges[0][0]
	for r1, r2 in pairwise(merged_ranges):
		num_allowed += r2[0] - r1[1] - 1
	return num_allowed


ip_ranges = read_input()
print(part_one(ip_ranges))
print(part_two(ip_ranges))