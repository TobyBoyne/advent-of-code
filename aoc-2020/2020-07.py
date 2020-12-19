from parse import parse

bags = {}
with open('day07.txt') as f:
	for line in f.readlines():
		container, contains = parse('{} bags contain {}.', line.rstrip()).fixed
		bags[container] = {}
		if contains != 'no other bags':
			for bag in contains.split(', '):
				count, bag_colour, _ = parse('{:d} {} ba{}', bag)
				bags[container][bag_colour] = count


def part_one():
	target = 'shiny gold'
	outer = [target]
	contains_target = set()
	while outer:
		prev_outer = outer
		outer = []
		for b in prev_outer:
			for container, contents in bags.items():
				if b in contents:
					outer.append(container)
					contains_target.add(container)

	return len(contains_target)


def get_num_bags_within(bag):
	total_bags_within = 0
	for inner, count in bags[bag].items():
		total_bags_within += count * (1 + get_num_bags_within(inner))
	return total_bags_within

def part_two():
	return get_num_bags_within('shiny gold')




print('Part one', part_one())
print('Part two', part_two())
