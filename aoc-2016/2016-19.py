import numpy as np

def part_one(N):
	#TODO - every steps=2, 3, 4, 5, ..., start each loop by finding doing ((k*steps)% length)
	has_presents = np.arange(N) % 2 == 0
	elf = -1
	to_steal = True
	num_remaining = np.count_nonzero(has_presents)
	while num_remaining > 1:
		elf += 1
		elf %= N
		if has_presents[elf]:
			if to_steal:
				has_presents[elf] = False
				num_remaining -= 1
				to_steal = False
			else:
				to_steal = True
	return np.where(has_presents)[0] + 1

def part_two(N):
	"""linked list where each item in array contains index of next person
	Across circle = num_remaining // 2"""
	next_in_circle = np.arange(N) + 1
	next_in_circle[-1] = 0
	num_remaining = N
	elf = 0
	while num_remaining > 1:
		jump = num_remaining // 2
		next_elf = elf
		for i in range(jump - 1):
			next_elf = next_in_circle[next_elf]
		new_pointer = next_in_circle[next_in_circle[next_elf]]
		next_in_circle[next_elf] = new_pointer
		num_remaining -= 1
		elf = next_in_circle[elf]

	print(next_in_circle)
	return elf + 1



#print(part_one(3014387))
print(part_two(300))