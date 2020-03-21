puzz_input = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]

def distr(old_banks):
	new_banks = old_banks[::]
	i = new_banks.index(max(new_banks))
	value = new_banks[i]
	new_banks[i] = 0
	for j in range(value):
		i = (i + 1) % len(new_banks)
		new_banks[i] += 1
	return new_banks

def reallocate(banks):
	count = 0
	prev_banks = []
	while banks not in prev_banks:
		prev_banks.append(banks)
		banks = distr(banks)
		count += 1

	print("Total cycles:", count)
	print("Cycles in loop:", count - prev_banks.index(banks))

reallocate(puzz_input)