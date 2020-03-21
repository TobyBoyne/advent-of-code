class Op:
	def __init__(self, params, func, has_output):
		self.params = params
		self.func = func
		self.has_output = has_output

	def __call__(self, modes, args):
		for n, arg in enumerate(args):
			# set the value of position mode arguments to the value stored in that register
			# if output, ignore the final argument as output will never be in immediate mode
			if not self.has_output or n < len(args) - 1:
				if modes[n] == '0':
					args[n] = memory[arg]

		func_output = self.func(*args)
		if self.has_output:
			memory[func_output[1]] = func_output[0]
		else:
			# if not output, the instruction is a jump
			jump = func_output[1]
			return jump

HALT = 99

OPS = {
	1: Op(3, lambda a, b, r: (a + b, r), True),			# ADD
	2: Op(3, lambda a, b, r: (a * b, r), True),			# MUL
	3: Op(1, lambda r: (inputs[-1], r), True),			# INP
	4: Op(1, lambda a: (print(a), None), False),		# OUT
	5: Op(2, lambda a, p: (a, p if a else None), False),# JUMP-IF-TRUE
	6: Op(2, lambda a, p: (a, None if a else p), False),# JUMP-IF-FALSE
	7: Op(3, lambda a, b, r: (int(a < b), r), True),	# LESS-THAN
	8: Op(3, lambda a, b, r: (int(a == b), r), True)	# EQUAL
}

def read_file():
	with open("day5.txt") as f:
		program = [int(x) for x in f.read().split(",")]

	return program


inputs = [5]
memory = read_file()
i = 0
while memory[i] != HALT:
	instr = memory[i]
	opcode = instr % 100
	operation = OPS[opcode]

	num_args = operation.params
	args = memory[i+1:i+1+num_args]
	modes = list(reversed(str(instr)[:-2].rjust(num_args, '0')))

	op_output = operation(modes, args)
	if op_output is None:
		i += 1 + num_args
	else:
		i = op_output
