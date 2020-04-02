from itertools import combinations
from copy import deepcopy

class State:
	def __init__(self, steps, elevator, floors):
		self.steps = steps
		self.e = elevator
		self.floors = floors
	def __eq__(self, other):
		return self.e == other.e and self.floors == other.floors

	def is_valid(self):
		# no components are fried, and there is at least one component on the floor with the elevator
		return all(not any_fried(floor) for floor in self.floors) and len(self.floors[self.e]) != 0

	def is_finished(self):
		# components are all on last floor - every other floor is empty
		return all(len(floor) == 0 for floor in self.floors[:-1])

	def __repr__(self):
		return "\n".join(str(floor) for floor in self.floors) + "\n-------"


def read_input():
	with open("day11.txt") as f:
		floors = [[] for _ in range(4)]
		elements = {}
		n = 0
		for i, line in enumerate(f):
			line_clean = line.strip(".\n").replace(" and", "").replace("-compatible", "")
			_, *comp_strings = line_clean.split(" a ")
			for comp in comp_strings:
				element, comp_type = comp.split()
				if element not in elements:
					elements[element] = n
					n += 1
				component = (elements[element], comp_type == 'microchip')
				floors[i].append(component)

	return floors


def any_fried(floor):
	# returns true if any of the microchips on a floor will be fried
	has_gens = any(not is_micro_other for _, is_micro_other in floor)
	for (i, is_micro) in floor:
		if is_micro:
			powered = any(i == j and not is_micro_other for j, is_micro_other in floor)
			if not powered and has_gens:
				return True

	return False

def get_moves(floor):
	# returns the state of the floor, and all the moved components, in every possible combination
	for comps in combinations(floor + [None], 2):
		comps = [c for c in comps if c is not None]
		new_floor = floor.copy()
		[new_floor.remove(comp) for comp in comps]
		yield new_floor, comps


def part_one(floors):
	elevator = 0
	steps = 0
	initial_state = State(0, 0, floors)
	states = [initial_state]
	new_states = [initial_state]
	done = False

	while not done and steps < 100:
		steps += 1
		cur_states = new_states
		new_states = []

		for state in cur_states:
			cur = state.e
			next_floor_idx = [x for x in (cur + 1, cur - 1) if 0 <= x <= 3]
			for new_floor, to_move in get_moves(state.floors[cur]):
				for i in next_floor_idx:
					new_floors = deepcopy(state.floors)
					new_floors[cur] = new_floor
					new_floors[i] += to_move
					new_state = State(steps, i, new_floors)
					if new_state.is_valid() and new_state not in states:
						states.append(new_state)
						new_states.append(new_state)
						if new_state.is_finished():
							done = True

	return steps



floors = read_input()
print(part_one(floors))