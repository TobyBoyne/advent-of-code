from parse import compile

pat = compile('{ct_min:d}-{ct_max:d} {letter}: {pword}')
with open('day02.txt') as f:
	passwords = [pat.parse(l.rstrip()) for l in f.readlines()]

def part_one():
	valid_count = 0
	for p in passwords:
		if p['ct_min'] <= p['pword'].count(p['letter']) <= p['ct_max']:
			valid_count += 1

	return valid_count


def part_two():
	valid_count = 0
	for p in passwords:
		letters = p['pword'][p['ct_min'] - 1] + p['pword'][p['ct_max'] - 1]
		if letters.count(p['letter']) == 1:
			valid_count += 1

	return valid_count

print('Part one', part_one())
print('Part two', part_two())