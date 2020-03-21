from functools import partial

def spin(n, programs):
	programs[:] = programs[-n:] + programs[:-n]

def exchange(a, b, programs):
	programs[a], programs[b] = programs[b], programs[a]

def partner(prog1, prog2, programs):
	a, b = programs.index(prog1), programs.index(prog2)
	programs[a], programs[b] = programs[b], programs[a]


def read_file():
	moves = []
	swaps = []
	with open("day16.txt", 'r') as f:
		moves_txt = f.read().strip("\n").split(',')

	for move in moves_txt:
		if move[0] == 's':
			n = int(move[1:])
			moves.append(partial(spin, n))
		elif move[0] == 'x':
			a, b = map(int, move[1:].split('/'))
			moves.append(partial(exchange, a, b))
		else:
			a, b = move[1:].split('/')
			moves.append(partial(partner, a, b))
			swaps.append((a, b))

	return moves, swaps

def dance(programs, moves):
	progs = programs[::]
	for move in moves:
		move(progs)

	return progs


def find_mapping(programs, moves, swaps):
	# find final positions of letters, undo partner swaps, get mapping
	out_programs = dance(programs, moves)
	for s in reversed(swaps):
		partner(*s, out_programs)

	mapping = {i: ord(c) - 97 for i, c in enumerate(out_programs)}

	return mapping

def sim_dance(programs, moves, swaps, n=1):
	# first, ignoring swaps, moves all of the letters to their final positions
	# then swaps all letters in order
	mapping = find_mapping(programs, moves, swaps)
	for count in range(n):
		programs = [programs[mapping[i]] for i in range(len(programs))]
		for s in swaps:
			partner(*s, programs)
		yield programs


num_programs = 16
PROGRAMS = list(map(chr, range(97, 97 + num_programs)))
MOVES, SWAPS = read_file()

print("Part one:", "".join(dance(PROGRAMS, MOVES)))

repeats = []
count = 0
for count, p in enumerate(sim_dance(PROGRAMS, MOVES, SWAPS, 100)):
	if p in repeats:
		break
	repeats.append(p)

print("Part two:", "".join(repeats[1000000000 % count - 1]))


