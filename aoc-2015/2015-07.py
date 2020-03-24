ops = {
	"AND":		lambda a: a[0] & a[1],
	"OR":		lambda a: a[0] | a[1],
	"NOT":		lambda a: ~ a[0],
	"LSHIFT":	lambda a: a[0] << a[1],
	"RSHIFT":	lambda a: a[0] >> a[1],
	"SET":		lambda a: a[0]
}


def read_input():
	instructions = []
	with open("day07.txt") as f:
		for line in f:
			in_signal, output = line.strip("\n").split(" -> ")
			split_signal = in_signal.split()
			if len(split_signal) == 1:
				instructions.append(("SET", split_signal, output))
			else:
				*a, operation, b = split_signal
				inputs = list(a) + [b]
				instructions.append((operation, inputs, output))

	return instructions


def part_one(instructions):
	wires = {}
	wires_with_values = set()
	# compile all instructions
	# if the wire is assigned a value, set that wire to the value in this step
	for operation, inputs, output in instructions:
		wires[output] = (operation, inputs)
		if operation == "SET" and inputs[0].isnumeric():
			wires[output] = int(inputs[0])
			wires_with_values.add(output)

	# repeatedly go through all wires until every wire has been assigned a value
	while len(wires) != len(wires_with_values):
		for wire, in_signal in wires.items():
			if wire not in wires_with_values:
				operation, inputs = in_signal
				in_wires = [w for w in inputs if not w.isnumeric()]
				if set(in_wires).issubset(wires_with_values):
					converted_inputs = [int(i) if i.isnumeric() else wires[i] for i in inputs]
					wires[wire] = ops[operation](converted_inputs)
					wires_with_values.add(wire)

	return wires['a']



instructions = read_input()
print(part_one(instructions))