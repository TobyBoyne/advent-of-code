def read_file():
	components = []
	with open("day24.txt", 'r') as f:
		for line in f:
			components.append([int(v) for v in line.strip("\n").split('/')])
	return components


def strength(bridge):
	return sum(sum(piece) for piece in bridge)

def length(bridge):
	return len(bridge)

def strongest_bridge(pieces):
	return build_bridge(pieces, strength)

def longest_bridge(pieces):
	return build_bridge(pieces, length)


def build_bridge(pieces, func, open_port=0):
	bridge = []
	sub_bridges = []
	next_pieces = []

	# find all the possible pieces that can fit at the end of the current piece

	next_pieces = [p for p in pieces if open_port in p]
	if len(next_pieces) == 0:
		return []
	elif len(next_pieces) == 1:
		next_piece = next_pieces[0]
		next_open = [p for p in next_piece if p != open_port]
		# if both ports are equal, then both will be removed - need to add one back
		if not next_open: next_open = [open_port]

		return [next_piece] + build_bridge([p for p in pieces if p != next_piece], func, next_open[0])
	else:
		for next_piece in next_pieces:
			next_open = [p for p in next_piece if p != open_port]
			# if both ports are equal, then both will be removed - need to add one back
			if not next_open: next_open = [open_port]

			# build a new sub bridge starting from each possible next piece
			new_sub = [next_piece] + build_bridge([p for p in pieces if p != next_piece], func, next_open[0])
			sub_bridges.append(new_sub)

		# find the strongest sub bridge
		return max(sub_bridges, key=func)



components = read_file()

print("Part one:", strength(strongest_bridge(components)))
print("Part two:", strength(longest_bridge(components)))