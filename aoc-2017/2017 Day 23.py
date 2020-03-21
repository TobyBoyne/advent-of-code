eval("print('hey there')")

registers = {c: 0 for c in map(chr, range(97, 105))}
print(registers)

cur = 0
mul_count = 0


def set(x, y):
	registers[x] = y

def sub(x, y):
	registers[x] -= y

def mul(x, y):
	global mul_count
	registers[x] *= y
	mul_count += 1

def jnz(x, y):
	global cur

	try:
		x = int(x)
	except ValueError:
		x = registers[x]

	if x != 0:
		cur += y - 1


def read_file():
	instructions = []
	with open("day23.txt", 'r') as f:
		for line in f:
			if line != '--\n':
				instructions.append(line.strip("\n").split())
	return instructions

def debug():
	global cur
	global mul_count

	instructions = read_file()
	cur = 0
	mul_count = 0

	while 0 <= cur < len(instructions):

		instr, x, y = instructions[cur]
		try:
			y = int(y)
		except ValueError:
			y = registers[y]

		eval(instr + '("' + x + '", ' + str(y) + ')')
		cur += 1

	print(mul_count)

def prime_check():
	h=0
	for x in range(108400, 125400 + 1, 17):
		for i in range(2, x):
			if x % i == 0:
				h += 1
				break
	print(h)



#debug()
prime_check()