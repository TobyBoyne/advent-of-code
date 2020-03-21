from itertools import product

DIRECTIONS = {
	"U": 1j,
	"D": -1j,
	"R": 1,
	"L": -1
}


class Line:
	def __init__(self, start:complex, end:complex, direction, steps):
		# vertical is True if the the line is moving up or down
		self.vertical = direction in ("U", "D")

		# line is always either pointing to the right or up
		sort_key = lambda x: x.imag if self.vertical else x.real
		self.start, self.end = sorted((start, end), key=sort_key)

		# steps stores the number of steps taken to get to the START of the wire
		self.steps = steps

	def intersect(self, other:'Line'):
		if self.vertical == other.vertical:
			return False

		horiz, vert = sorted((self, other), key=lambda l: l.vertical)
		if (horiz.start.real <= vert.start.real <= horiz.end.real and
			vert.start.imag <= horiz.start.imag <= vert.end.imag):
			# returns (intersection_coordinate, total_steps)
			x, y = vert.start.real, horiz.start.imag
			total_steps = horiz.steps + (x - horiz.start.real) + \
						  vert.steps + (y - vert.start.imag)

			if total_steps == 581:
				print(horiz.steps, vert.steps, y, vert.start.imag)

			return x + y * 1j, total_steps
		else:
			return False


class Wire:
	def __init__(self, instructions):
		self.lines = []
		self.cur_pos = 0+0j
		self.steps = 0

		self.read_instructions(instructions)

	def read_instructions(self, instructions):
		for i in instructions:
			self.new_line(i)

	def new_line(self, instruction):
		direction, steps = instruction[0], int(instruction[1:])
		end_pos = self.cur_pos + steps * DIRECTIONS[direction]
		self.lines.append(Line(self.cur_pos, end_pos, direction, self.steps))

		self.steps += steps
		self.cur_pos = end_pos

	def find_intersections(self, other:'Wire'):
		intersections = []

		for line, other_line in product(self.lines, other.lines):
			intersect = line.intersect(other_line)
			if intersect:
				intersections.append(intersect)

		return intersections




def read_file():
	with open("day3.txt") as f:
		wires = [line.strip("\n").split(",") for line in f]

	return wires


instructions = read_file()
wire_A, wire_B = (Wire(instr) for instr in instructions)
intersections = wire_A.find_intersections(wire_B)

closest_intersction = min(intersections, key=lambda x: abs(x[0].real) + abs(x[0].imag))
print("Part one:", closest_intersction)

fewest_steps = min(intersections, key=lambda x: x[1])
print("Part two:", fewest_steps)

