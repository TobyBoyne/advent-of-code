import re

def read_input():
	with open("day12.txt") as f:
		return f.read()


def part_one(json):
	all_nums = re.findall(r'-?[0-9]+(?![0-9])', json)
	return sum(map(int, all_nums))


json = read_input()
print(part_one(json))