moves = {
	'^': 1j,
	'v': -1j,
	'>': 1 + 0j,
	'<': -1 + 0j
}

def read_input():
	with open("day03.txt") as f:
		move_list = f.read().strip("\n")

	return move_list

def part_one(move_list):
	cur_house = 0 + 0j
	houses = {0 + 0j}
	for m in move_list:
		cur_house += moves[m]
		houses.add(cur_house)

	return len(houses)

move_list = read_input()
print(part_one(move_list))