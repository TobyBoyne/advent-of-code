with open("day5.txt", 'r') as f:
	jumps = [int(line.strip("\n")) for line in f]


def part_one():
	cur = 0
	count = 0
	while 0 <= cur <= len(jumps) - 1:
		temp = jumps[cur]
		jumps[cur] += 1
		cur += temp
		count += 1

	print(count)

def part_two():
	cur = 0
	count = 0
	while 0 <= cur <= len(jumps) - 1:
		temp = jumps[cur]
		if temp >= 3:
			jumps[cur] -= 1
		else:
			jumps[cur] += 1
		cur += temp
		count += 1

	print(count)

part_two()