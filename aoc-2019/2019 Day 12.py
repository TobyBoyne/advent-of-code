import numpy as np
from functools import reduce
from math import gcd

class MoonGroup:
	def __init__(self, moons_coords):
		self.moons = [Moon(pos) for pos in moons_coords]

	def sim(self):
		[m.calc_vel(self.moons) for m in self.moons]
		[m.move() for m in self.moons]


	def sim_n_times(self, n=1):
		for i in range(n):
			self.sim()

	def sim_until_equal(self, other: 'MoonGroup', max_iter=10000):
		for i in range(max_iter):
			if i > 0 and self == other:
				break
			self.sim()
		# if no break, then raise an error
		else:
			raise ValueError("Too many iterations")

		return i


	def total_energy(self):
		return sum(m.energy() for m in self.moons)

	def __eq__(self, other):
		return all(m in other.moons for m in self.moons)


class Moon:
	def __init__(self, initial_pos):
		self.pos = initial_pos
		self.vel = np.zeros_like(self.pos)

	def calc_vel(self, moons):
		self.vel += sum(self.gravity(moon) for moon in moons if moon is not self)

	def gravity(self, other: 'Moon'):
		return np.sign(other.pos - self.pos)

	def move(self):
		self.pos += self.vel

	def energy(self):
		return sum(abs(self.pos)) * sum(abs(self.vel))

	def __eq__(self, other):
		return self.pos == other.pos and self.vel == other.vel

	def __repr__(self):
		return f"pos=<{self.pos}, vel=<{self.vel}>>"


def read_file():
	moon_coords = np.zeros((4, 3))
	with open("day12.txt") as f:
		for i, line in enumerate(f):
			remove_chars = ['\n', '<', '>', ' ', 'x', 'y', 'z', '=']
			coords = "".join(c for c in line if c not in remove_chars)
			pos = np.fromstring(coords, sep=',')
			moon_coords[i,:] = pos

	return moon_coords


moons = MoonGroup(read_file())
moons.sim_n_times(1000)
print("Part one:", moons.total_energy())


initial_state = read_file()
loop_sizes = []
# find the time taken for a complete loop in each dimension
for moons_in_dim in zip(*initial_state):
	initial_moons = MoonGroup(moons_in_dim)
	current_moons = MoonGroup(moons_in_dim)
	t = current_moons.sim_until_equal(initial_moons, max_iter=500000)
	print(t)
	loop_sizes.append(t)

lcm = lambda a, b: abs(a * b) // gcd(a, b) if a and b else 0
time_to_repeat = reduce(lcm, loop_sizes)
print("Part two:", time_to_repeat)