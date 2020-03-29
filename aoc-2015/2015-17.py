def read_input():
	containers = []
	with open("day17.txt") as f:
		for line in f:
			containers.append(int(line.strip("\n")))
	return containers

#  --- INITIAL SOLUTION ---
# def num_combinations(containers, L):
# 	# containers must be sorted
# 	if L == 0:
# 		return 1
# 	total = 0
# 	for i, c in enumerate(containers):
# 		if c <= L:
# 			remaining = containers[:i]
# 			total += num_combinations(remaining, L - c)
#
# 	return total

def find_all_combinations(containers, used, L):
	# containers must be sorted
	combinations = []
	for i, c in enumerate(containers):
		if c == L:
			combinations.append(used + [c])
		if c <= L:
			remaining = containers[:i]
			combinations += find_all_combinations(remaining, used + [c], L - c)

	return combinations


def part_one(combinations):
	return len(combinations)

def part_two(combinations):
	lengths = [len(comb) for comb in combinations]
	min_length = min(lengths)
	return sum(l==min_length for l in lengths)


containers = read_input()
combinations = find_all_combinations(containers, [], 150)
print(part_one(combinations))
print(part_two(combinations))