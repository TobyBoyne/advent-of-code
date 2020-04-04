import numpy as np

def part_one(N):
	# in the first round, all even elves will lose their present
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
	return elf + 1

print(part_one(3014387))