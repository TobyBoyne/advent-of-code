from itertools import product
from typing import List

class Vector:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y
	def __add__(self, other: 'Vector'):
		return Vector(self.x + other.x, self.y + other.y)
	def __eq__(self, other: 'Vector'):
		return self.x == other.x and self.y == other.y
	def __repr__(self):
		return f"V({self.x}, {self.y})"

DIRECTIONS = {
	'N':	Vector(0, 1),
	'S':	Vector(0, -1),
	'E':	Vector(1, 0),
	'W':	Vector(-1, 0)
}


class Room:
	def __init__(self, pos: Vector):
		self.pos = pos
		self.linked_rooms: List['Room'] = []
		self.distance = 0
	def __eq__(self, other: 'Room'):
		return self.pos == other.pos


class Map:
	def __init__(self):
		self.rooms = []
		self.regex = ''

	def read_file(self):
		with open("day20.txt", 'r') as f:
			self.regex = f.read()[1:-1]

	def map_rooms(self, regex: str):
		cur = Vector(0, 0)
		i = 0

		for c in regex:
			c = regex[i]
			current_room = Room(cur)
			if current_room in self.rooms:
				current_room = self.rooms[self.rooms.index(current_room)]
			else:
				self.rooms.append(current_room)

			if c in "NSEW":
				cur += DIRECTIONS[c]

def parse_regex(regex: str) -> List[str]:
	print(regex)
	output = ""
	choices = []
	if regex.count('|') == 0:
		return [regex]

	elif regex.count('(') == 0:
		return regex.split("|")

	else:
		for i, c in enumerate(regex):
			if c in "NSEW":
				output += c
			elif c == '|':
				choices.append(output)
				output = ""

			elif c == '(':
				# extract bracketed bits, then parse that
				cur_index = i + 1
				finished_bracket = False
				while not finished_bracket:
					cur_index += 1
					finished_bracket = regex[i:cur_index + 1].count('(') - regex[i:cur_index + 1].count(')') == 0

				choices += parse_regex(regex[i + 1:cur_index])

	print("!", regex, choices)
	if not choices: choices = ['']
	return [output + c for c in choices]

reg = "E(N|SSE(EE|N))"
reg = "(E|NW)"
for p in parse_regex(reg):
	print("PATHS:", p)