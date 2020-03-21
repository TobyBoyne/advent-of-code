def read_file():
	planets = []
	with open("day6.txt") as f:
		for line in f:
			planets.append(line.strip("\n").split(")"))

	return planets


def checksum(orbit_pairs):
	# {planet: centre of orbit}
	planets = {"COM": [None, 0]}
	for planet1, planet2 in orbit_pairs:
		planets[planet2] = [planet1, -1]

	for p in planets:
		d = 0
		cur_planet = p
		while planets[cur_planet][1] == -1:
			d += 1
			cur_planet = planets[cur_planet][0]

		d += planets[cur_planet][1]
		planets[p][1] = d

	return sum(x[1] for x in planets.values())


def to_COM(planets, name):
	path = []
	cur = name
	while cur != "COM":
		cur = planets[cur]
		path.append(cur)

	return path


def dist_to_santa(orbit_pairs):
	planets = {"COM":[None, 0]}
	for planet1, planet2 in orbit_pairs:
		planets[planet2] = planet1

	path_YOU = to_COM(planets, "YOU")
	path_SAN = to_COM(planets, "SAN")

	i = 0
	sub_path1, sub_path2 = [], []
	while sub_path1 == sub_path2:
		i += 1
		sub_path1 = path_YOU[-i:]
		sub_path2 = path_SAN[-i:]

	return len(path_SAN) + len(path_YOU) - 2 * (i - 1)



orbit_pairs = read_file()
print("Part one:", checksum(orbit_pairs))
print("Part two:", dist_to_santa(orbit_pairs))