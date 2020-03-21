import numpy as np
from collections import Counter

def decode(n):
	with open("day6.txt") as f:
		lines = np.array(list(map(lambda s: list(s.strip("\n")), f.readlines())))
		lines_trans = lines.transpose()


	return "".join(Counter(line).most_common()[n][0] for line in lines_trans)



print(decode(0))
print(decode(-1))