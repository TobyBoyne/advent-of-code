
S = open("day9.txt", 'r').read()

i = 0
garbage_count = 0

def score(bonus=0):
	global i
	global garbage_count

	garbage = False
	my_score = 0
	while i < len(S):
		if not garbage:
			if S[i] == '{':
				i += 1
				my_score += score(bonus+1)
			elif S[i] == '}':
				return my_score + bonus
			elif S[i] == '!':
				i += 1
			elif S[i] == '<':
				garbage = True
		else:
			if S[i] == '!':
				i += 1
			elif S[i] == '>':
				garbage = False
			else:
				garbage_count += 1

		i += 1
	return my_score

print("Part one:", score())
print("Part two:", garbage_count)