keypad = ["--1--",
		  "-234-",
		  "56789",
		  "-ABC-",
		  "--D--"]

dirs = {
	"R": 1+0j,
	"L": -1+0j,
	"U": 0-1j,
	"D": 0+1j
}

def part_one(moves):
	pos = 1+1j
	code = []
	for move in moves:
		for c in move:
			next_pos = pos + dirs[c]
			x, y = int(next_pos.real), int(next_pos.imag)
			if all(0 <= coord <= 2 for coord in (x, y)):
				pos = next_pos

		code.append(str(int(pos.real + 3 * pos.imag + 1)))

	print("PART ONE:","".join(code))


def part_two(moves):
	pos = 0+2j
	code = ""
	for move in moves:
		for c in move:
			next_pos = pos + dirs[c]
			x, y = int(next_pos.real), int(next_pos.imag)
			if all(0 <= coord <= 4 for coord in (x, y)) and keypad[y][x] != "-":
				pos = next_pos

		code += keypad[int(pos.imag)][int(pos.real)]

	print("PART TWO:", code)


with open("day2.txt", "r") as f:
	moves = [line.strip("\n") for line in f]

part_one(moves)
part_two(moves)