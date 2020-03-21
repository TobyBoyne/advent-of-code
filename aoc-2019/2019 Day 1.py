def fuel_for_mass(m):
	return m // 3 - 2


def total_fuel(include_fuel=False):
	total = 0
	with open("day1.txt") as f:
		for line in f:
			mass = int(line.strip("\n"))
			fuel = fuel_for_mass(mass)
			if include_fuel:
				while fuel > 0:
					total += fuel
					fuel = fuel_for_mass(fuel)

			else:
				total += fuel

	return total


print("Part one:", total_fuel())
print("Part two:", total_fuel(include_fuel=True))