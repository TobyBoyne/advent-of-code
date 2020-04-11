import re
from json import loads

def read_input():
	with open("day12.txt") as f:
		return f.read()


def part_one(string):
	all_nums = re.findall(r'-?\d+', string)
	return sum(map(int, all_nums))


def hook(obj):
	if "red" in obj.values():
		return {}
	else:
		return obj

def part_two(string):
	as_json = str(loads(string, object_hook=hook))
	return part_one(as_json)

string = read_input()
print(part_one(string))
print(part_two(string))