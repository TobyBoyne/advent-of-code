import re
from parse import parse

def read_input():
	with open("day09.txt") as f:
		string = f.read()
	return string

def decompress(string):
	# first get all markers in the string and their index
	# each marker stored as ((A, B), (start, end)) where marker is (AxB)
	markers = []
	marker_pattern = r"\([0-9|x]*\)"
	for m in re.finditer(marker_pattern, string):
		p = parse("({:d}x{:d})", m.group())
		idx = (m.start(), m.end())
		markers.append((*p.fixed, *idx))

	new_string = ""
	prev_end = 0
	for A, B, start, end in markers:
		if prev_end <= start:
			new_string += string[prev_end:start]
			repeat_group = string[end:end+A]
			new_string += repeat_group * B
			prev_end = end + A
	new_string += string[prev_end:]
	return new_string

def part_one(string):
	return len(decompress(string))

string = read_input()
print(part_one(string))