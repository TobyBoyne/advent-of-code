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
		if not inverse:
			idx = np.argwhere(arr == self.args[0])[0]
			n = 1 + idx + (idx >= 4)
			arr = np.roll(arr, n)
		else:
			idx = np.argwhere(arr == self.args[0])[0][0]
			i = 0
			while not ((1 + idx == i) or ((2 + idx != i) and idx >= 4)):
				arr = np.roll(arr, -1)
				i += 1
				idx = (idx - 1) % len(arr)
				print(i, idx)
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

def scramble(moves, password):
	arr = np.array([c for c in password])
	for move in moves:
		arr = move(arr)
	return arr

def part_one(moves, password):
	scrambled_arr = scramble(moves, password)
	return "".join(scrambled_arr)


moves = read_input()
password = "abcdefgh"
print(part_one(moves, password))