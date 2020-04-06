import numpy as np
from parse import parse


class Op:
	def __init__(self, args):
		self.args = args

class SwapPosition(Op):
	def __call__(self, arr, inverse=False):
		# symmetric
		arr[self.args[0]], arr[self.args[1]] = arr[self.args[1]], arr[self.args[0]]
		return arr

class SwapLetter(Op):
	def __call__(self, arr, inverse=False):
		# symmetric
		i, j = np.argwhere(arr == self.args[0])[0], np.argwhere(arr == self.args[1])[0]
		arr[i], arr[j] = arr[j], arr[i]
		return arr

class RotateSteps(Op):
	def __call__(self, arr, inverse=False):
		n = self.args[1]
		n *= -1 if self.args[0] == "left" else 1
		n *= -1 if inverse else 1
		arr = np.roll(arr, n)
		return arr

class RotateBased(Op):
	def __call__(self, arr, inverse=False):
		idx = np.argwhere(arr == self.args[0])[0][0]
		if not inverse:
			n = rotate_map[idx] - idx
		else:
			n = reverse_rotate_map[idx] - idx

		arr = np.roll(arr, n)
		return arr

class Reverse(Op):
	def __call__(self, arr, inverse=False):
		i, j = self.args
		arr[i:j + 1] = arr[i:j + 1][::-1]
		return arr

class Move(Op):
	def __call__(self, arr, inverse=False):
		if not inverse:
			i, j = self.args
		else:
			j, i = self.args

		value = arr[i]
		arr = np.delete(arr, i)
		arr = np.insert(arr, j, value)
		return arr


# unique word in string matches to a pattern for parse
patterns = {
	"swap position":	(SwapPosition, "swap position {:d} with position {:d}"),
	"swap letter":		(SwapLetter, "swap letter {} with letter {}"),
	"step":				(RotateSteps, "rotate {} {:d} {}"),
	"rotate based":		(RotateBased, "rotate based on position of letter {}"),
	"reverse":			(Reverse, "reverse positions {:d} through {:d}"),
	"move":				(Move, "move position {:d} to position {:d}")
}

# dictionaries used to work out where a letter will end up after rotation
rotate_map = {i: (2 * i + 1 + (i >= 4)) % 8 for i in range(8)}
reverse_rotate_map = {v: k for k, v in rotate_map.items()}

def read_input():
	moves = []
	with open("day21.txt") as f:
		for line in f:
			for phrase, details in patterns.items():
				if phrase in line:
					operation, pat = details
					p = parse(pat, line.strip("\n"))
					move = operation(p.fixed)
					moves.append(move)
	return moves

def scramble(moves, password, inverse=False):
	arr = np.array([c for c in password])
	if inverse:
		moves = moves[::-1]
	for move in moves:
		arr = move(arr, inverse)
	return arr

def part_one(moves, password):
	scrambled_arr = scramble(moves, password)
	return "".join(scrambled_arr)

def part_two(moves, password):
	scrambled_arr = scramble(moves, password, inverse=True)
	return "".join(scrambled_arr)


moves = read_input()
password = "abcdefgh"
scrambled_password = "fbgdceah"
print(part_one(moves, password))
print(part_two(moves, scrambled_password))