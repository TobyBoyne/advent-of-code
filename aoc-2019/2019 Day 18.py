import numpy as np
from string import ascii_lowercase, ascii_uppercase

DIRS = (
	0 + 1j,
	0 - 1j,
	1 + 0j,
	-1 + 0j
)

class Tunnels:
	def __init__(self):
		self.start_pos = 0 + 0j
		self.tunnels = []
		self.door_keys = {}
		self.locks = {}
		self.read_map()


	def read_map(self):
		tunnel_map = read_file()
		self.tunnels = tunnel_map
		for y, line in enumerate(tunnel_map):
			for x, c in enumerate(line):
				if c == "@":
					self.start_pos = x + y * 1j
				if c in ascii_lowercase:
					self.door_keys[c] = True

	def get_moves(self, cur_pos):
		possible_moves = []

		def is_blocked(coord):
			tile = self.tunnels[coord.imag][coord.real]
			return tile == '#' or self.door_keys.get(tile.upper())

		def step(cur_pos, prev_dir, num_steps):
			tile = self.tunnels[cur_pos.imag][cur_pos.real]
			if tile in self.door_keys:
				pass








	def __repr__(self):
		return "\n".join("".join(c for c in line) for line in self.tunnels)



def read_file():
	tunnel_map = []
	with open("day18.txt") as f:
		for line in f:
			map_line = [c for c in line.strip("\n")]
			tunnel_map.append(map_line)

	return tunnel_map

t = Tunnels()
print(t)
