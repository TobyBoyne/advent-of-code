"""
After fiddling around with large gens, the following pattern is stable:
"#...#...#...#...#...#...#...#...#.####...#...#...#...#...#...#...#...#...#...#...#...
#...#...#...#...#...#..####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####"
(53 chars long)
It moves one unit to the right each gen (adding 53 to sum)

At gen 300, the sum is 16366
At gen 50,000,000,000, the sum is 16366 + (50000000000 - 300) * 53
 =
"""


num_gens = 20
L_OFFSET = 30
R_OFFSET = 300

def read():
	pots = []
	rules = {}
	with open("day12.txt", 'r') as f:
		for line_num, line in enumerate(f):
			if line_num == 0:
				pots = [False] * L_OFFSET + [True if c == '#' else False for c in line] + [False] * R_OFFSET
			else:
				rules[sum([2**n if c == '#' else 0 for n, c in enumerate(line[:5])])] = (line[-2] == '#')
	return pots, rules

def str_pots(pots):
	return "".join(['#' if plant else '.' for plant in pots])

def sum_plants(pots):
	return sum([(n - L_OFFSET) * plant for n, plant in enumerate(pots)])

def generation(pots, rules, n):
	for gen in range(n):
		new_pots = [False] * len(pots)
		for i in range(2, len(pots) - 1):
			new_pots[i] = rules[sum([2**n if plant else 0 for n, plant in enumerate(pots[i - 2 : i + 3])])]
		pots = new_pots

	return pots

def repeat_pattern(pots, rules):
	repeat_gen = 0
	current_gen = 0
	s = "#...#...#...#...#...#...#...#...#.####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####"
	for current_gen in range(300):
		pots = generation(pots, rules, 1)
		#print_pots(pots)
		if s in str_pots(pots):
			print("Gen:", current_gen + 1, "sum:", sum_plants(pots))



pots, rules = read()
repeat_pattern(pots, rules)

pots = generation(pots, rules, num_gens)
print(str_pots(pots))
print(sum_plants(pots))

