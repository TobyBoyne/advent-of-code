from typing import List
from collections import defaultdict

class Particle:
	def __init__(self, part_id: int, input_string: str):
		self.part_id = part_id
		coords = input_string.split(", ")
		p, v, a = (list(map(int, values[3:-1].split(','))) for values in coords)

		self.p = p
		self.v = v
		self.a = a

	def move(self):
		self.v = [self.v[i] + self.a[i] for i in range(3)]
		self.p = [self.p[i] + self.v[i] for i in range(3)]


	def position_at(self, t: int):
		# s = ut + (1/2) a t^2
		pos = [self.v[i] * t + (1/2) * self.a[i] * t**2 for i in range(3)]
		return pos


	def dist(self):
		return sum(map(abs, self.p))

	def distance_at(self, t: int):
		pos = self.position_at(t)
		return sum(map(abs, pos))


	def __repr__(self):
		return ", ".join(attr + '=' + str(self.__getattribute__(attr)) for attr in vars(self))


def read_file():
	particles = []
	with open("day20.txt", 'r') as f:
		for i, line in enumerate(f):
			particles.append(Particle(i, line.strip("\n")))
	return particles

def closest_to_zero(particles):
	closest = min(particles, key=lambda p: p.distance_at(1000))
	return closest

def collisions(particles: List[Particle], n=200):
	for t in range(n):
		particle_positions = defaultdict(list)
		for p in particles:
			p.move()
			pos = str(p.p)
			particle_positions[pos].append(p.part_id)

		particles = [p for p in particles if len(particle_positions[str(p.p)]) < 2]

	return particles



particles = read_file()
print("Part one:", closest_to_zero(particles).part_id)
print("Part two:", len(collisions(particles)))
