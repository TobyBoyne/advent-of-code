from itertools import groupby

RANGE = (256310, 732736)

def any_repeats(N):
	has_double = False
	prev_d = '0'

	for d in N:
		if d < prev_d:
			return False
		if d == prev_d:
			has_double = True
		prev_d = d

	return has_double

def one_repeat(N):
	# len_repeats stores the number of times each digit in the number is repeated
	len_repeats = [len(list(group)) for _, group in groupby(N)]
	# True if in order and there is a group of length 2
	return 2 in len_repeats and sorted(N) == list(N)


def num_valid(valid_function):
	valid_count = 0
	for N in map(str, range(RANGE[0], RANGE[1] + 1)):
		valid_count += valid_function(N)

	return valid_count

print("Part one:", num_valid(valid_function=any_repeats))
print("Part two:", num_valid(valid_function=one_repeat))