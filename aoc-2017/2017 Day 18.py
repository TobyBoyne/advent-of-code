from collections import defaultdict
from typing import Union

OPERATIONS = {
	'set':	lambda prog, a, b, r: prog.set_reg(r, b),
	'add':	lambda prog, a, b, r: prog.set_reg(r, a + b),
	'mul':	lambda prog, a, b, r: prog.set_reg(r, a * b),
	'mod':	lambda prog, a, b, r: prog.set_reg(r, a % b),

	'snd':	lambda prog, x, _: prog.snd(x),
	'rcv':	lambda prog, x, r: prog.rcv(x, r),
	'jgz':	lambda prog, x, y, _: prog.jump(y) if x > 0 else None
}

class Program:
	def __init__(self, program_id):
		self.registers = defaultdict(int)
		self.registers['p'] = program_id
		self.instructions = []
		self.cur = 0

		self.done = False
		self.queue = []
		self.waiting = False
		self.total_msgs_sent = 0

		# attribute to link the two programs
		self.other_prog: Union['Program', None] = None

		self.read_file()

	def read_file(self):
		self.instructions = []
		with open("day18.txt", 'r') as f:
			for line in f:
				opcode, *operands = line.strip("\n").split()
				self.instructions.append((opcode, operands))

	def execute_instructions(self):
		while not self.done and 0 <= self.cur < len(self.instructions):
			if not self.waiting:
				opcode, operands = self.instructions[self.cur]
				func = OPERATIONS[opcode]
				func(self, *self.function_args(*operands))
				self.cur += 1
			else:
				self.other_prog.execute_instructions()

	def function_args(self, *args):
		"""Converts args into constant/register references, depending on their value"""
		converted_args = []
		for arg in args:
			try:
				converted_args.append(int(arg))
			except ValueError:
				converted_args.append(self.registers[arg])
		converted_args.append(args[0])
		return converted_args

	def set_reg(self, r, value):
		self.registers[r] = value

	def snd(self, value):
		self.total_msgs_sent += 1
		self.other_prog.queue.append(value)
		if self.other_prog.waiting:
			self.other_prog.rcv(None, self.other_prog.waiting)

	def rcv(self, _, reg):
		if self.queue:
			self.set_reg(reg, self.queue.pop(0))
			self.waiting = False
		else:
			self.waiting = reg
			if self.other_prog.waiting:
				print("Deadlock")
				self.done = True
				self.other_prog.done = True



	def jump(self, offset):
		self.cur += offset - 1


class SoundProgram(Program):
	""" Replace send with sound; replace receive with recover sound """
	def __init__(self):
		self.last_sound = 0
		super().__init__(program_id=0)

	def snd(self, sound, *_):
		self.last_sound = sound

	def rcv(self, value, _):
		if value != 0:
			self.done = True


def part_one():
	p = SoundProgram()
	p.execute_instructions()
	return p.last_sound

def part_two():
	prog0 = Program(0)
	prog1 = Program(1)
	prog0.other_prog = prog1
	prog1.other_prog = prog0

	prog0.execute_instructions()
	return prog1.total_msgs_sent


print("Part one:", part_one())
print("Part two:", part_two())