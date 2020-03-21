from collections import defaultdict

registers = defaultdict(int)

operations = {
	'==':	lambda a, b: a == b,
	'<':	lambda a, b: a < b,
	'<=':	lambda a, b: a <= b,
	'>':	lambda a, b: a > b,
	'>=':	lambda a, b: a >= b,
	'!=':	lambda a, b: a != b,
}

highest_value = 0
with open("day8.txt", 'r') as f:
	for line in f:
		reg, sign, value, _, con_reg, con_op, con_value = line.strip("\n").split()
		condition = operations[con_op]
		if condition(registers[con_reg], int(con_value)):
			registers[reg] += int(value) * (1 if sign == "inc" else -1)
			if registers[reg] > highest_value:
				highest_value = registers[reg]


print(registers)
highest_value_at_end = registers[max(registers, key=lambda x:registers[x])]
print("Part one:", registers[max(registers, key=lambda x:registers[x])])
print("Part two:", highest_value)