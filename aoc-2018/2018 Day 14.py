class Recipes:
	def __init__(self, initial):
		self.rec = initial
		self.elf1_i = 0
		self.elf2_i = 1
	def next_index(self):
		self.elf1_i = (self.elf1_i + 1 + self.rec[self.elf1_i]) % len(self.rec)
		self.elf2_i = (self.elf2_i + 1 + self.rec[self.elf2_i]) % len(self.rec)
	def next_recipe(self):
		num_new_recipes = 0
		for c in str(self.rec[self.elf1_i] + self.rec[self.elf2_i]):
			num_new_recipes += 1
			self.rec.append(int(c))
		self.next_index()
		return num_new_recipes
	def generate_recipes(self, n):
		for i in range(n):
			self.next_recipe()


# --- PART ONE ---
def next_ten_recipes(n):
	recipes = Recipes([3, 7])
	recipes.generate_recipes(n + 11)
	print("".join(str(c) for c in recipes.rec[n : n + 10]))

# --- PART TWO ---
def first_appears(puzzle_input):
	recipes = Recipes([3, 7])
	input_list = [int(c) for c in puzzle_input]
	n = 2 - len(input_list)
	done = False
	while not done:
		n += recipes.next_recipe()
		if input_list == recipes.rec[- len(input_list) :]:
			print(input_list)
			print(recipes.rec[- len(input_list) :])
			done = True


	print(n)

puzzle_input = "084601"


first_appears(puzzle_input)