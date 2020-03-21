from collections import namedtuple

def execute_opcode(input_registers, args, opcode):
	registers = list(input_registers)
	if opcode == "setr":
		registers[args[2]] = registers[args[0]]
	elif opcode == "seti":
		registers[args[2]] = args[0]

	elif "gt" in opcode or "eq" in opcode:
		if opcode[-2:] == 'ir':
			arg1, arg2 = args[0], registers[args[1]]
		elif opcode[-2:] == 'ri':
			arg1, arg2 = registers[args[0]], args[1]
		else:
			arg1, arg2 = registers[args[0]], registers[args[1]]

		if "gt" in opcode:
			registers[args[2]] = int(arg1 > arg2)
		elif "eq" in opcode:
			registers[args[2]] = int(arg1 == arg2)

	else:
		if opcode[-1] == 'r':
			arg1, arg2 = registers[args[0]], registers[args[1]]
		else:
			arg1, arg2 = registers[args[0]], args[1]

		if "add" in opcode:
			registers[args[2]] = arg1 + arg2
		elif "mul" in opcode:
			registers[args[2]] = arg1 * arg2
		elif "ban" in opcode:
			registers[args[2]] = arg1 & arg2
		elif "bor" in opcode:
			registers[args[2]] = arg1 | arg2
	return	registers

with open("day19.txt") as f:
	instructions = []
	for n, line in enumerate(f):
		if n == 0:
			ip = int(line[4])
			registers = [0 for i in range(6)]
		else:
			Instruction = namedtuple("Instruction", ["opcode", "args"])
			opcode, *arguments = line.strip("\n").split()
			arguments = [int(a) for a in arguments]
			instructions.append(Instruction(opcode, arguments))

i = registers[ip]
[print(instr) for instr in instructions]
while i < len(instructions):
	print(registers, i)
	instr = instructions[i]
	registers = execute_opcode(registers, instr.args, instr.opcode)
	print(registers, instr.opcode, instr.args, "\n")
	registers[ip] += 1
	i = registers[ip]
