from collections import Counter
from typing import List


class Program:
	def __init__(self, name: str, weight: int):
		self.name = name
		self.weight = weight
		self.children: List['Program'] = []
		self.parent = None

	def add_child(self, child: 'Program'):
		self.children.append(child)

	def total_weight(self):
		return self.weight + sum(c.total_weight() for c in self.children)

	def balanced(self) -> bool:
		return len(set(c.total_weight() for c in self.children)) < 2

	def __eq__(self, other):
		return other == self.name
	def __repr__(self):
		return self.name + "(" + str(self.weight) + ")"
	def __hash__(self):
		return hash(self.name)


class Tower:
	def __init__(self):
		self.tower: List[Program] = []
		self.read_file()

	def read_file(self):
		with open("day7.txt", 'r') as f:
			for line in f:
				name, weight, *children = line.strip("\n").split()
				weight = int(weight[1:-1])
				children = [child.strip(",") for child in children[1:]]
				if name in self.tower:
					new_prog = self.tower[self.tower.index(name)]
					new_prog.weight = weight
				else:
					new_prog = Program(name, weight)
					self.tower.append(new_prog)

				if children:
					# for all of the new program's children, either:
					# - if the child already exists, make the parent/child link between the two
					# - if the child does not exist, make a new child with the link
					for child in children:
						if child in self.tower:
							child_prog = self.tower[self.tower.index(child)]

						else:
							child_prog = Program(child, -1)
							self.tower.append(child_prog)

						child_prog.parent = new_prog
						new_prog.add_child(child_prog)


	def find_base(self):
		# PART ONE
		base = [p for p in self.tower if not p.parent][0]
		return base

	def unbalanced_prog(self):
		# PART TWO
		for prog in self.tower:
			if not prog.balanced() and all(child.balanced() for child in prog.children):
				weights = {c: c.total_weight() for c in prog.children}
				count = Counter(weights[key] for key in weights)
				common_weight, odd_weight = count.most_common()[0][0], count.most_common()[1][0]

				weight_to_change_prog = [key for key in weights if weights[key] == odd_weight][0]
				prog_weight = weight_to_change_prog.weight
				return prog_weight + common_weight - odd_weight

		return 0

t = Tower()
print(t.find_base())
print(t.unbalanced_prog())