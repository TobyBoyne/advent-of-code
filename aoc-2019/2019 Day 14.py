


def read_file():
	# {"FUEL": (n, {A: 1, B:3}}
	recipes = {}
	with open("day14.txt") as f:
		for line in f:
			LHS, RHS = line.strip("\n").split(" => ")

			terms = (term.split() for term in LHS.split(", "))
			reactants = {R: int(n) for n, R in terms}
			count, product = RHS.split()
			recipes[product] = (int(count), reactants)

	return recipes

def min_ore(recipes):
	# chemicals stores the quantity of each chemical needed
	# if any chemical (other than ORE) is greater than 0, break it into it's base parts
	chemicals = {chem: 0 for chem in recipes.keys()}
	chemicals["FUEL"] = 1
	chemicals["ORE"] = 0
	fuel_produced = 1

	while True:
		# produce one batch of any of the chemicals that have not been offset yet
		to_produce = [k for (k, v) in chemicals.items() if k != "ORE" and v > 0]
		if not to_produce:
			break
		product = to_produce[0]

		count, reactants = recipes[product]
		chemicals[product] -= count
		for reactant, quantity in reactants.items():
			chemicals[reactant] += quantity

	return chemicals

def exact_ore_per_fuel(recipes):
	ore_values = {"ORE": 1}
	while len(ore_values) <= len(recipes):
		for product, recipe in recipes.items():
			count, reactants = recipe
			# if reactant chemicals are a subset of the ore_value chemicals
			# i.e. if all of the reactants have a known corresponding ore value
			if reactants.keys() <= ore_values.keys():
				value = sum(ore_values[k] * v for k, v in reactants.items()) / count
				ore_values[product] = value

	return ore_values

recipes = read_file()
ore_per_fuel = min_ore(recipes)["FUEL"]
print("Part one:", ore_per_fuel)

large_ore_per_fuel = exact_ore_per_fuel(recipes)["FUEL"]
print("Part two:", 1e12 // large_ore_per_fuel)