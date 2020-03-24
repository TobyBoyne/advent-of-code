import numpy as np

def read_input():
	ranges = []
	with open("day06.txt") as f:
		for line in f:
			*action, c1, _, c2 = line.strip("\n").split()
			x1, y1 = (int(x) for x in c1.split(','))
			x2, y2 = (int(x) for x in c2.split(','))
			ranges.append((" ".join(action), (x1, y1), (x2, y2)))

	return ranges

def part_one(ranges):
	lights = np.zeros((1000, 1000))
	for instr in ranges:
		action, (x1, y1), (x2, y2) = instr
		if action == "turn on":
			lights[y1:y2+1, x1:x2+1] = 1
		if action == "turn off":
			lights[y1:y2+1, x1:x2+1] = 0
		if action == "toggle":
			lights[y1:y2+1, x1:x2+1] = 1 - lights[y1:y2+1, x1:x2+1]

	return lights

ranges = read_input()
print(np.count_nonzero(part_one(ranges)))