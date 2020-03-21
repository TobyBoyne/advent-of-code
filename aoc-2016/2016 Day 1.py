dirs = (
	0+1j,	#N
	1+0j,	#E
	0-1j,	#S
	-1+0j	#W
)

def part_one(moves):
	cur_dir = 0
	pos = 0+0j
	for move in moves:
		cur_dir += 1 if "R" in move else -1
		cur_dir %= 4
		pos += int(move[1:]) * dirs[cur_dir]

	print("PART ONE:", abs(pos.real) + abs(pos.imag))

def part_two(moves):
	cur_dir = 0
	pos = 0 + 0j
	visited = []
	for move in moves:
		cur_dir += 1 if "R" in move else -1
		cur_dir %= 4
		for step in range(int(move[1:])):
			pos += dirs[cur_dir]
			if pos in visited:
				print("PART TWO:", abs(pos.real) + abs(pos.imag))
				break
			else:
				visited.append(pos)


with open("day1.txt") as f:
	moves = f.read().strip("\n").split(", ")

part_two(moves)

