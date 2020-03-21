from typing import List

class Program:
	def __init__(self, name: str):
		self.name = name
		self.connections: List['Program'] = []

	def add_connection(self, prog: 'Program'):
		self.connections.append(prog)


	def __eq__(self, other):
		if isinstance(other, Program):	return self.name == other.name
		else:							return self.name == other
	def __repr__(self):
		return self.name + "[" + ", ".join(c.name for c in self.connections) + "]"



class Village:
	def __init__(self):
		self.programs: List[Program] = []
		self.read_file()

	def read_file(self):
		with open("day12.txt", 'r') as f:
			for line in f:
				prog, _, *other_progs = line.strip("\n").replace(',', '').split()
				if prog in self.programs:
					new_prog = self.programs[self.programs.index(prog)]
				else:
					new_prog = Program(prog)
					self.programs.append(new_prog)

				for other in other_progs:
					if other in self.programs:
						other_prog = self.programs[self.programs.index(other)]
					else:
						other_prog = Program(other)
						self.programs.append(other_prog)
					new_prog.add_connection(other_prog)

	def group(self, containing):
		programs = [self.programs[self.programs.index(containing)]]
		progs_added = True
		while progs_added:
			progs_added = False
			for p in programs:
				for c in p.connections:
					if c not in programs:
						programs.append(c)
						progs_added = True
		return programs

	def num_groups(self):
		visited = {str(i): False for i in range(len(self.programs))}
		group_count = 0
		while not all(visited[k] for k in visited):
			to_visit = min(p for p in visited if not visited[p])
			for prog in self.group(to_visit):
				visited[prog.name] = True
			group_count += 1

		return group_count



v = Village()
print("Part one:", len(v.group('0')))
print("Part two:", v.num_groups())
