def max_index(x):
	return 5 - x

def most_min_asleep():
	with open("day4.txt", 'r') as f:
		shifts = sorted([line.strip("\n") for line in f])
		guard_asleep = {}
		mins_per_guard = {}
		for line in shifts:
			if '#' in line:
				id_index = line.find('#')
				guard_id = line[id_index + 1:id_index + line[id_index:].find(' ')]
			elif "falls asleep" in line:
				sleep_start = int(line[15:17])
			else:
				mins_asleep = int(line[15:17]) - sleep_start
				if guard_id in guard_asleep:
					guard_asleep[guard_id] += mins_asleep
				else:
					guard_asleep[guard_id] = mins_asleep
					mins_per_guard[guard_id] = [0 for i in range(60)]
				for minute in range(mins_asleep):
					mins_per_guard[guard_id][sleep_start + minute] += 1

		most_sleep_guard_id = max(guard_asleep, key=guard_asleep.get)
		most_common_min = max(range(60), key=lambda n: mins_per_guard[most_sleep_guard_id][n])

		print(most_sleep_guard_id, most_common_min)
		print("Product =", int(most_sleep_guard_id) * most_common_min)

		# -- PART 2 --
		max_repeats = 0
		for guard in mins_per_guard:
			if max(mins_per_guard[guard]) > max_repeats:
				max_repeats = max(mins_per_guard[guard])
				most_repeated_min = max(range(60), key=lambda n: mins_per_guard[guard][n])
				max_guard = guard

		print(max_guard, most_repeated_min)
		print("Product =", int(max_guard) * most_repeated_min)

most_min_asleep()