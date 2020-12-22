from parse import parse

MOVES = {
	'N': 1j,
	'E': 1,
	'S': -1j,
	'W': -1
}

COMPASS = list(MOVES.keys())

with open('day12.txt') as f:
	instructions = [parse('{:.1}{:d}', l.rstrip()).fixed for l in f.readlines()]

def part_one():
	direction = 'E'
	pos = 0 + 0j
	for instr, num in instructions:
		if instr in MOVES:
			pos += num * MOVES[instr]
		elif instr == 'F':
			pos += num * MOVES[direction]
		else:
			rotation_dir = 1 if instr == 'R' else -1
			cur_dir_idx = COMPASS.index(direction)
			direction = COMPASS[(cur_dir_idx + (num//90) * rotation_dir) % 4]

	return abs(pos.real) + abs(pos.imag)

def part_two():
	pos = 0 + 0j
	waypoint = 10 + 1j
	for instr, num in instructions:
		if instr in MOVES:
			waypoint += num * MOVES[instr]
		elif instr == 'F':
			pos += waypoint * num
		else:
			rotation_dir = 1 if instr == 'L' else -1
			rot = 1j ** (rotation_dir * num // 90)
			waypoint *= rot
	return abs(pos.real) + abs(pos.imag)

print('Part one', part_one())
print('Part two', part_two())

