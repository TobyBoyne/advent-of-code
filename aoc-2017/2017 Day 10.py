puzz_input = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
SUFFIX = [17, 31, 73, 47, 23]

num_lst = [i for i in range(256)]

def knot_hash(lengths, rounds=1):
	lst = [i for i in range(256)]
	cur = 0
	skip = 0
	for i in range(rounds):
		for length in lengths:
			if cur + length < len(lst):
				twist_seq = lst[cur:cur + length]
			else:
				twist_seq = lst[cur:] + lst[:length + cur - len(lst)]
			twist_seq = list(reversed(twist_seq))
			if cur + length < len(lst):
				lst[cur:cur + length] = twist_seq
			else:
				lst[cur:] = twist_seq[:len(lst) - cur]
				lst[:length + cur - len(lst)] = twist_seq[len(lst) - cur:]
			cur = (cur + length + skip) % len(lst)
			skip += 1

	return lst


def dense_hash(lst):
	output = ""
	for i in range(16):
		block = 0
		for j in range(16):
			block ^= lst[16*i + j]
		output += "0" * (block < 16) + hex(block)[2:]
	return output

if __name__ == "__main__":
	if puzz_input.replace(",", '').isnumeric():
		num_puzz_input = [int(x) for x in puzz_input.split(",")]
		hash_lst = knot_hash(num_puzz_input, 1)
		print("Part one:", hash_lst[0] * hash_lst[1])

	asc_puzz_input = [ord(c) for c in puzz_input]
	asc_puzz_input += SUFFIX
	hash_lst = knot_hash(asc_puzz_input, 64)
	print("Part two:", dense_hash(hash_lst))