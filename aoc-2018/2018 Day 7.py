ALPHABET = list(map(chr, range(65, 91)))

def read_dependencies():
	with open("day7.txt", 'r') as f:
		dependencies = {i: [] for i in ALPHABET}
		for line in f:
			dependencies[line[36]] += [line[5]]
		return dependencies

# -- PART ONE --
def traversal_order():
	dep = read_dependencies()
	completed = []
	step_list = ""
	i = -1
	while i < len(ALPHABET) - 1:
		i += 1
		step = ALPHABET[i]
		# if the step has not already been completed, AND it is only dependent on completed steps
		if not step in completed and all(item in completed for item in dep[step]):
				step_list += step
				completed += [step]
				# start again from the beginning of the alphabet
				i = -1

	print(step_list)

# -- PART TWO --
def time_taken_by_workers(num_workers):
	dep = read_dependencies()
	completed = []
	time = 0
	workers = {i: ['', -1] for i in range(num_workers)}
	while len(completed) < len(ALPHABET):
		# check if any workers have completed their step
		for w in workers:
			if workers[w][0] != '':
				if time - workers[w][1] == ord(workers[w][0]) - 4:
					completed += workers[w][0]
					workers[w] = ['', -1]

		# assign new steps
		i = -1
		while i < len(ALPHABET) - 1:
			i += 1
			step = ALPHABET[i]
			# if the step has not already been completed, AND it is only dependent on completed steps
			# then assign it to the first free worker
			if not step in completed and all(item in completed for item in dep[step]):
				# if no other worker is working on this step at the moment
				for w in range(num_workers):
					if not any(workers[w][0] == step for w in workers) and workers[w][0] == '' :
						workers[w] = [step, time]
						# start again from the beginning of the alphabet
						i = -1


		time += 1
	time -= 1
	print(time)

traversal_order()
time_taken_by_workers(5)