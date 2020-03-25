def read_file():
	with open("day08.txt") as f:
		return [line.strip("\n") for line in f]


def literal_len_diff(s):
	escapes = s.count('\\\\')
	s = s.replace('\\\\', ' ')
	escapes += s.count('\\"') + s.count('\\x') * 3
	# +2 for the quote at the beginning/end
	return escapes + 2

def encoded_len_diff(s):
	new_slashes = s.count('\\') + s[1:-1].count('"')
	# +4 for quote at beginning/end
	return new_slashes + 4


def part_one(strings):
	return sum(literal_len_diff(s) for s in strings)

def part_two(strings):
	return sum(encoded_len_diff(s) for s in strings)


strings = read_file()
print(part_one(strings))
print(part_two(strings))