def calculate_checksum():
	with open("day2.txt", "r") as f:
		two_count, three_count = 0, 0
		for line in f.readlines():
			letter_count = {}
			for c in line:
				if c in letter_count:
					letter_count[c] += 1
				else:
					letter_count[c] = 1
			two_count += any(letter_count[c]==2 for c in letter_count)
			three_count+=any(letter_count[c]==3 for c in letter_count)
		return	two_count * three_count

def find_common():
	common_matrix = {}
	with open("day2.txt", "r") as f:
		IDs = [line.strip("\n") for line in f]
		for id1 in IDs:
			for id2 in IDs:
				if id1 != id2:
					common_matrix[id1 + " " + id2] = sum(id1[i]==id2[i] for i in range(len(id1)))
	s = max(common_matrix, key=common_matrix.get)
	print(s)
	common = "".join([s[i] if s[i]==s[i+27] else "" for i in range(26)])
	return	common

print(find_common())