starting = [20,9,11,0,1,2]
starting = [20,9,11,0,1,2]

def run(total_turns):
	prev_said = {n: turn for turn, n in enumerate(starting[:-1])}
	total_turns = 30000000
	n = starting[-1]
	for turn in range(len(starting) - 1, total_turns - 1):
		if n in prev_said:
			next_number = turn - prev_said[n]
		else:
			next_number = 0

		prev_said[n] = turn
		n = next_number

	return n

def part_one():
	return run(2020)

def part_two():
	return run(30000000)

print('Part one', part_one())
print('Part two', part_two())