def read_input():
	strings = []
	with open("day05.txt") as f:
		for line in f:
			strings.append(line.strip("\n"))

	return strings

def nice_string1(s):
	vowel_count = 0
	letter_repeat = False
	for i, c in enumerate(s):
		vowel_count += c in 'aeiou'
		pair = s[i:i+2]
		if len(pair) == 2 and pair[0] == pair[1]:
			letter_repeat = True
		if pair in ('ab', 'cd', 'pq', 'xy'):
			return False

	return vowel_count >= 3 and letter_repeat

def nice_string2(s):
	pairs = {}
	repeated_pair = False
	sandwich = False
	for i, c in enumerate(s):
		if i < len(s) - 2 and s[i + 2] == c:
			sandwich = True
		p = s[i:i+2]
		if p in pairs:
			if pairs[p] < i - 1:
				repeated_pair = True
		else:
			pairs[p] = i

	return repeated_pair and sandwich


def part_one(strings):
	return sum(nice_string1(s) for s in strings)

def part_two(strings):
	return sum(nice_string2(s) for s in strings)

strings = read_input()
print(part_one(strings))
print(part_two(strings))