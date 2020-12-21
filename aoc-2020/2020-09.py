with open('day09.txt') as f:
	seq = [int(l.rstrip()) for l in f.readlines()]

def part_one():
	for i in range(25, len(seq) - 1):
		prev_nums = seq[i-25:i]
		for n in prev_nums:
			if seq[i] - n in prev_nums:
				break
		else: #nobreak
			return seq[i]

def part_two():
	invalid = 14360655
	for i in range(len(seq) - 1):
		total = 0
		for j in range(i, len(seq) - 1):
			total += seq[j]
			if total == invalid:
				return min(seq[i:j+1]) + max(seq[i:j+1])
			elif total > invalid:
				break

print('Part one', part_one())
print('Part two', part_two())