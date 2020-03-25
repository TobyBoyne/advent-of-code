def read_file():
	with open("day08.txt") as f:
		return [line.strip("\n") for line in f]


def len_diff(s):
	escapes = s.count('\\\\')
	s = s.replace('\\\\', ' ')
	escapes += s.count('\\"') + s.count('\\x') * 3
	return 2 + escapes

def part_one(strings):
	return sum(len_diff(s) for s in strings)


strings = read_file()
print(part_one(strings))