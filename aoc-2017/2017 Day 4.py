from collections import Counter

# PART ONE
valid_count = 0
with open("day4.txt", 'r') as f:
	for line in f:
		words = line.strip("\n").split()
		# if the count of the most common word is greater than 1, then there is at least 1 repeat
		if Counter(words).most_common()[0][1] < 2:
			valid_count += 1

print("Part one:", valid_count)


# PART TWO
valid_count = 0
with open("day4.txt", 'r') as f:
	for line in f:
		words = line.strip("\n").split()
		sorted_words = ["".join(sorted(word)) for word in words]
		if Counter(sorted_words).most_common()[0][1] < 2:
			valid_count += 1

print("Part two:", valid_count)