f = open("day16.txt", 'r')

OPCODES = [
	"addr",
	"addi",
	"mulr",
	"muli",
	"banr",
	"bani",
	"borr",
	"bori",
	"setr",
	"seti",
	"gtrr",
	"gtri",
	"gtir",
	"eqrr",
	"eqri",
	"eqir"
]

def execute_opcode(input_registers, args, opcode):
	registers = list(input_registers)
	if opcode == "setr":
		registers[args[3]] = registers[args[1]]
	elif opcode == "seti":
		registers[args[3]] = args[1]

	elif "gt" in opcode or "eq" in opcode:
		if opcode[-2:] == 'ir':
			arg1, arg2 = args[1], registers[args[2]]
		elif opcode[-2:] == 'ri':
			arg1, arg2 = registers[args[1]], args[2]
		else:
			arg1, arg2 = registers[args[1]], registers[args[2]]

		if "gt" in opcode:
			registers[args[3]] = int(arg1 > arg2)
		elif "eq" in opcode:
			registers[args[3]] = int(arg1 == arg2)

	else:
		if opcode[-1] == 'r':
			arg1, arg2 = registers[args[1]], registers[args[2]]
		else:
			arg1, arg2 = registers[args[1]], args[2]

		if "add" in opcode:
			registers[args[3]] = arg1 + arg2
		elif "mul" in opcode:
			registers[args[3]] = arg1 * arg2
		elif "ban" in opcode:
			registers[args[3]] = arg1 & arg2
		elif "bor" in opcode:
			registers[args[3]] = arg1 | arg2
	return	registers


# -- PART ONE --
def total_three_or_more():
	with open("day16.txt", 'r') as f:
		total = 0
		file_input = f.readlines()
		# 3224
		for line in range(0, 3224, 4):
			num_matching_opcodes = 0
			registers = [int(c) for c in file_input[line][9:19].split(',')]
			args = [int(c) for c in file_input[line + 1].split()]
			results = [int(c) for c in file_input[line + 2][9:19].split(',')]
			for opcode in OPCODES:
				if execute_opcode(registers, args, opcode) == results:
					num_matching_opcodes += 1
			if num_matching_opcodes >= 3:
				total += 1
	print("Count with >= 3:", total)

# -- PART TWO --
def run_test_program():
	# temp_op_numbers stores the possible number for each opcode
	# op_numbers stores the final opcode for each number, as they are unique
	temp_op_numbers = {i:[opcode for opcode in OPCODES] for i in range(16)}
	op_numbers = {i:'' for i in range(16)}
	with open("day16.txt", 'r') as f:
		file_input = f.readlines()
		for line in range(0, 3224, 4):
			registers = [int(c) for c in file_input[line][9:19].split(',')]
			args = [int(c) for c in file_input[line + 1].split()]
			results = [int(c) for c in file_input[line + 2][9:19].split(',')]
			for opcode in OPCODES:
				if execute_opcode(registers, args, opcode) != results:
					if opcode in temp_op_numbers[args[0]]:
						temp_op_numbers[args[0]].remove(opcode)

		# loop as long as not every number is assigned an opcode
		assigned_opcodes = []
		while not all([op_numbers[i] for i in range(16)]):
			for n in temp_op_numbers:
				# unique_opcodes is an array of all the possible opcodes of a number that haven't been assigned
				unique_opcodes = [x for x in temp_op_numbers[n] if x not in assigned_opcodes]
				if len(unique_opcodes) == 1:
					op_numbers[n] = unique_opcodes[0]
					assigned_opcodes.append(unique_opcodes[0])
		print(op_numbers)

		test_registers = [0, 0, 0, 0]
		for line in range(3226, 4174):
			args = [int(c) for c in file_input[line].split()]
			test_registers = execute_opcode(test_registers, args, op_numbers[args[0]])
		print(test_registers)
		print("Contents of registers[0]:", test_registers[0])


total_three_or_more()
run_test_program()