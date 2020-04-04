import numpy as np
from parse import parse

# unique word in string matches to a pattern for parse
patterns = {
	"swap position":	"swap position {:d} with position {:d}",
	"swap letter":		"swap letter {} with letter {}",
	"step":				"rotate {} {:d} {}",
	"rotate based":		"rotate based on position of letter {}",
	"reverse":			"reverse positions {:d} through {:d}",
	"move":				"move position {:d} to position {:d}"
}


def read_input():
	moves = []
	with open("day21.txt") as f:
		for line in f:
			for phrase, pat in patterns.items():
				if phrase in line:
					p = parse(pat, line.strip("\n"))
					move = (phrase, p.fixed)
					moves.append(move)
	return moves

def scramble(moves, password):
	arr = np.array([c for c in password])
	for move, args in moves:
		print(arr, "next move", move, args)
		if move == "swap position":
			arr[args[0]], arr[args[1]] = arr[args[1]], arr[args[0]]
		if move == "swap letter":
			i, j = np.argwhere(arr == args[0])[0], np.argwhere(arr == args[1])[0]
			arr[i], arr[j] = arr[j], arr[i]
		if move == "step":
			n = args[1]
			n *= -1 if args[0] == "left" else 1
			arr = np.roll(arr, n)
		if move == "rotate based":
			idx = np.argwhere(arr == args[0])[0]
			n = 1 + idx + (idx >= 4)
			arr = np.roll(arr, n)
		if move == "reverse":
			i, j = args
			arr[i:j+1] = arr[i:j+1][::-1]
		if move == "move":
			i, j = args
			if i < j:
				arr = np.concatenate([arr[:i], arr[i+1:j+1], [arr[i]], arr[j+1:]])
			else:
				arr = np.concatenate((arr[:j], [arr[i]], arr[j:i], arr[i+1:]))

	return arr

def part_one(moves, password):
	scrambled_arr = scramble(moves, password)
	return "".join(scrambled_arr)


moves = read_input()
password = "abcdefgh"
print(part_one(moves, password))