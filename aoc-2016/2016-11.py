from itertools import combinations

class Floor(list):
	def is_safe(self):
		return not any(comp.is_fried for comp in self)

	def copy(self):
		return Floor([comp.copy() for comp in self])

	def get_moves(self):
		# returns the state of the floor, and all the moved components, in every possible combination
		for comps in combinations(self + [None], 2):
			comps = [c for c in comps if c is not None]
			new_floor = self.copy()
			[new_floor.remove(comp) for comp in comps]
			yield new_floor, comps



class Component:
	def __init__(self, element, is_micro):
		self.e = element
		self.is_micro = is_micro

	def is_fried(self, floor):
		if self.is_micro:
			powered = any(comp.e == self.e and not comp.is_micro for comp in floor)
			return not powered and any(not comp.is_micro for comp in floor)
		else:
			return False

	def copy(self):
		return Component(self.e, self.is_micro)

	def __repr__(self):
		return self.e[0].upper() + ('M' if self.is_micro else 'G')


def read_input():
	with open("day11.txt") as f:
		floors = [Floor() for _ in range(4)]
		for i, line in enumerate(f):
			line_clean = line.strip(".\n").replace(" and", "").replace("-compatible", "")
			_, *comp_strings = line_clean.split(" a ")
			for comp in comp_strings:
				element, comp_type = comp.split()
				component = Component(element, comp_type == 'microchip')
				floors[i].append(component)

	return floors

def is_valid(floors, elevator):
	# no components are fried, and there is at least one component on the floor with the elevator
	return all(floor.is_safe() for floor in floors) and len(floors[elevator]) != 0



def part_one(floors):
	pass

floors = read_input()
print(floors)
