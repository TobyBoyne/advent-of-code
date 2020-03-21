from collections import defaultdict

def read_file():
	n = 0
	start_state = 'A'
	current_state = ''
	state_data = [[0, 0, ''], [0, 0, '']]
	states = {}
	with open("day25.txt", 'r') as f:
		for y, line in enumerate(f):
			line = line.strip("\n")
			if y == 0:
				start_state = line[15]
			elif y == 1:
				n = int(line[36 : -7])
			elif "In state" in line:
				current_state = line[-2]
			elif line:
				current_value = 0 if (y - 2) % 10 < 6 else 1
				if "Write" in line:
					state_data[current_value][0] = int(line[22])
				elif "Move" in line:
					state_data[current_value][1] = 1 if 'r' in line else -1
				elif "Continue" in line:
					state_data[current_value][2] = line[26]
			else:
				# if the line is blank, store the state data in the state
				if current_state:
					states[current_state] = state_data
					state_data = [[0, 0, ''], [0, 0, '']]

	return n, start_state, states


def run():
	n, start_state, states = read_file()
	state = start_state
	tape = defaultdict(int)
	cursor = 0

	for i in range(n):
		value, direction, new_state = states[state][tape[cursor]]

		tape[cursor] = value
		cursor += direction
		state = new_state

	print(sum(tape.values()))



run()