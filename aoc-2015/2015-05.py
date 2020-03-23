def read_input():
	strings = []
	with open("day05.txt") as f:
		for line in f:
			strings.append(line.strip("\n"))

	return strings

def nice_string(s):
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

def part_one(strings):
	return sum(nice_string(s) for s in strings)

strings = read_input()
print(part_one(strings))