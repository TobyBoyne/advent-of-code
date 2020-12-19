with open('day06.txt') as f:
	all_answers = [group.split('\n') for group in f.read().split('\n\n')]

def part_one():
	total_counts = 0
	for group in all_answers:
		ans_set = set()
		for person in group:
			ans_set = ans_set.union(set(person))
		total_counts += len(ans_set)

	return total_counts

def part_two():
	total_counts = 0
	for group in all_answers:
		ans_set = set(group[0])
		for person in group:
			ans_set = ans_set.intersection(set(person))
		total_counts += len(ans_set)

	return total_counts


print('Part one', part_one())
print('Part two', part_two())